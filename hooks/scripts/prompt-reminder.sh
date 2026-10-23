#!/bin/bash
# UserPromptSubmit: re-state the filing convention on every turn, so it survives
# long sessions and compaction. Silent outside a 12-pillar workspace.
root="${CLAUDE_PROJECT_DIR:-$PWD}"
[ -f "$root/life/wiki/index.md" ] || exit 0
cat >/dev/null 2>&1   # drain stdin (prompt JSON); content is not used

cat <<'MSG'
12-pillar workspace convention: personal facts shared in a message (events, health, money, people, plans) are proposed for filing right away — propose, one confirm, then write, as in /12-pillars:capture. Working sessions (brainstorming, planning, strategy) are not interrupted for filing; when one winds down, a /12-pillars:wrap is offered to file its decisions, ideas and actions. Facts about the person mentioned in passing during other tasks are noted without interrupting and offered in one batch at a natural pause.
MSG
