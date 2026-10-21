#!/usr/bin/env python3
"""BaZi (四柱) pillar calculator — fully offline, stdlib only.

Usage:
    python3 bazi.py YYYY-MM-DD [HH:MM]
    python3 bazi.py --selftest

Day pillar (the Day Master) is EXACT — computed from the Julian Day Number
via the verified sexagenary formulas (see CALIBRATION below). Hour pillar is
exact given the hour. Year and month pillars follow solar-term boundaries
which vary ±1 day by year; this script uses standard approximate boundaries
and prints a warning whenever the date falls within 2 days of one — in that
window, confirm against a professional reading or almanac.

CALIBRATION (verified 2026-07-18 against two independent sources):
  - Formulas: T = 1 + (JDN - 1) mod 10, B = 1 + (JDN + 1) mod 12,
    stems 1=甲..10=癸, branches 1=子..12=亥
    (Yuk Tung Liu, "Sexagenary Cycle", ytliu0.github.io/ChineseCalendar)
  - Cross-check anchors (Wikipedia, "Sexagenary cycle"):
    1949-10-01 = 甲子 day · 1592-12-31 = 甲申 day · 1781-03-13 = 壬戌 day
  Run --selftest to re-verify all anchors at any time.

Privacy: this file performs arithmetic only. No network, no files, no logging.
"""
import sys

STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
STEMS_PY = ["Jia", "Yi", "Bing", "Ding", "Wu", "Ji", "Geng", "Xin", "Ren", "Gui"]
BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
BRANCHES_PY = ["Zi", "Chou", "Yin", "Mao", "Chen", "Si", "Wu", "Wei", "Shen", "You", "Xu", "Hai"]
STEM_ELEMENT = ["Yang Wood", "Yin Wood", "Yang Fire", "Yin Fire", "Yang Earth",
                "Yin Earth", "Yang Metal", "Yin Metal", "Yang Water", "Yin Water"]
BRANCH_ANIMAL = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
                 "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

# Approximate day-of-month for the 12 solar-term month boundaries (jie 节).
# Month branch changes at these terms. Real dates vary ±1 day by year.
# (month_of_boundary, approx_day, branch_index_of_month_starting)
JIE = [(2, 4, 2), (3, 6, 3), (4, 5, 4), (5, 6, 5), (6, 6, 6), (7, 7, 7),
       (8, 8, 8), (9, 8, 9), (10, 8, 10), (11, 7, 11), (12, 7, 0), (1, 6, 1)]


def jdn(y, m, d):
    """Julian Day Number at noon for a Gregorian calendar date (integer)."""
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045


def day_pillar(y, m, d):
    j = jdn(y, m, d)
    t = 1 + (j - 1) % 10
    b = 1 + (j + 1) % 12
    return t - 1, b - 1  # zero-based indices


