"""Week 3 · Civil Liberties and Rights — Lessons 3.1 to 3.4.
  python hafta3.py   ->  ekran/3.x/*.txt + *.png, OLCUMLER.json (d3_*)
Court facts come from primary sources (kaynaklar.py). Camera frame rate, permit numbers and the safety zone are EXAMPLE values."""
import numpy as np
import matplotlib.pyplot as plt
from ortak import recording, measure, session, figure
from arac import (ORANGE, BLUE, GREEN, PURPLE, GREY, INK, RED, SIM, D, box, arrow, blank)


def lesson_3_1():
    """The Bill of Rights: what the first ten amendments protect, and against whom (government, not private businesses)."""
    fig, ax = blank()
    ax.set_title("The Bill of Rights limits government · examples linked to the cafe robot")
    rows = [("First Amendment", "speech, press, religion, assembly, petition", "a city wants to ban the robot's\nscreen message (EXAMPLE)", BLUE),
            ("Fourth Amendment", "no unreasonable searches and seizures", "police want the robot's\ncamera recording (Lesson 3.2)", GREEN),
            ("Fifth and Fourteenth", "due process: fair procedures before\nlife, liberty or property is taken", "a city fines the cafe for\nits robot (EXAMPLE)", ORANGE)]
    for k, (a, w, ex, c) in enumerate(rows):
        y = 0.68 - k * 0.27
        box(ax, 0.02, y, 0.25, 0.2, a, c, fs=22)
        box(ax, 0.30, y, 0.35, 0.2, w, c, fs=19, weight="normal")
        box(ax, 0.68, y, 0.30, 0.2, ex, c, fs=19, weight="normal")
    ax.text(0.5, 0.04, "Selective incorporation: through the Fourteenth Amendment most of these rights also limit the states", ha="center", fontsize=19, color=GREY)
    figure("3.1", "rights-map")
    ns = session("3.1", "first-amendment", """
from kaynaklar import TEXT
print(TEXT["first"])
TEXT["first"].startswith("Congress")     # the text names Congress; incorporation extends it to states
amendments_in_bill_of_rights = 10
amendments_in_bill_of_rights
""")
    measure(d3_1_bill_of_rights=10)


def lesson_3_2():
    """Privacy and the Fourth Amendment: cameras and data. How much data a robot makes, compared with the Carpenter case."""
    ns = session("3.2", "data-per-day", """
from ortak import recording
rec = recording()
rate = round(1 / (rec["t"][1] - rec["t"][0]))       # samples per second in the recording
rate
rows_per_day = rate * 60 * 60 * 24                  # if the robot recorded all day
rows_per_day
carpenter_points, carpenter_days = 12898, 127       # Carpenter v. United States, syllabus
carpenter_points // carpenter_days                  # whole location points per day, as in the syllabus
camera_fps = 15                                     # EXAMPLE camera: 15 frames per second
camera_fps * 60 * 60 * 10                           # frames in a ten-hour cafe day
""")
    per_day = ns["rows_per_day"]; carp = 12898 // 127; cam = 15 * 3600 * 10
    fig, ax = plt.subplots()
    names = ["Carpenter case:\nphone location points\nper day", f"robot arm and cup:\nrows per day\n({SIM})", "EXAMPLE camera:\nframes in a\nten-hour day"]
    vals = [carp, per_day, cam]
    bars = ax.bar(names, vals, color=[GREEN, BLUE, ORANGE]); ax.set_yscale("log"); ax.set_ylim(10, 2e7)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.3, f"{v:,}", ha="center", fontsize=24, weight="bold")
    ax.set_ylabel("records per day (log scale)")
    ax.set_title("How much data? A phone in a Supreme Court case and a robot in a cafe")
    figure("3.2", "data-scale")
    fig, ax = blank()
    ax.set_title("Two Fourth Amendment cases about digital data")
    box(ax, 0.03, 0.42, 0.44, 0.4, "Riley v. California\ndecided 25 June 2014\n\npolice generally need a warrant\nto search the data on a phone\ntaken at an arrest", BLUE, fs=21)
    box(ax, 0.53, 0.42, 0.44, 0.4, "Carpenter v. United States\ndecided 22 June 2018\n\ngetting 127 days of a person's\nphone location records\nwas a search", GREEN, fs=21)
    ax.text(0.5, 0.22, "Open question for the cafe: these cases limit government. A private cafe camera is a different question:\n"
                       "state privacy laws and the cafe's own rules apply, and police may ask the cafe for the recording.",
            ha="center", fontsize=19, color=INK)
    figure("3.2", "two-cases")
    measure(d3_2_rate_hz=ns["rate"], d3_2_rows_per_day=per_day, d3_2_carpenter_points=12898, d3_2_carpenter_days=127,
            d3_2_carpenter_per_day=carp, d3_2_example_fps=15, d3_2_example_frames_day=cam)


