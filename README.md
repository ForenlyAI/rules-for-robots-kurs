# Rules for Robots — course files

These are the lab files of the **Rules for Robots** course on Forenly AI Academy, a course on United States government and politics for students who prepare for the AP U.S. Government and Politics exam. Every Python session, graph and number you see on the screen in the lessons was produced by these scripts.

You do not need to write a program to follow the course. The files are for students who want to repeat the calculations on their own computer or try their own EXAMPLE rules.

## What you need

- **Python 3.10 or newer**, `numpy` (2.0 or newer) and `matplotlib`. All of them are free.
- Install: `python -m pip install -r requirements.txt`
- If you do not want to install anything, upload this folder to a notebook that runs in the browser (for example Google Colab) and run the same scripts there.

## How to run

1. Download this repository (Code → Download ZIP) and open a terminal in the folder.
2. Run the weeks in order: `python hafta1.py`, `python hafta2.py`, `python hafta3.py`, `python hafta4.py`. (`hafta` means "week".)
3. The scripts write figures (`.png`) and Python session records (`.txt`) to `ekran/<lesson>/`, and the measured numbers to `OLCUMLER.json`. (`ekran` means "screen", `OLCUMLER` means "measurements".)
4. Optional: `python komut_ciz.py` draws the session records as images, as in the lessons (needs Pillow).

## Compare your results

`beklenen/OLCUMLER.json` holds the numbers our team measured in the run of 2026-10-08. `beklenen/ekran/` holds the figures and session records of the same run. (`beklenen` means "expected".) If your numbers match these, your setup works. On another computer a figure can differ by a few pixels; that is normal.

## Files

| File | Content |
|---|---|
| `ortak.py` | Shared tools: load the recording (`recording`), smoothing (`smooth`), find a sample (`at`), save sessions, figures and measurements |
| `arac.py` | The dates and thresholds used in the lessons, each read in a primary source, and drawing helpers |
| `kaynaklar.py` | The primary sources of the course (National Archives, Supreme Court, Federal Register, govinfo, EUR-Lex, the AP Course and Exam Description) and how each was checked |
| `hafta1.py` | Week 1 · Foundations: Article V thresholds, veto override, federalism, the deadlines of an executive order |
| `hafta2.py` | Week 2 · The Branches: the days of a real bill, four executive orders, an EXAMPLE speed rule checked against the recording, the length of a real case |
| `hafta3.py` | Week 3 · Civil Liberties and Rights: the Bill of Rights, data per day and Carpenter v. United States, EXAMPLE approval rates, an EXAMPLE safety zone |
| `hafta4.py` | Week 4 · Participation: margin of error, EXAMPLE public comments, the Electoral College, the dates of the EU AI Act |
| `komut_ciz.py` | Draws session records as images (optional) |
| `veri/cay_servisi_kaydi.csv` | The simulation recording: time, four arm joint angles, elbow velocity, cup position × 5666 samples (50 per second) |

The column names in the data file are Turkish. `recording()` in `ortak.py` gives them English names. Positions are in metres, time in seconds.

## About the data and the rules

The robot data is a **simulation recording**. It is **not** a measurement of a real robot. It comes from one run of Forenly AI's [cafe project](https://forenly.ai/work/cafe), in which a humanoid robot carries a cup from a counter to a table in simulation.

The robot rules (speed limit, safety zone, city permits), the polls and the comment counts are **EXAMPLE** values. Constitutional thresholds are computed from the text of the Constitution, and every real date comes from a primary source listed in `kaynaklar.py`. Legal texts are described as of 8 October 2026; later changes were not checked.

The course names institutions, not politicians, and gives both sides of contested questions with equal weight. It is not legal advice and it is not an official College Board programme; the topic names of the Course and Exam Description are listed only to show where each lesson fits.

## Final project

Write a local ordinance of three to five clauses for the cafe robot. For each clause, name the constitutional principle it rests on and who would write, enforce and review it, then defend it in a one-page argument essay. Use numbers from these scripts as evidence and say which ones are EXAMPLE values.
