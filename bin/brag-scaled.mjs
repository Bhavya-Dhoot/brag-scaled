#!/usr/bin/env node
// Installs the brag-scaled skills, then reports what this machine still needs.
// With Claude Code on the PATH they go in as a plugin, so updates keep arriving from the marketplace.
// With --dir they are copied into any folder an agent reads skills from.
// Nothing is bundled: the skills always come from the repository, so this package cannot go stale.
import { spawnSync } from "node:child_process";
import { cpSync, existsSync, mkdtempSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { homedir, tmpdir } from "node:os";
import path from "node:path";

const REPO = "Bhavya-Dhoot/brag-scaled";
const PLUGIN = "brag-scaled@brag-scaled";
const MARK = ".brag-scaled"; // left in each copied skill, so a later run knows the folder is its own to replace
const HELP = `brag-scaled: agent skills that turn a project, a running site or a script into a short video

  npx brag-scaled                  install as a Claude Code plugin, then check this machine
  npx brag-scaled --dir <folder>   copy the skills into a folder another agent reads:
                                   ~/.agents/skills (Codex, opencode), .claude/skills, ...

  --from <checkout>   with --dir: copy from a local checkout instead of GitHub
  --force             with --dir: replace same-named skills that came from somewhere else
  --no-check          skip the setup check

Needs git. The tools the skills run are Python; the setup check lists what is missing.
https://github.com/${REPO}`;

const args = process.argv.slice(2);
const flag = (name) => args.includes(name);
const folder = (name) => {
  const i = args.indexOf(name);
  if (i < 0) return null;
  const v = args[i + 1];
  if (!v || v.startsWith("--")) throw new Error(`${name} needs a folder`);
  return path.resolve(v.replace(/^~(?=$|[\\/])/, homedir())); // PowerShell and cmd pass ~ through as typed
};
// Every command line below is a constant: paths go in through cwd, never into the line.
const sh = (line, cwd) => spawnSync(line, { stdio: "inherit", shell: true, cwd }).status === 0;
const has = (cmd) => spawnSync(`${cmd} --version`, { stdio: "ignore", shell: true }).status === 0;

function viaClaude() {
  // all four are safe to repeat: a second run updates instead of failing
  for (const step of [`marketplace add ${REPO}`, "marketplace update brag-scaled", `install ${PLUGIN}`, `update ${PLUGIN}`])
    if (!sh(`claude plugin ${step}`)) throw new Error(`"claude plugin ${step}" failed. Nothing after it was run.`);
  // the commands saying so is not the plugin being there: ask where it landed and look
  let at;
  try {
    at = JSON.parse(spawnSync("claude plugin list --json", { shell: true, encoding: "utf8" }).stdout).find((p) => p.id === PLUGIN);
  } catch {}
  if (!at || !existsSync(path.join(at.installPath, "skills")))
    throw new Error('Claude Code reported success, but "claude plugin list --json" does not show the plugin\'s files.');
  console.log(`\nInstalled as a Claude Code plugin, version ${at.version}. Restart Claude Code, then try /brag-slim.`);
  return path.join(at.installPath, "skills");
}

function viaCopy(dir, from) {
  let src = from && path.join(from, "skills"), tmp;
  try {
    if (!src) {
      if (!has("git")) throw new Error("git is needed to fetch the skills: https://git-scm.com");
      tmp = mkdtempSync(path.join(tmpdir(), "brag-scaled-"));
      if (!sh(`git clone --depth 1 --quiet https://github.com/${REPO}.git .`, tmp)) throw new Error("Could not fetch the skills from GitHub.");
      src = path.join(tmp, "skills");
    }
    const names = readdirSync(src, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name);
    const foreign = names.filter((n) => existsSync(path.join(dir, n)) && !existsSync(path.join(dir, n, MARK)));
    if (foreign.length && !flag("--force"))
      throw new Error(`${dir} already holds ${foreign.join(", ")}, and this installer did not put ${foreign.length > 1 ? "them" : "it"} there. Nothing was changed.\nMove ${foreign.length > 1 ? "them" : "it"}, choose another --dir, or add --force to replace.`);
    for (const n of names) {
      const to = path.join(dir, n);
      rmSync(to, { recursive: true, force: true }); // replace, so files removed upstream do not linger
      cpSync(path.join(src, n), to, { recursive: true, filter: (f) => !f.includes("__pycache__") });
      writeFileSync(path.join(to, MARK), "Installed by npx brag-scaled. A later run replaces this folder.\n");
    }
    console.log(`\nCopied ${names.length} skills to ${dir}. Start a new agent session, then ask for a launch video or a demo of a running site.`);
    return dir;
  } finally {
    if (tmp) rmSync(tmp, { recursive: true, force: true, maxRetries: 3 });
  }
}

function check(skills) {
  const py = ["python3", "python", "py"].find((c) => has(c));
  console.log("\nSetup check:");
  if (!py) return console.log("python          MISSING  install Python 3.9 or newer, then run this again");
  const scripts = path.join(skills, "fast-render", "scripts");
  const report = spawnSync(`${py} fastrender.py --doctor`, { shell: true, cwd: scripts, encoding: "utf8", stdio: ["ignore", "pipe", "inherit"] }).stdout || "";
  process.stdout.write(report);
  if (!report.trim() || report.includes("MISSING"))
    console.log(`\nTo add what is missing:\n  ${py} -m pip install playwright imageio-ffmpeg kokoro-onnx soundfile numpy scipy pillow\n  ${py} -m playwright install chromium`);
  if (/^tuned\s+no/m.test(report)) console.log(`\nTo calibrate, from this folder: ${scripts}\n  ${py} fastrender.py --tune`);
}

try {
  if (flag("--help") || flag("-h")) console.log(HELP);
  else {
    const dir = folder("--dir"), from = folder("--from");
    if (!dir && !has("claude"))
      throw new Error("Claude Code was not found on the PATH.\nFor another agent, name the folder it reads skills from:\n  npx brag-scaled --dir ~/.agents/skills");
    const skills = dir ? viaCopy(dir, from) : viaClaude();
    if (!flag("--no-check")) check(skills);
  }
} catch (e) {
  console.error(`\nbrag-scaled: ${e.message}`);
  process.exitCode = 1;
}
