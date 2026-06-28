# Using /brag with any AI coding agent

The core skill logic lives in a single file: [`AGENT.md`](../../AGENT.md). It is plain markdown with zero plugin-specific assumptions — any AI coding agent can follow it.

## How to load it

### Copy-paste into custom instructions

Open your agent's custom instructions or system prompt settings and paste the contents of `AGENT.md`.

### Reference as a file

If your agent supports loading instructions from a file:

```
path/to/AGENT.md
```

### Claude Code

See [`adapters/claude-code/`](../claude-code/) for the `.claude-plugin` manifest. Install via:

```bash
rsync -a --exclude '.DS_Store' skills/brag/ ~/.claude/skills/brag/
cp adapters/claude-code/.claude-plugin/* ~/.claude/plugins/brag/
```

### opencode

See [`adapters/opencode/`](../opencode/) for the `opencode.json` config. Point your `opencode.json` at this repo's `skills/` directory, or copy the skill folder into `.opencode/skills/`.

### Cursor, Codex, Aider, etc.

1. Read `AGENT.md` and follow the steps.
2. Ensure the project has access to the `/brag` skill assets: clone or symlink this repo, or copy `skills/brag/` into your working directory.
3. Run `npx hyperframes doctor` to verify Hyperframes is available.
4. Invoke by saying `/brag` or "make a launch video".
