# Instruments — optional profiles

> Astrology and personality profiles are optional extra lenses. They run in the background, they're shown whenever the user asks, and they never make decisions for anyone.

## 1. Always the user's choice

During setup, offer instruments as one choice, before any instrument question:

- **Yes, include them**: run the astrology profile and the personality type
- **Just one**: let them pick which; mark the other one `skipped`
- **Not now**: mark them `deferred`; offer once more at the end of setup
- **No**: mark them `skipped`; never bring them up again unless the user does

A no is completely fine and needs no explanation. Everything else in the plugin works the same without them.

## 2. What they're for

Instruments add three things to the AI's understanding of a person:
1. **Risk**: what to watch out for.
2. **Timing**: an extra lens on when to push and when to hold.
3. **Expectations**: a counterweight to the person's default emotional read.

They are **tools, not verdicts**. The failure mode to avoid is the profile "holding hope" for someone, where they wait on a reading instead of acting. Profiles never define who someone is and never decide anything.

## 3. The quiet rule

- Results live in `life/wiki/self/instruments/`. They inform how the AI reads the person, but the AI does **not** bring up chart terms, type numbers, or readings in conversation unless the user does first.
- Quiet is not secret. Tell the user what the information is for when collecting it. Show the full profile whenever they ask ("show my profile"). If profile-based reasoning shaped a piece of advice and they ask why, say so.
- Record every result with a date and treat it as a working read that can be revisited, not a permanent label.

## 4. The two bundled instruments

**Astrology profile (Chinese four-pillar chart).** User-facing word: **"astrology"**. Don't use technical chart vocabulary in questions or confirmations. Ask with a fill-in template:

> I can keep an astrology-based profile on file to understand you a bit better. Totally optional. If you'd like it, pop in:
>
> **When:**
> - Date:
> - Time (to the hour if you know it):
>
> **Where:**
> - Country / city:

The place is kept on file for completeness. The calculation uses the local clock date and time.

Compute it **only** with the bundled script `instruments/bazi.py` (the command running this step gives you its full path), never by hand and never with a web calculator, since birth data must not leave the machine. Pass the date as `YYYY-MM-DD` and the time as 24-hour `HH:MM`. Convert "8am" to `08:00` yourself, and omit the time if it's unknown. If the script prints an `ERROR`, fix the input and rerun; never save a partial chart.

Save the inputs and the full output, including any warnings, to `life/wiki/self/instruments/astrology.md`, with the standard wiki frontmatter (`type: self`, `pillars: [faith]`, `sources:` pointing to the raw file of the answers). Then just confirm: "Noted. Ask to see it any time." If Python isn't available, save the inputs and mark the chart pending. The script self-checks with `--selftest`.

**Personality type (Enneagram).** Ask if they already know their type (offer clickable options: yes, I know it · no, help me find it · skip). If they don't know it, run the bundled protocol `instruments/enneagram-typing.md` (the command running this step gives you its full path; about 5 minutes, all multiple choice). Save the result with a confidence level and date to `life/wiki/self/instruments/enneagram.md`, with the standard wiki frontmatter and a `## Sources` section.

**Others** (MBTI, DISC, numerology, other astrology systems): if the user already has results, record them the same way. Don't run new tests for them.
