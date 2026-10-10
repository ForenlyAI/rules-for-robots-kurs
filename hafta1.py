"""Week 1 · Foundations — Lessons 1.1 to 1.4 (and one figure for the introduction lesson).
  python hafta1.py   ->  ekran/1.x/*.txt + *.png, ekran/0.1/*.png, OLCUMLER.json (d1_*, d0_*)
Constitutional thresholds are computed from the text of the Constitution; dates come from primary sources (kaynaklar.py).
Rules written for the cafe robot are EXAMPLE rules."""
import numpy as np
import matplotlib.pyplot as plt
from ortak import recording, measure, session, figure
from arac import (ORANGE, BLUE, GREEN, PURPLE, GREY, INK, RED, SIM, HOUSE, SENATE, STATES, D, box, arrow, blank, timeline, ceil_frac)


def lesson_1_1():
    """The Constitution as a rulebook: what the robot records, and how hard it is to change the rulebook (Article V)."""
    ns = session("1.1", "amendment-thresholds", """
from arac import HOUSE, SENATE, STATES, ceil_frac
HOUSE, SENATE, STATES
house_two_thirds = ceil_frac(HOUSE, 2, 3)     # Article V: two thirds of both Houses propose
senate_two_thirds = ceil_frac(SENATE, 2, 3)
states_three_fourths = ceil_frac(STATES, 3, 4) # three fourths of the states ratify
house_two_thirds, senate_two_thirds, states_three_fourths
house_majority, senate_majority = HOUSE // 2 + 1, SENATE // 2 + 1
house_majority, senate_majority                # a simple majority for an ordinary law
""")
    fig, ax = blank()
    ax.set_title("Changing the rulebook: Article V, the usual path (every member present)")
    box(ax, 0.03, 0.55, 0.26, 0.26, "PROPOSE\nHouse: two thirds\n" + f"{ns['house_two_thirds']} of {HOUSE}", BLUE)
    box(ax, 0.37, 0.55, 0.26, 0.26, "PROPOSE\nSenate: two thirds\n" + f"{ns['senate_two_thirds']} of {SENATE}", BLUE)
    box(ax, 0.71, 0.55, 0.26, 0.26, "RATIFY\nthree fourths of states\n" + f"{ns['states_three_fourths']} of {STATES}", GREEN)
    arrow(ax, (0.29, 0.68), (0.37, 0.68)); arrow(ax, (0.63, 0.68), (0.71, 0.68))
    box(ax, 0.20, 0.13, 0.60, 0.22, f"An ordinary law needs a simple majority:\nHouse {ns['house_majority']} of {HOUSE} · Senate {ns['senate_majority']} of {SENATE}", ORANGE)
    ax.text(0.5, 0.02, "Thresholds computed from the text of Article V and Article I · sizes as printed in the AP course description", ha="center", fontsize=18, color=GREY)
    figure("1.1", "amendment-path")
    rec = recording()
    measure(d1_1_house=HOUSE, d1_1_senate=SENATE, d1_1_states=STATES, d1_1_house_two_thirds=ns["house_two_thirds"],
            d1_1_senate_two_thirds=ns["senate_two_thirds"], d1_1_states_three_fourths=ns["states_three_fourths"],
            d1_1_house_majority=ns["house_majority"], d1_1_senate_majority=ns["senate_majority"],
            d1_1_recording_columns=len(rec), d1_1_recording_rows=len(rec["t"]))


def lesson_1_2():
    """Separation of powers and checks: the three branches; the veto and the override (Article I, Section 7)."""
    fig, ax = blank()
    ax.set_title("Separation of powers: three branches, each can check the others")
    box(ax, 0.36, 0.66, 0.28, 0.2, "LEGISLATIVE\nCongress makes laws\nArticle I", BLUE)
    box(ax, 0.03, 0.12, 0.28, 0.2, "EXECUTIVE\nPresident carries out laws\nArticle II", ORANGE)
    box(ax, 0.69, 0.12, 0.28, 0.2, "JUDICIAL\nCourts decide cases\nArticle III", GREEN)
    arrow(ax, (0.37, 0.70), (0.10, 0.33), BLUE, "override a veto,\nconfirm officials", off=(-0.15, 0.02), fs=18)
    arrow(ax, (0.24, 0.33), (0.43, 0.66), ORANGE, "veto a bill", off=(0.08, -0.04), fs=18)
    arrow(ax, (0.63, 0.70), (0.90, 0.33), BLUE, "confirms judges,\ncan impeach", off=(0.15, 0.02), fs=18)
    arrow(ax, (0.76, 0.33), (0.57, 0.66), GREEN, "can rule a law\nunconstitutional", off=(-0.10, -0.04), fs=18)
    arrow(ax, (0.31, 0.17), (0.69, 0.17), ORANGE, "nominates judges", off=(0, -0.05), fs=18)
    arrow(ax, (0.69, 0.26), (0.31, 0.26), GREEN, "can rule an action unconstitutional", off=(0, 0.05), fs=18)
    ax.text(0.5, 0.02, "Federalist No. 51: ambition must be made to counteract ambition", ha="center", fontsize=20, color=GREY)
    figure("1.2", "checks-and-balances")
    ns = session("1.2", "veto-override", """
from arac import HOUSE, SENATE, ceil_frac
# Article I, Section 7: after a veto, two thirds of each House must agree to pass the bill again
present_house, present_senate = HOUSE, SENATE     # EXAMPLE: every member present and voting
ceil_frac(present_house, 2, 3), ceil_frac(present_senate, 2, 3)
present_house, present_senate = 400, 90           # EXAMPLE: fewer members present
ceil_frac(present_house, 2, 3), ceil_frac(present_senate, 2, 3)
days_to_sign = 10                                 # Article I, Section 7: ten days, Sundays excepted
days_to_sign
""")
    measure(d1_2_override_full=[ceil_frac(HOUSE, 2, 3), ceil_frac(SENATE, 2, 3)], d1_2_override_example=[ceil_frac(400, 2, 3), ceil_frac(90, 2, 3)],
            d1_2_example_present=[400, 90], d1_2_days_to_sign=10)