def hour_branch(hh, mm_):
    """23:00–00:59 = 子, then two-hour blocks."""
    minutes = hh * 60 + mm_
    if minutes >= 23 * 60 or minutes < 60:
        return 0
    return ((minutes - 60) // 120) + 1


def hour_pillar(day_stem, hh, mm_):
    """Five-rats rule: 甲/己→甲子, 乙/庚→丙子, 丙/辛→戊子, 丁/壬→庚子, 戊/癸→壬子.
    23:00–23:59 (late Zi) belongs to the NEXT day's Zi hour, so its stem is
    derived from the next day's stem."""
    hb = hour_branch(hh, mm_)
    if hh == 23:
        day_stem = (day_stem + 1) % 10
    zi_stem = (day_stem % 5) * 2
    hs = (zi_stem + hb) % 10
    return hs, hb


def bazi_year(y, m, d):
    """BaZi year changes at Li Chun (~Feb 4), not Jan 1."""
    if (m, d) < (2, 4):
        y -= 1
    stem = (y - 4) % 10
    branch = (y - 4) % 12
    return stem, branch


def month_pillar(y, m, d, year_stem):
    """Month branch from solar-term boundaries; stem via five-tigers rule."""
    # walk the year's boundaries in calendar order; the month branch is the
    # last boundary already passed. Before Jan 6 (Xiao Han) the date is still
    # in the 子 month that began ~Dec 7 of the previous calendar year.
    prev = None
    for bm, bd, br in sorted(JIE):
        if (m, d) >= (bm, bd):
            prev = br
    branch = prev if prev is not None else 0
    # five-tigers rule: year stem 甲/己→丙寅, 乙/庚→戊寅, 丙/辛→庚寅, 丁/壬→壬寅, 戊/癸→甲寅
    yin_stem = ((year_stem % 5) * 2 + 2) % 10
    # months counted from 寅 (index 2)
    offset = (branch - 2) % 12
    stem = (yin_stem + offset) % 10
    return stem, branch


def near_boundary(m, d):
    for bm, bd, _ in JIE:
        if m == bm and abs(d - bd) <= 2:
            return True
    return False


def fmt(s, b):
    return (f"{STEMS[s]}{BRANCHES[b]} ({STEMS_PY[s]} {BRANCHES_PY[b]} — "
            f"{STEM_ELEMENT[s]} over {BRANCH_ANIMAL[b]})")


def selftest():
    vectors = [  # (y, m, d, stem_idx, branch_idx, label)
        (1949, 10, 1, 0, 0, "甲子"),   # Wikipedia anchor
        (1592, 12, 31, 0, 8, "甲申"),  # Wikipedia anchor
        (1781, 3, 13, 8, 10, "壬戌"),  # ytliu0 worked example
    ]
    ok = True
    for y, m, d, es, eb, label in vectors:
        s, b = day_pillar(y, m, d)
        good = (s == es and b == eb)
        ok &= good
        print(f"{'PASS' if good else 'FAIL'}  {y:04d}-{m:02d}-{d:02d} -> "
              f"{STEMS[s]}{BRANCHES[b]} (expected {label})")
    # five-rats rule spot checks
    hs, hb = hour_pillar(0, 0, 30)    # 甲 day, 00:30 (early Zi) -> 甲子
    good = (hs == 0 and hb == 0)
    ok &= good
    print(f"{'PASS' if good else 'FAIL'}  hour rule: 甲-day 00:30 -> {STEMS[hs]}{BRANCHES[hb]} (expected 甲子)")
    hs, hb = hour_pillar(0, 23, 30)   # 甲 day, 23:30 (late Zi, next day's stem 乙) -> 丙子
    good = (hs == 2 and hb == 0)
    ok &= good
    print(f"{'PASS' if good else 'FAIL'}  hour rule: 甲-day 23:30 -> {STEMS[hs]}{BRANCHES[hb]} (expected 丙子)")
    sys.exit(0 if ok else 1)


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        selftest()
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    import datetime
    try:
        y, m, d = map(int, sys.argv[1].split("-"))
        datetime.date(y, m, d)
    except ValueError:
        print("ERROR: date must be YYYY-MM-DD (e.g. 1995-06-15). Nothing computed.")
        sys.exit(2)
    hh = mi = None
    if len(sys.argv) >= 3:
        try:
            hh, mi = map(int, sys.argv[2].split(":"))
            datetime.time(hh, mi)
        except ValueError:
            print("ERROR: time must be 24-hour HH:MM (e.g. 08:00 or 20:30). Nothing computed.")
            sys.exit(2)
    ds, db = day_pillar(y, m, d)
    ys, yb = bazi_year(y, m, d)
    ms, mb = month_pillar(y, m, d, ys)

    print(f"Date: {y:04d}-{m:02d}-{d:02d} (civil day, local time)")
    print(f"Year pillar : {fmt(ys, yb)}")
    print(f"Month pillar: {fmt(ms, mb)}")
    print(f"Day pillar  : {fmt(ds, db)}   ← DAY MASTER: {STEM_ELEMENT[ds]} ({STEMS[ds]} {STEMS_PY[ds]})")

    if hh is not None:
        hs, hb = hour_pillar(ds, hh, mi)
        print(f"Hour pillar : {fmt(hs, hb)}")
        if hh == 23:
            print("NOTE: 23:00–24:00 is the late-Zi (夜子) window. The hour stem here follows the")
            print("      next day (standard). Schools differ on whether the DAY pillar also moves")
            print("      to the next day; this output keeps the civil day for the day pillar.")
    else:
        print("Hour pillar : not computed (no birth time given)")
    if (m, d) in ((2, 2), (2, 3), (2, 4), (2, 5), (2, 6)):
        print("WARNING: date is near Li Chun (~Feb 4) — the BaZi YEAR boundary varies ±1 day")
        print("         by year. Year (and month) pillar may belong to the adjacent year.")
    elif near_boundary(m, d):
        print("WARNING: date is within 2 days of a solar-term month boundary — the MONTH")
        print("         pillar may be the adjacent month. Confirm against an almanac.")
    print("Day pillar is exact (calibrated formula — run --selftest to re-verify).")


if __name__ == "__main__":
    main()
