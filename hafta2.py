"""Week 2 · The Branches — Lessons 2.1 to 2.4.
  python hafta2.py   ->  ekran/2.x/*.txt + *.png, OLCUMLER.json (d2_*)
Dates come from primary sources (kaynaklar.py). The speed rule for the cafe robot is an EXAMPLE rule."""
import numpy as np
import matplotlib.pyplot as plt
from ortak import recording, smooth, measure, session, figure
from arac import (ORANGE, BLUE, GREEN, PURPLE, GREY, INK, RED, SIM, HOUSE, SENATE, D, box, arrow, blank, timeline)


def lesson_2_1():
    """Congress: how a bill becomes law — the TAKE IT DOWN Act (S. 146, Public Law 119-12)."""
    ns = session("2.1", "bill-timeline", """
from arac import D, HOUSE, SENATE
senate, house, signed = D["take_it_down_senate"], D["take_it_down_house"], D["take_it_down_signed"]
senate, house, signed
(house - senate).days, (signed - house).days, (signed - senate).days
HOUSE // 2 + 1, SENATE // 2 + 1      # majority if every member votes
""")
    fig, ax = blank()
    ax.set_title("How a bill becomes law: S. 146, the TAKE IT DOWN Act")
    steps = [("introduced in\nthe Senate\nS. 146", BLUE), ("Senate\nconsiders\nthe bill", BLUE), ("passed Senate\n13 Feb 2025", BLUE),
             ("passed House\n28 Apr 2025", GREEN), ("signed by the\nPresident\n19 May 2025", ORANGE), ("Public Law\n119-12", INK)]
    for k, (s, c) in enumerate(steps):
        x = 0.02 + k * 0.163
        box(ax, x, 0.5, 0.135, 0.26, s, c, fs=19)
        if k:
            arrow(ax, (x - 0.02, 0.63), (x, 0.63))
    ax.text(0.5, 0.33, f"Senate to House: {(ns['house'] - ns['senate']).days} days   ·   House to signature: {(ns['signed'] - ns['house']).days} days",
            ha="center", fontsize=22, color=INK)
    ax.text(0.5, 0.12, "Both chambers must pass the same text. A veto could be overridden by two thirds of each House (Lesson 1.2).",
            ha="center", fontsize=20, color=GREY)
    figure("2.1", "bill-path")
    measure(d2_1_senate=str(D["take_it_down_senate"]), d2_1_house=str(D["take_it_down_house"]), d2_1_signed=str(D["take_it_down_signed"]),
            d2_1_days_senate_house=(D["take_it_down_house"] - D["take_it_down_senate"]).days,
            d2_1_days_house_signed=(D["take_it_down_signed"] - D["take_it_down_house"]).days,
            d2_1_days_total=(D["take_it_down_signed"] - D["take_it_down_senate"]).days, d2_1_majorities=[HOUSE // 2 + 1, SENATE // 2 + 1])


def lesson_2_2():
    """The presidency and executive orders: four AI orders, one revoked by the next administration."""
    ns = session("2.2", "orders", """
from arac import D
orders = {"14110": D["eo14110"], "14148": D["eo14148"], "14179": D["eo14179"], "14365": D["eo14365"]}
for number, signed in orders.items():
    print("Executive Order", number, "signed", signed)
in_force = (D["eo14148"] - D["eo14110"]).days     # 14110 was revoked on 20 January 2025
in_force
(D["eo14365"] - D["eo14179"]).days
""")
    fig, ax = blank()
    ax.set_title("Executive orders on artificial intelligence, Federal Register")
    timeline(ax, [(D["eo14110"], "EO 14110\nsafe, secure and\ntrustworthy AI"), (D["eo14148"], "EO 14148\nrescissions,\nincl. 14110"),
                  (D["eo14179"], "EO 14179\nremoving barriers\nto AI leadership"), (D["eo14365"], "EO 14365\nnational policy\nframework for AI")],
             y=0.5, above=[True, False, True, False], fs=19)
    ax.text(0.5, 0.05, f"EO 14110 stayed in force {ns['in_force']} days. An order binds the executive branch; a later president can revoke it.",
            ha="center", fontsize=20, color=INK)
    figure("2.2", "order-timeline")
    measure(d2_2_eo14110_days=ns["in_force"], d2_2_days_14179_to_14365=(D["eo14365"] - D["eo14179"]).days,
            d2_2_dates=[str(D[k]) for k in ("eo14110", "eo14148", "eo14179", "eo14365")])


def lesson_2_3():
    """Bureaucracy and regulators: notice and comment (5 U.S.C. 553), and checking an EXAMPLE speed rule against the recording."""
    rec = recording(); t = rec["t"]
    xy = smooth(np.column_stack([rec["cup_x"], rec["cup_y"]]), 25)
    v = np.hypot(*np.gradient(xy, t, axis=0).T)
    ns = session("2.3", "speed-rule", """
import numpy as np
from ortak import recording, smooth
rec = recording()
t = rec["t"]
xy = smooth(np.column_stack([rec["cup_x"], rec["cup_y"]]), 25)   # half-second average
speed = np.hypot(*np.gradient(xy, t, axis=0).T)                 # metres per second on the floor
limit = 0.5                                                     # EXAMPLE rule: at most 0.5 m/s inside a cafe
round(speed.max(), 3), round(float(t[speed.argmax()]), 1)
bool(speed.max() <= limit)
round(100 * float((speed > 0.05).mean()), 1)                    # percent of the time the cup is moving
""")
    fig, ax = plt.subplots()
    ax.plot(t, v, color=BLUE, label=f"cup speed on the floor · {SIM}")
    ax.axhline(0.5, color=RED, ls="--", lw=3, label="EXAMPLE rule: 0.5 m/s")
    ax.set_xlabel("time (s)"); ax.set_ylabel("speed (m/s)"); ax.set_ylim(0, 0.6); ax.legend(loc="upper left")
    ax.set_title("A regulator writes a rule, an agency checks it: does the robot stay under the limit?")
    figure("2.3", "speed-check")
    fig, ax = blank()
    ax.set_title("Rulemaking under 5 U.S.C. 553 (notice and comment)")
    steps = [("Congress passes\na law that gives\nan agency power", INK), ("Notice of proposed\nrule in the\nFederal Register", BLUE),
             ("Anyone may send\nwritten data,\nviews or arguments", GREEN), ("Final rule with\nits basis and\npurpose", BLUE), ("Usually in force\nat least 30 days\nafter publication", ORANGE)]
    for k, (s, c) in enumerate(steps):
        x = 0.02 + k * 0.198
        box(ax, x, 0.45, 0.165, 0.3, s, c, fs=18)
        if k:
            arrow(ax, (x - 0.03, 0.6), (x, 0.6))
    ax.text(0.5, 0.2, "Courts can review a rule · Congress can change the law · the president directs most agencies", ha="center", fontsize=21, color=GREY)
    figure("2.3", "notice-and-comment")
    measure(d2_3_max_speed=float(ns["speed"].max()), d2_3_t_max=float(t[ns["speed"].argmax()]), d2_3_example_limit=0.5,
            d2_3_under_limit=bool(ns["speed"].max() <= 0.5), d2_3_moving_pct=100 * float((ns["speed"] > 0.05).mean()),
            d2_3_min_days_before_effect=30, d2_3_takedown_hours=48)


def lesson_2_4():
    """The courts and judicial review: the path of a case, Marbury v. Madison, and how long one case took."""
    ns = session("2.4", "case-length", """
from arac import D
argued, decided = D["carpenter_argued"], D["carpenter_decided"]
argued, decided
(decided - argued).days            # Carpenter v. United States: argument to decision
decided.year - 1803                # years since Marbury v. Madison set out judicial review
""")
    fig, ax = blank()
    ax.set_title("The path of a federal case, and the power of judicial review")
    for k, (s, c) in enumerate([("U.S. district court\ntrial: facts\nand law", BLUE), ("U.S. court of appeals\nreviews the\ntrial court", GREEN),
                                ("Supreme Court\nchooses its cases,\ncan rule a law\nunconstitutional", ORANGE)]):
        x = 0.04 + k * 0.33
        box(ax, x, 0.5, 0.26, 0.3, s, c, fs=21)
        if k:
            arrow(ax, (x - 0.07, 0.65), (x, 0.65))
    ax.text(0.5, 0.3, "Marbury v. Madison (1803): the Court may declare an act of the legislative or executive branch unconstitutional",
            ha="center", fontsize=19, color=INK)
    ax.text(0.5, 0.18, "Federalist No. 78: the judiciary has neither force nor will, but merely judgment", ha="center", fontsize=19, color=GREY)
    figure("2.4", "case-path")
    measure(d2_4_carpenter_days=(D["carpenter_decided"] - D["carpenter_argued"]).days, d2_4_years_since_marbury=D["carpenter_decided"].year - 1803)


if __name__ == "__main__":
    lesson_2_1(); lesson_2_2(); lesson_2_3(); lesson_2_4()
    print("week 2 done")
