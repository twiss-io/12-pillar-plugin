# Install guide

12 Pillars works in **Claude Code** (terminal and the Claude desktop app) and **Codex** (terminal and the Codex app). You need at least one of them installed and signed in:

- Claude Code: https://claude.com/claude-code
- Codex: https://developers.openai.com/codex

**Install page with one-click buttons:** https://mcp.johannsenlum.com/12-pillars

## Option A: one step (Mac / Linux)

Open **Terminal**, paste this line, and press Enter:

```bash
curl -fsSL https://raw.githubusercontent.com/twiss-io/12-pillar-plugin/main/install.sh | bash
```

The installer:
1. finds Claude Code and/or Codex on your machine,
2. installs the 12 Pillars plugin into each one, or updates it if it's already there,
3. creates your personal folder, `~/my-life`,
4. tells you exactly what to type next.

Run the same line again any time to update. The desktop apps use the same settings as the terminal, so once it's installed, it's there in the app too. Restart any app window that was already open.

Want a different folder? Put `PILLARS_HOME=~/somewhere` in front of `bash`:
`curl -fsSL https://raw.githubusercontent.com/twiss-io/12-pillar-plugin/main/install.sh | PILLARS_HOME=~/somewhere bash`

## Option B: step by step

### Claude desktop app

1. Open the **Code** tab and start a session in a personal folder (create one called `my-life`).
2. In the prompt box, type:
   ```
   /plugin install 12-pillars --marketplace twiss-io/12-pillar-plugin
   ```
   Confirm adding the marketplace, then choose **Install for you**.
   (Or use **+** → **Add plugins** after adding the marketplace.)
3. Type `/12-pillars:setup`.

### Claude Code in the terminal

```bash
claude plugin install 12-pillars --marketplace twiss-io/12-pillar-plugin
mkdir -p ~/my-life && cd ~/my-life && claude
```
Then type `/12-pillars:setup`.

On an older Claude Code, use two commands instead: `claude plugin marketplace add twiss-io/12-pillar-plugin`, then `claude plugin install 12-pillars@12-pillars`.

### Codex in the terminal

```bash
codex plugin marketplace add twiss-io/12-pillar-plugin
codex plugin add 12-pillars@12-pillars
mkdir -p ~/my-life && cd ~/my-life && codex
```
Then type `$12-pillars:setup`.

### Codex app

1. Run the two `codex plugin …` commands above once in Terminal (or use Option A). The app reads the same Codex settings.
2. Open the app, go to **Plugins**, and check that **12 Pillars** is installed. If not, install it with the **+** button.
3. Start a new chat in your `my-life` folder and type `$12-pillars:setup`.

### Windows

Option A needs a Mac or Linux shell. On Windows, use the Option B commands in PowerShell (they're the same), or run Option A inside WSL.

## After installing

- **Codex only:** the plugin has two small hooks that keep filing reliable in long chats. Codex asks you to review them first: type `/hooks` and trust both. Everything still works if you skip this.
- In setup, choose **Full setup**, **Choose parts**, or **Quick start**. Quick start takes about 2 minutes, and the rest is learned as you go.

## Update or remove

- **Update:** run Option A again. It updates Claude Code and Codex, whichever you have.
- **Claude Code auto-update:** `/plugin` → Manage marketplaces → 12-pillars → Enable auto-update. Off by default for plugins from GitHub.
- **By hand:** `claude plugin marketplace update 12-pillars` then `claude plugin update 12-pillars@12-pillars` / `codex plugin marketplace upgrade 12-pillars` then `codex plugin add 12-pillars@12-pillars`.
- **After an update:** restart open windows. If the plugin has newer workspace rules, your next session in your folder says so; `/12-pillars:lint rules` refreshes them. Your notes and anything under `## My additions` stay untouched.
- **Remove:** `claude plugin uninstall 12-pillars@12-pillars` / `codex plugin remove 12-pillars@12-pillars`. Your `my-life` folder and everything in it stays untouched.