def lesson_3_3():
    """Equal protection: comparing outcomes for two groups. EXAMPLE numbers for a city that uses software to approve permits."""
    ns = session("3.3", "approval-rates", """
applied = {"neighbourhood A": 200, "neighbourhood B": 150}    # EXAMPLE numbers
approved = {"neighbourhood A": 150, "neighbourhood B": 84}
rates = {k: approved[k] / applied[k] for k in applied}
{k: round(v, 2) for k, v in rates.items()}
round(rates["neighbourhood B"] / rates["neighbourhood A"], 2)  # ratio of the two rates
""")
    r = ns["rates"]
    fig, ax = plt.subplots()
    bars = ax.bar(list(r), [100 * v for v in r.values()], color=[BLUE, ORANGE], width=0.5)
    for b, v in zip(bars, r.values()):
        ax.text(b.get_x() + b.get_width() / 2, 100 * v + 2, f"{100 * v:.0f}%", ha="center", fontsize=28, weight="bold")
    ax.set_ylim(0, 100); ax.set_ylabel("permits approved (%)")
    ax.set_title("EXAMPLE: a city approves cafe robot permits with software. Same rule for everyone?")
    ax.text(0.5, 88, "A gap is a question, not proof: courts ask whether the government treats\npeople differently and why", ha="center", fontsize=20, color=INK)
    figure("3.3", "approval-gap")
    measure(d3_3_rates=r, d3_3_ratio=float(r["neighbourhood B"] / r["neighbourhood A"]))


def lesson_3_4():
    """Balancing freedom and safety: an EXAMPLE safety zone around the robot's path."""
    rec = recording(); x, y = rec["cup_x"], rec["cup_y"]
    ns = session("3.4", "safety-zone", """
import numpy as np
from ortak import recording
rec = recording()
x, y = rec["cup_x"], rec["cup_y"]
path = np.hypot(np.diff(x), np.diff(y)).sum()        # length of the cup's path on the floor
round(path, 2)
zone = 0.75                                          # EXAMPLE rule: keep 0.75 m clear on each side of the robot's path
round(path * 2 * zone, 2)                            # floor area the rule closes, in square metres
""")
    fig, ax = plt.subplots()
    ax.plot(x, y, color=ORANGE, lw=90, alpha=0.18, solid_capstyle="round", label="EXAMPLE safety zone, 0.75 m each side")
    ax.plot(x, y, color=BLUE, lw=4, label=f"cup path · {SIM}")
    ax.set_aspect("equal"); ax.set_xlabel("x (m)"); ax.set_ylabel("y (m)"); ax.legend(loc="upper left")
    ax.set_title(f"Safety rule or limit on customers' movement? Path {ns['path']:.2f} m, zone about {ns['path'] * 2 * 0.75:.2f} m²")
    figure("3.4", "zone-map")
    measure(d3_4_path_m=float(ns["path"]), d3_4_example_zone_m=0.75, d3_4_zone_area_m2=float(ns["path"] * 2 * 0.75))


if __name__ == "__main__":
    lesson_3_1(); lesson_3_2(); lesson_3_3(); lesson_3_4()
    print("week 3 done")
