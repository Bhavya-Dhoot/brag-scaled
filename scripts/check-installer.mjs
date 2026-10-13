#!/usr/bin/env node
// The installer must never replace a skill folder it did not put there, and must replace its own.

import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const dir = mkdtempSync(path.join(tmpdir(), "brag-check-"));
const install = (...more) =>
  spawnSync(process.execPath, [path.join(root, "bin", "brag-scaled.mjs"), "--dir", dir, "--from", root, "--no-check", ...more], { encoding: "utf8" });

try {
  const mine = path.join(dir, "narrate", "SKILL.md");
  mkdirSync(path.dirname(mine), { recursive: true });
  writeFileSync(mine, "mine");

  const refused = install();
  assert.equal(refused.status, 1, "a folder from somewhere else must stop the install");
  assert.match(refused.stderr, /narrate/);
  assert.equal(readFileSync(mine, "utf8"), "mine");
  assert.deepEqual(readdirSync(dir), ["narrate"], "a refused install copies nothing");

  assert.equal(install("--force").status, 0);
  assert.notEqual(readFileSync(mine, "utf8"), "mine");
  for (const name of readdirSync(path.join(root, "skills")))
    assert.ok(existsSync(path.join(dir, name, "SKILL.md")), `${name} was not copied`);

  const stale = path.join(dir, "narrate", "removed-upstream.txt");
  writeFileSync(stale, "");
  assert.equal(install().status, 0, "a second run replaces its own folders without --force");
  assert.ok(!existsSync(stale), "a replaced folder keeps nothing from the old copy");

  console.log("installer ok");
} finally {
  rmSync(dir, { recursive: true, force: true });
}
