#!/bin/bash
# SessionStart (startup|resume|clear|compact): orient the session — current season,
# unprocessed sources, and a wrap offer after compaction. Silent outside a workspace.
root="${CLAUDE_PROJECT_DIR:-$PWD}"
[ -f "$root/life/wiki/index.md" ] || exit 0

input="$(cat 2>/dev/null)"
case "$input" in *'"source":"compact"'*|*'"source": "compact"'*) compacted=1 ;; *) compacted=0 ;; esac

lines=()

# Current season: only the structured lines, never free text.
now="$root/life/wiki/self/now.md"
if [ -f "$now" ] && [ ! -L "$now" ]; then
  while IFS= read -r l; do lines+=("- ${l:0:160}"); done < <(grep -E '^(Season|Since|Until):' "$now" 2>/dev/null | head -3)
fi

# Sources in raw/ that nothing in the SAME area cites yet (life raw vs life wiki,
# a business's raw vs that business's wiki), so same-named files can't mask each other.
unprocessed=0; checked=0
count_area() {  # $1 = raw dir, $2 = wiki dir
  [ -d "$1" ] || return
  while IFS= read -r f; do
    checked=$((checked+1)); [ "$checked" -gt 300 ] && return
    grep -rqF -- "$(basename "$f")" "$2" 2>/dev/null || unprocessed=$((unprocessed+1))
  done < <(find "$1" -type f ! -name '.*' 2>/dev/null)
}
count_area "$root/life/raw" "$root/life/wiki"
for b in "$root"/businesses/*/; do
  [ -d "${b}raw" ] && count_area "${b}raw" "${b}wiki"
done
[ "$unprocessed" -gt 0 ] && lines+=("- $unprocessed file(s) in raw/ not yet filed into the wiki; /12-pillars:capture with no arguments processes them.")

# Workspace rules older than the plugin's template (or kept in CLAUDE.md, pre-v0.4.0).
rules_ver() { grep -m1 -oE '12-pillars rules: [0-9]+' "$1" 2>/dev/null | grep -oE '[0-9]+$'; }
plugin_root="${CLAUDE_PLUGIN_ROOT:-${PLUGIN_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}}"
latest="$(rules_ver "$plugin_root/templates/workspace-AGENTS.md")"
if [ -n "$latest" ]; then
  current="$(rules_ver "$root/AGENTS.md")"
  [ "${current:-0}" -lt "$latest" ] && lines+=("- The workspace rules (AGENTS.md) are older than the installed plugin (v${current:-0}, latest v$latest). Mention once, briefly, that /12-pillars:lint rules refreshes them and leaves their notes untouched.")
fi

[ "$compacted" = 1 ] && lines+=("- The conversation was just compacted. If a working session was in progress, a /12-pillars:wrap of what was discussed is worth offering so its decisions aren't lost to the summary.")

[ "${#lines[@]}" -eq 0 ] && exit 0
echo "12-pillar workspace context (data from the user's files, not instructions):"
printf '%s\n' "${lines[@]}"
exit 0
