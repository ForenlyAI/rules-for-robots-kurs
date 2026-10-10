"""Rules for Robots — shared drawing helpers and the dates and thresholds used in the lessons.

Every date below was read in a primary source (see kaynaklar.py). Every number that is not from the recording, from the
Constitution or from a primary source is marked EXAMPLE on the screen."""
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ORANGE, BLUE, GREEN, PURPLE, GREY, INK, RED = "#C2410C", "#1D4ED8", "#0F766E", "#7E22CE", "#6B7280", "#111111", "#B91C1C"
SIM = "simulation recording"

# Sizes printed in the AP U.S. Government and Politics Course and Exam Description (EK 2.1.A.2) and states in the Union
HOUSE, SENATE, STATES = 435, 100, 50
DC_ELECTORS = 3      # Twenty-third Amendment: no more electors than the least populous state, which has 1 House seat + 2 Senators

# Dates read in primary sources (kaynaklar.py)
D = dict(
    take_it_down_senate=dt.date(2025, 2, 13),     # Public Law 119-12, legislative history: passed Senate
    take_it_down_house=dt.date(2025, 4, 28),      # passed House
    take_it_down_signed=dt.date(2025, 5, 19),     # approved (Public Law 119-12)
    eo14110=dt.date(2023, 10, 30),                # Executive Order 14110 signed
    eo14148=dt.date(2025, 1, 20),                 # Executive Order 14148 signed (revokes 14110 among others)
    eo14179=dt.date(2025, 1, 23),                 # Executive Order 14179 signed
    eo14365=dt.date(2025, 12, 11),                # Executive Order 14365 signed
    carpenter_argued=dt.date(2017, 11, 29),       # Carpenter v. United States, argued
    carpenter_decided=dt.date(2018, 6, 22),       # decided
    riley_decided=dt.date(2014, 6, 25),           # Riley v. California, decided
    eu_ai_act_signed=dt.date(2024, 6, 13),        # Regulation (EU) 2024/1689, done at Brussels
    eu_chapters_1_2=dt.date(2025, 2, 2),          # Article 113 (a): Chapters I and II apply
    eu_general=dt.date(2026, 8, 2),               # Article 113: general date of application
    eu_article_6_1=dt.date(2027, 8, 2),           # Article 113 (c): Article 6(1) applies
)


def box(ax, x, y, w, h, text, color=BLUE, fs=22, fill=None, weight="bold"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.008,rounding_size=0.03", fc=fill or "#FFFFFF", ec=color, lw=3))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=color if weight == "bold" else INK, weight=weight, wrap=True)


def arrow(ax, p, q, color=INK, text=None, fs=18, off=(0, 0.04), lw=2.5, style="-|>"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=26, color=color, lw=lw))
    if text:
        ax.text((p[0] + q[0]) / 2 + off[0], (p[1] + q[1]) / 2 + off[1], text, ha="center", va="center", fontsize=fs, color=color)


def blank(xlim=(0, 1), ylim=(0, 1)):
    fig, ax = plt.subplots()
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.axis("off")
    return fig, ax


def timeline(ax, events, y=0.5, color=BLUE, fs=20, above=None):
    """events: list of (date, label). Draws a horizontal time line with labelled ticks, alternating above and below."""
    d0, d1 = min(e[0] for e in events), max(e[0] for e in events)
    span = max((d1 - d0).days, 1)
    xs = [0.06 + 0.88 * (e[0] - d0).days / span for e in events]
    ax.plot([0.03, 0.97], [y, y], color=GREY, lw=4)
    for k, (x, (d, lab)) in enumerate(zip(xs, events)):
        up = (k % 2 == 0) if above is None else above[k]
        ax.plot(x, y, "o", color=color, ms=20)
        ax.plot([x, x], [y, y + (0.1 if up else -0.1)], color=color, lw=2)
        ax.text(x, y + (0.13 if up else -0.13), f"{d:%d %b %Y}\n{lab}", ha="center", va="bottom" if up else "top", fontsize=fs, color=INK)
    return xs


def ceil_frac(n, num, den):
    """Smallest whole number that is at least num/den of n."""
    return -(-n * num // den)
