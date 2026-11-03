# Sourced by the hooks: sets $root to the 12-pillar workspace containing the current
# folder (a chat may be opened inside a pillar or unit folder), and $layout to
# "pillars" (0.8.0+) or "old" (life/ + area folders). Leaves $root empty outside one.
root=""; layout=""
d="${CLAUDE_PROJECT_DIR:-$PWD}"
for _ in 1 2 3 4 5 6 7; do
  if [ -d "$d/02-identity" ] && [ -f "$d/index.md" ]; then root="$d"; layout="pillars"; break; fi
  if [ -f "$d/life/wiki/index.md" ]; then root="$d"; layout="old"; break; fi
  [ "$d" = "/" ] && break
  d="$(dirname "$d")"
done
