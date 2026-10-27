#!/usr/bin/env bash
# One-step installer for the 12 Pillars plugin.
# Installs (or updates) it in Claude Code and/or Codex, whichever is on this machine.
#   curl -fsSL https://raw.githubusercontent.com/twiss-io/12-pillar-plugin/main/install.sh | bash
set -u

REPO="twiss-io/12-pillar-plugin"
NAME="12-pillars"
WORKSPACE="${PILLARS_HOME:-$HOME/my-life}"
installed=()

say() { printf '%s\n' "$*"; }
ok()  { printf '  ✓ %s\n' "$*"; }
bad() { printf '  ✗ %s\n' "$*"; }

say "12 Pillars installer"
say ""

if command -v claude >/dev/null 2>&1; then
  say "Claude Code found."
  if claude plugin list 2>/dev/null | grep -q "$NAME@$NAME"; then
    claude plugin marketplace update "$NAME" >/dev/null 2>&1
    if claude plugin update "$NAME@$NAME" >/dev/null 2>&1; then ok "Updated to the latest version"; installed+=("claude"); else bad "Update failed. Try: claude plugin update $NAME@$NAME"; fi
  else
    claude plugin marketplace add "$REPO" >/dev/null 2>&1
    if claude plugin install "$NAME@$NAME" >/dev/null 2>&1; then ok "Installed"; installed+=("claude"); else bad "Install failed. Try: claude plugin install $NAME@$NAME"; fi
  fi
  say ""
fi

# Codex: the CLI on PATH, or the copy bundled inside the ChatGPT / Codex desktop app.
CODEX=""; CODEX_ON_PATH=0
if command -v codex >/dev/null 2>&1; then CODEX="$(command -v codex)"; CODEX_ON_PATH=1
else
  for c in "/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex" \
           "$HOME/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex" \
           "/Applications/Codex.app/Contents/Resources/codex"; do
    [ -x "$c" ] && { CODEX="$c"; break; }
  done
fi
codex() { "$CODEX" "$@"; }

if [ -n "$CODEX" ]; then
  say "Codex found."
  codex plugin marketplace upgrade "$NAME" >/dev/null 2>&1 || codex plugin marketplace add "$REPO" >/dev/null 2>&1
  if codex plugin add "$NAME@$NAME" >/dev/null 2>&1; then ok "Installed (latest version)"; installed+=("codex"); else bad "Install failed. Try: codex plugin add $NAME@$NAME"; fi
  say ""
fi

if [ "${#installed[@]}" -eq 0 ]; then
  say "Neither Claude Code nor Codex was found on this machine (or the install failed)."
  say "Install one first, then run this again:"
  say "  Claude Code: https://claude.com/claude-code"
  say "  Codex:       https://developers.openai.com/codex"
  exit 1
fi

mkdir -p "$WORKSPACE"
say "Your personal folder: $WORKSPACE"
say ""
say "Next:"
for t in "${installed[@]}"; do
  case "$t" in
    claude) say "  Claude Code:  cd \"$WORKSPACE\" && claude      then type  /12-pillars:setup"
            say "  Claude app:   Code tab → open the folder above → type  /12-pillars:setup" ;;
    codex)  [ "$CODEX_ON_PATH" = 1 ] && say "  Codex:        cd \"$WORKSPACE\" && codex       then type  \$12-pillars:setup"
            say "  Codex app:    open the folder above → type  \$12-pillars:setup  (trust the hooks in /hooks when asked)" ;;
  esac
done
say ""
say "Restart any Claude or Codex window that was already open."
