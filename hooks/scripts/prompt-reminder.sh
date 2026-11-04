#!/bin/bash
# UserPromptSubmit: re-state the filing convention on every turn, so it survives
# long sessions and compaction. Silent outside a 12-pillar workspace.
. "$(dirname "$0")/find-root.sh"
[ -n "$root" ] || exit 0
cat >/dev/null 2>&1   # drain stdin (prompt JSON); content is not used

cat <<'MSG'
12-pillar workspace convention: personal facts worth keeping (people, deadlines, decisions, numbers, events, goals, changes, files they send; not small talk, passing moods, questions or task help; skip when borderline) are filed right away without asking first, as the plugin's frameworks/llm-wiki.md section 4 "Filing" describes, then reported in one or two plain lines (the user can correct or say undo). Questions are answered from the workspace pages. Working sessions (brainstorming, planning, strategy) are not interrupted; when one winds down, the 12-pillars wrap files its decisions, ideas and actions. Facts about the person mentioned in passing during other tasks are filed at a natural pause and mentioned in one line.
MSG