def lesson_1_3():
    """Federalism: who makes the rule for the cafe robot. Layers of government and the two key clauses."""
    fig, ax = blank()
    ax.set_title("Federalism: one cafe robot, three layers of rules (rules are EXAMPLE)")
    rows = [("NATIONAL · Congress,\nfederal agencies", "a federal law on fake images online\n(real example: Lesson 2.1)", BLUE),
            ("STATE · legislature, governor", "EXAMPLE: a state law on robots\nin shops and cafes", GREEN),
            ("LOCAL · city council", "EXAMPLE: a city rule on robots\non the pavement outside", ORANGE)]
    for k, (who, what, c) in enumerate(rows):
        y = 0.66 - k * 0.27
        box(ax, 0.03, y, 0.40, 0.2, who, c, fs=22)
        box(ax, 0.55, y, 0.42, 0.2, what, c, fs=20, weight="normal")
        arrow(ax, (0.43, y + 0.1), (0.55, y + 0.1), c)
    ax.text(0.5, 0.03, "Supremacy Clause (Article VI): valid federal law wins over a conflicting state law  ·  Tenth Amendment: other powers stay with the states",
            ha="center", fontsize=17, color=INK)
    figure("1.3", "three-layers")
    ns = session("1.3", "two-clauses", """
from kaynaklar import TEXT
print(TEXT["supremacy"])
print(TEXT["tenth"])
len(TEXT["tenth"].split())        # the whole Tenth Amendment is one sentence
""")
    import kaynaklar
    measure(d1_3_tenth_words=len(kaynaklar.TEXT["tenth"].split()))


def lesson_1_4():
    """State and federal AI rules: the December 2025 executive order and its deadlines."""
    ns = session("1.4", "order-deadlines", """
import datetime as dt
from arac import D
signed = D["eo14365"]                     # Executive Order 14365, signed
signed
task_force = signed + dt.timedelta(days=30)   # Sec. 3: AI Litigation Task Force within 30 days
evaluation = signed + dt.timedelta(days=90)   # Sec. 4: evaluation of state AI laws within 90 days
task_force, evaluation
""")
    fig, ax = blank()
    ax.set_title("Executive Order 14365 (11 Dec 2025): what it directs and by when")
    timeline(ax, [(D["eo14365"], "order signed"), (ns["task_force"], "Sec. 3 deadline:\ntask force to challenge\nstate AI laws in court"),
                  (ns["evaluation"], "Sec. 4 and 5 deadline:\nlist of state laws,\nfunding conditions")], y=0.55, above=[True, False, True])
    ax.text(0.5, 0.08, "Sec. 8: a proposal to Congress for a national framework that would preempt conflicting state AI laws\n"
                       "The order directs federal officials; it does not by itself repeal any state law",
            ha="center", fontsize=19, color=INK)
    figure("1.4", "order-timeline")
    measure(d1_4_signed=str(D["eo14365"]), d1_4_task_force=str(ns["task_force"]), d1_4_evaluation=str(ns["evaluation"]))


def intro():
    """Introduction lesson: the recording at a glance, cup position on the floor and cup height."""
    rec = recording(); t = rec["t"]
    fig, (a1, a2) = plt.subplots(1, 2, gridspec_kw=dict(width_ratios=[1.2, 1]))
    a1.plot(rec["cup_x"], rec["cup_y"], color=BLUE); a1.set_aspect("equal")
    a1.plot(rec["cup_x"][0], rec["cup_y"][0], "o", color=GREEN, ms=16, label="start: counter")
    a1.plot(rec["cup_x"][-1], rec["cup_y"][-1], "s", color=ORANGE, ms=16, label="end: table")
    a1.set_xlabel("x (m)"); a1.set_ylabel("y (m)"); a1.legend(loc="lower right"); a1.set_title("Path of the cup on the floor")
    a2.plot(t, rec["cup_z"], color=INK); a2.set_xlabel("time (s)"); a2.set_ylabel("cup height (m)"); a2.set_title("Height of the cup")
    fig.suptitle(f"One robot, one cafe, many rules · {SIM}", fontsize=28)
    figure("0.1", "recording-overview")
    measure(d0_1_samples=len(t), d0_1_duration_s=float(t[-1]), d0_1_rate_hz=float(round(1 / (t[1] - t[0]))))


if __name__ == "__main__":
    lesson_1_1(); lesson_1_2(); lesson_1_3(); lesson_1_4(); intro()
    print("week 1 done")
