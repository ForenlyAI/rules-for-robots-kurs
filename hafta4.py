"""Week 4 · Participation — Lessons 4.1 to 4.4.
  python hafta4.py   ->  ekran/4.x/*.txt + *.png, OLCUMLER.json (d4_*)
Poll results, comment counts and dates of an imagined rule are EXAMPLE values. EU dates come from Article 113 of Regulation (EU) 2024/1689."""
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from ortak import measure, session, figure
from arac import (ORANGE, BLUE, GREEN, PURPLE, GREY, INK, RED, HOUSE, SENATE, STATES, DC_ELECTORS, D, box, arrow, blank, timeline)


def lesson_4_1():
    """Public opinion and polling: the margin of error of a simple random sample (95 percent level)."""
    ns = session("4.1", "margin-of-error", """
import numpy as np
n = 1000                 # EXAMPLE poll: 1000 adults chosen at random
p = 0.52                 # EXAMPLE result: 52 percent support a rule for robots in cafes
moe = 1.96 * np.sqrt(p * (1 - p) / n)
round(100 * moe, 1)                          # margin of error in percentage points
round(100 * (p - moe), 1), round(100 * (p + moe), 1)
for size in (250, 1000, 4000):
    print(size, round(100 * 1.96 * np.sqrt(0.25 / size), 1))
""")
    n = np.arange(100, 4001, 10); m = 100 * 1.96 * np.sqrt(0.25 / n)
    fig, ax = plt.subplots()
    ax.plot(n, m, color=BLUE)
    for s in (250, 1000, 4000):
        v = 100 * 1.96 * np.sqrt(0.25 / s); ax.plot(s, v, "o", color=ORANGE, ms=16); ax.text(s + 60, v + 0.4, f"{s} people: ±{v:.1f} points", fontsize=22)
    ax.set_xlabel("people in the sample"); ax.set_ylabel("margin of error (percentage points)")
    ax.set_title("Bigger samples, smaller margin of error · four times the people halves the margin")
    figure("4.1", "sample-size")
    measure(d4_1_example_n=1000, d4_1_example_p=0.52, d4_1_moe_pts=float(100 * ns["moe"]),
            d4_1_interval=[float(100 * (0.52 - ns["moe"])), float(100 * (0.52 + ns["moe"]))],
            d4_1_moe_by_size={s: float(100 * 1.96 * np.sqrt(0.25 / s)) for s in (250, 1000, 4000)})


def lesson_4_2():
    """Interest groups and lobbying: who comments on a proposed rule. EXAMPLE comment counts."""
    ns = session("4.2", "comments", """
import datetime as dt
published = dt.date(2026, 3, 2)                  # EXAMPLE: a proposed rule on service robots appears in the Federal Register
deadline = published + dt.timedelta(days=60)     # EXAMPLE: a 60-day comment period
deadline
comments = {"restaurant owners' association": 420, "robot makers' trade group": 310,
            "privacy advocacy group": 380, "individual citizens": 1890}   # EXAMPLE counts
total = sum(comments.values())
total
{k: round(100 * v / total, 1) for k, v in comments.items()}
""")
    c = ns["comments"]
    fig, ax = plt.subplots()
    ax.barh(list(c), list(c.values()), color=[ORANGE, PURPLE, GREEN, BLUE])
    for k, v in enumerate(c.values()):
        ax.text(v + 20, k, f"{v} ({100 * v / ns['total']:.0f}%)", va="center", fontsize=22)
    ax.set_xlim(0, 2400); ax.set_xlabel("comments (EXAMPLE)")
    ax.set_title("EXAMPLE: comments on a proposed rule about service robots")
    figure("4.2", "comment-count")
    measure(d4_2_deadline=str(ns["deadline"]), d4_2_total=ns["total"], d4_2_shares={k: 100 * v / ns["total"] for k, v in c.items()})


def lesson_4_3():
    """Elections and media: the Electoral College total and majority, computed from the Constitution."""
    ns = session("4.3", "electoral-votes", """
from arac import HOUSE, SENATE, DC_ELECTORS
electors = HOUSE + SENATE + DC_ELECTORS   # Article II: Senators + Representatives · Twenty-third Amendment: District of Columbia
electors
electors // 2 + 1                         # majority needed to win
""")
    fig, ax = plt.subplots()
    parts = [("House seats", HOUSE, BLUE), ("Senate seats", SENATE, GREEN), ("District of Columbia", DC_ELECTORS, ORANGE)]
    left = 0
    for name, v, c in parts:
        ax.barh([0], [v], left=left, color=c, label=f"{name}: {v}"); left += v
    ax.axvline(ns["electors"] // 2 + 1, color=RED, ls="--", lw=3); ax.text(ns["electors"] // 2 + 6, 0.32, f"majority: {ns['electors'] // 2 + 1}", fontsize=24, color=RED)
    ax.set_yticks([]); ax.set_xlim(0, 560); ax.set_ylim(-0.6, 0.6); ax.set_xlabel("electoral votes"); ax.legend(loc="lower right")
    ax.set_title(f"The Electoral College: {ns['electors']} electors")
    figure("4.3", "electoral-college")
    measure(d4_3_electors=ns["electors"], d4_3_majority=ns["electors"] // 2 + 1)


def lesson_4_4():
    """Comparing with the EU AI Act: dates of application in Article 113 (original text)."""
    ns = session("4.4", "eu-dates", """
from arac import D
signed = D["eu_ai_act_signed"]
signed, D["eu_chapters_1_2"], D["eu_general"], D["eu_article_6_1"]
(D["eu_general"] - signed).days          # from adoption to general application
(D["eu_article_6_1"] - D["eu_general"]).days
""")
    fig, ax = blank()
    ax.set_title("EU Artificial Intelligence Act, Regulation (EU) 2024/1689: when the rules apply (Article 113, original text)")
    timeline(ax, [(D["eu_ai_act_signed"], "adopted"), (D["eu_chapters_1_2"], "Chapters I and II:\nincl. prohibited\npractices"),
                  (D["eu_general"], "most rules apply"), (D["eu_article_6_1"], "Article 6(1)\nhigh-risk rule")], y=0.55, above=[True, False, True, False], fs=20)
    ax.text(0.5, 0.06, "One regulation for all member states, sorted by risk  ·  in the United States: federal laws, orders, agencies and state laws",
            ha="center", fontsize=19, color=INK)
    figure("4.4", "eu-timeline")
    measure(d4_4_days_to_general=(D["eu_general"] - D["eu_ai_act_signed"]).days, d4_4_days_general_to_6_1=(D["eu_article_6_1"] - D["eu_general"]).days)


if __name__ == "__main__":
    lesson_4_1(); lesson_4_2(); lesson_4_3(); lesson_4_4()
    print("week 4 done")
