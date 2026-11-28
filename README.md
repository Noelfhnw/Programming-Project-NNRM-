# Programming-Project-NNRM-
Programming Foundations Group Project

# 😴 Sleep Tracker – Programming Project NNRM (Console)

A simple console app in Python that helps you track your sleep. You enter your sleep data for each day of the week, and the program shows you a daily and a weekly analysis with a sleep score and recommendations.

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules

## 📝 Analysis

**Problem**

People tend to sleep less than recommended and they don't know how to improve their sleep.

**Scenario**

People who acknowledge that they have to improve their sleep can use our program to get insight into their sleep behavior and receive recommendations on how to improve their sleeping habits.

### 👤 User Roles

| Role | Description |
|------|-------------|
| **Student** | Wants to track their sleep, see a daily and weekly analysis and get tips on how to improve their sleep. |

---

## 📖 User Stories

### User Story Assignment

| Member | User Stories | File |
|--------|--------------|------|
| Noel   | US-01, US-02, US-03 | `add_Sleep_data.py` |
| Nils   | US-04, US-05, US-06 | `daily.py` |
| Ronald | US-07, US-08, US-09 | `weekly.py` |
| Maryna | US-10, US-11, US-12 | `weekly.py` |

All members worked together on `main.py` (main menu) and added their functions there.

### Add Sleep Data (Noel)

#### US-01: Enter bedtime and wake-up time
As a student, I want to enter my bedtime and wake-up time for a day of the week, so that the program knows how long I was in bed.

**Acceptance Criteria:**
- The user chooses a day (1–7) and enters the times in the format `HH:MM`.
- Given `7:30`, the program saves it as `07:30`.
- Given an invalid input such as `25:00` or `abc`, `Invalid input! --> HH:MM format` is displayed and the question is asked again.

#### US-02: Enter minutes to fall asleep, morning rating and caffeine/alcohol
As a student, I want to enter how long it took me to fall asleep, how rested I feel and whether I consumed caffeine or alcohol after 2pm, so that my sleep can be analysed in more detail.

**Acceptance Criteria:**
- The minutes to fall asleep are entered as `HH:MM` and saved in minutes (e.g. `00:20` → `20`).
- The morning rating must be a whole number from 1 to 5, otherwise an error message is displayed and the question is asked again.
- Caffeine/alcohol only accepts `yes` or `no`.

#### US-03: Save and view my sleep data
As a student, I want my data to be saved and shown in an overview, so that I don't lose it and can change it later.

**Acceptance Criteria:**
- All data is saved in `sleep_data.json`. If the file does not exist, it is created automatically.
- The overview shows all 7 days with their values (empty values are shown as `None`).
- The user can change an existing value of any day.

### Daily (Nils)

#### US-04: See my daily sleep summary
As a student, I want to see a summary of last night, so that I know how long I slept.

**Acceptance Criteria:**
- Sleep duration = wake-up time − bedtime − minutes to fall asleep (also works over midnight).
- Given bedtime `23:00`, wake-up `07:00` and 15 minutes to fall asleep, `7h 45min` is displayed.
- If data for last night is missing, the program shows which fields are missing and returns to the menu.

#### US-05: Get a sleep score and a training recommendation
As a student, I want a sleep score from 0 to 100 and a training recommendation, so that I know how well I recovered.

**Acceptance Criteria:**
- Score = sleep duration (max. 50, −5 points for every 30 min below 8h) + morning rating × 5 (max. 25) + no caffeine/alcohol (25 points).
- Given 8h sleep, rating 4 and no caffeine/alcohol, the score is 50 + 20 + 25 = **95**.
- Score 75–100 → hard workout, 50–74 → easy workout, below 50 → rest day.

#### US-06: Get tips and export my daily review
As a student, I want sleep tips and to export my daily review to a text file, so that I can keep it.

**Acceptance Criteria:**
- With at least 4 logged nights, the ideal bedtime is shown (average wake-up time − 8h).
- If caffeine/alcohol = `yes`, a tip to avoid it after 2pm is displayed.
- Option `1. Export to text file` saves the review as `exports/daily_001.txt`, `daily_002.txt`, ... (existing files are never overwritten).

### Weekly (Ronald)

#### US-07: See my weekly average sleep duration
As a student, I want to see my average sleep duration of the week, so that I can see if I sleep enough.

**Acceptance Criteria:**
- The average is calculated from all logged nights of the week.
- Given nights of 7h, 8h and 6h, `7h 00min` is displayed.

#### US-08: See my average bedtime and wake-up time
As a student, I want to see my average bedtime and wake-up time, so that I can see how regular my sleep rhythm is.

**Acceptance Criteria:**
- The averages are shown in the format `HH:MM`.
- Bedtimes around midnight are calculated correctly.

#### US-09: Get a message if there is not enough data
As a student, I want to be informed if I have not logged enough nights, so that the weekly analysis makes sense.

**Acceptance Criteria:**
- The weekly analysis is only shown with at least 4 logged nights.
- Otherwise the program shows how many nights are logged (e.g. `2 of 4 nights logged`).

### Weekly (Maryna)

#### US-10: See my average morning rating
As a student, I want to see my average morning rating of the week, so that I know how rested I usually feel.

**Acceptance Criteria:**
- The average of all logged ratings (1–5) is displayed, rounded to one decimal.
- Given ratings 3, 4 and 5, `4.0` is displayed.

#### US-11: See my best and worst night
As a student, I want to see my longest and shortest night of the week, so that I can spot outliers.

**Acceptance Criteria:**
- The longest and shortest night are shown with the day and the duration.
- Given only one logged night, it is shown as both longest and shortest.

#### US-12: See how often I consumed caffeine or alcohol
As a student, I want to see on how many days I consumed caffeine or alcohol after 2pm, so that I can see how it affects my sleep.

**Acceptance Criteria:**
- The program counts the days with `yes`, e.g. `3 of 7 days`.
- If there was at least one `yes`, a tip is displayed.

---

## 📝 User Inputs

All inputs are entered in **Add sleep data** (`add_Sleep_data.py`). The user first chooses a day (1–7) and then the value to enter.

| Input | Question | Allowed values | Invalid example | Error message |
|---|---|---|---|---|
| **Bedtime** | Type in the time you went to bed (HH:MM) | `00:00`–`23:59` (`7:30` is accepted as `07:30`) | `25:00`, `7pm` | Invalid input! --> HH:MM format |
| **Wake-up time** | When did you wake up (HH:MM) | `00:00`–`23:59` | `25:00`, `abc` | Invalid input! --> HH:MM format |
| **Minutes to fall asleep** | How long did it take you to fall asleep (HH:MM) | `HH:MM`, saved in minutes | `20`, `abc` | Invalid input! --> HH:MM format |
| **Morning rating** | How good do you feel after getting up (1–5) | Whole number 1–5 | `0`, `6`, `abc` | Invalid input! --> enter a number between 1-5 |
| **Caffeine/Alcohol** | Did you consume caffeine or alcohol after 2pm (yes/no) | `yes` / `no` | `maybe`, `123` | Invalid input! --> enter yes or no |

**Morning rating scale:** 1 = miserable, 2 = bad, 3 = okay, 4 = good, 5 = very good

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

### 1. Interactive App (Console Input)

The application interacts with the user via the console. In the main menu the user can:
- **Add sleep data:** enter or change the data for each day of the week
- **Daily:** see the analysis of last night (sleep duration, sleep score, recommendations)
- **Weekly:** see the analysis of the whole week
- **Exit:** close the program

### 2. Data Validation

Every input is checked by its **own validation function** in `add_Sleep_data.py`, e.g. `time_input_valid_bedtime_data()`, `input_valid_morning_rating()` or `input_valid_caffeine_alcohol_data()`. If the input is invalid, an error message is displayed and the question is asked again. The menus also check if the chosen option exists, otherwise `!WRONG INPUT!` is displayed. This way the program does not crash on wrong input.

### 3. File Processing

- **`sleep_data.json`:** stores the sleep data of all 7 days. It is read when the program starts and saved after every input. If it does not exist, it is created automatically.
- **`exports/daily_XXX.txt`:** the daily review can be exported to a numbered text file (`daily_001.txt`, `daily_002.txt`, ...).

---

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: VS Code
- No external libraries

### 📂 Repository Structure
```text
Programming-Project-NNRM-/
├── main.py             # main menu, starts the program
├── add_Sleep_data.py   # enter, validate and save sleep data
├── daily.py            # daily analysis, sleep score and export
├── weekly.py           # weekly analysis
├── sleep_data.json     # saved sleep data (created automatically)
├── exports/            # exported daily reviews (created automatically)
└── README.md           # project description
```

### How to Run
1. Open the repository in **VS Code**
2. Open the **Terminal**
3. Run:
	```bash
	python main.py
	```

### Libraries Used

- `json`: to save and load the sleep data in `sleep_data.json`
- `os`: to check if a file exists and to create the `exports` folder
- `datetime`: to find out which day was last night

All libraries are part of the Python standard library, so no installation is required.

---

## 👥 Team & Contributions

| Name   | Contribution |
|--------|--------------|
| Noel   | `add_Sleep_data.py` – US-01, US-02, US-03 |
| Nils   | `daily.py` – US-04, US-05, US-06 |
| Ronald | `weekly.py` – US-07, US-08, US-09 |
| Maryna | `weekly.py` – US-10, US-11, US-12 |
| All    | `main.py` – main menu |

---

## 📖 User Stories (old)

These were our first user stories. During the project we noticed that they depended too much on each other, so we rewrote them (see above).

#### US-01 (old): Track Time to Fall Asleep
**Assigned to:** 

As a Worker I want to enter how many minutes it took me to fall asleep, so that I can track my sleep and understand how quickly I fall asleep.

**Acceptance Criteria:**
- [✅] The program asks the worker to enter how many minutes it took to fall asleep.
- [✅] Given a valid input of 20, the program saves 20 minutes together with today's date.
- [✅] Given an invalid input such as -5 or abc, then ⚠️ Invalid input. Enter a non-negative number of minutes. is displayed, and the question is asked again.
- [✅] After saving, ✅ Fall-asleep time saved. is displayed.
- [🟨] The worker can view previously recorded fall-asleep times together with their dates.
- [🟨] Given three recorded times of 10, 20, and 30 minutes within the last 7 days, then Weekly average fall-asleep time: 20 minutes (3 entries) is displayed.
- [🟨] Given no entries in the last 7 days, then ⚠️ No sleep data available for the last 7 days. is displayed.


#### US-02 (old): Rate Morning Sleep Quality
**Assigned to:** 

As a Student I want to rate how rested I feel each morning on a scale from 1 to 5, so that I can track my sleep quality, not just my sleep duration.

**Acceptance Criteria:**
- [ ] The program asks the student to rate how rested they feel each morning on a scale from 1 to 5.
- [ ]  The rating scale is clearly explained:
   * `1` = Very tired
   * `2` = Tired
   * `3` = Neutral
   * `4` = Rested
   * `5` = Very rested
- [ ] Given a valid input of 4, the program saves the rating together with today's date.
- [ ] Given an invalid input such as 0, 6, 2.5, or abc, then ⚠️ Invalid rating. Enter a whole number from 1 to 5. is displayed, and the question is asked again.
- [ ] After saving, ✅ Restedness rating saved. is displayed.
- [ ] The student can view previously recorded ratings together with their dates.


#### US-03 (old): Track Caffeine and Alcohol Consumption
**Assigned to:** 

As a Fitness Enthusiast, I want to record whether I consumed caffeine or alcohol during the day, so that I can understand how these habits may affect my sleep quality.

**Acceptance Criteria:**
- [✅] The program asks the user whether they consumed caffeine during the day (Yes/No).
- [✅] The program asks the user whether they consumed alcohol during the day (Yes/No).
- [✅] Given valid inputs of Yes for caffeine and No for alcohol, the program saves both answers together with today's date.
- [✅] Given an invalid input such as Maybe or 123, then ⚠️ Invalid input. Please enter Yes or No. is displayed, and the question is asked again.
- [✅] After saving, ✅ Daily habits saved. is displayed.
- [🟨] The user can view previously recorded caffeine and alcohol consumption together with their dates.


#### US-04 (old): Log bedtime and wake-up time
**Assigned to:** 

As a user, I want to log my bedtime and wake-up time, so that the program knows how long I slept.

**Acceptance criteria**
- [ ] The program asks for bedtime and wake-up time. The date is today's date.
- [ ] Given the input `25:00` or `7pm` as time, then `⚠️ Invalid time. Use HH:MM.` is displayed and the question is asked again.
- [ ] Given bedtime `23:30` and wake-up `07:00`, then the night is saved with a duration of 7h 30min.
- [ ] After saving, `✅ Night saved.` is displayed. If `sleep_log.csv` does not exist, it is created automatically.
- [ ] In none of the invalid cases does the program crash (no Python traceback).

#### US-05 (old): See how long I slept last night
**Assigned to:** 

As a user, I want to see how long I slept last night, so that I get immediate feedback.

**Acceptance criteria**
- [ ] After a night is logged, the program displays `You slept 7h 30min.`
- [ ] Given bedtime `22:45` and wake-up `06:15`, then `You slept 7h 30min.` is displayed.
- [ ] Given bedtime `00:15` and wake-up `06:15`, then `You slept 6h 00min.` is displayed.
- [ ] The message includes the difference to the 8h 00min target, e.g., `30min below your target`.
- [ ] Given `sleep_log.csv` has no entries, then `⚠️ No data yet. Log a night first.` is displayed.

#### US-06 (old): See my weekly average sleep time
**Assigned to:** 

As a user, I want to see my weekly average sleep time, so that I can spot trends.

**Acceptance criteria**
- [ ] The program averages the last 7 logged nights and displays `Weekly average: 7h 00min (3 nights)`.
- [ ] Given three nights of 7h 00min, 8h 00min, and 6h 00min, then `Weekly average: 7h 00min (3 nights)` is displayed.
- [ ] Given more than 7 entries, only the 7 most recent are used.
- [ ] Given only one entry, then its duration is shown with `(1 night)`.
- [ ] Given no entries, then `⚠️ No data yet. Log a night first.` is displayed.
- [ ] The average is rounded to the full minute.

#### US-07 (old): See my longest and shortest night
**Assigned to:** 

As a user, I want to see my longest and shortest night of the week or month, so that I can identify outliers.

**Acceptance criteria**
- [ ] The user enters `week` or `month`. Any other input shows `⚠️ Invalid choice.` and asks again.
- [ ] The output shows date and duration, e.g., `Longest: 2026-10-12 (9h 10min)` and `Shortest: 2026-10-14 (4h 45min)`.
- [ ] Given nights of 7h 00min, 9h 10min, and 4h 45min, then the longest is 9h 10min and the shortest is 4h 45min.
- [ ] Given only one entry, then it is shown as both longest and shortest.
- [ ] Given no entries, then `⚠️ No data yet. Log a night first.` is displayed.

#### US-08 (old): Compare my last night to my average bedtime and wake-up time
**Assigned to:** 

As a user, I want to see my average bedtime and wake-up time and how my last night differs from them, so that I can see how regular my sleep rhythm is.

**Acceptance criteria**
- [ ] The program averages the last 7 logged nights and displays `Average bedtime: 23:00 | Average wake-up: 07:00`.
- [ ] The difference of the last night is shown in minutes, e.g., `Last night: bedtime 30min later, wake-up 15min earlier than average`.
- [ ] Bedtimes around midnight are averaged correctly: given `23:30` and `00:30`, then the average bedtime is `00:00` (not `12:00`).
- [ ] Given the last night matches the average exactly, then `0min` difference is displayed.
- [ ] Given fewer than 3 entries, then `⚠️ At least 3 nights are needed.` is displayed.

#### US-09 (old): Get a personal sleep recommendation
**Assigned to:** 

As a user, I want a sleep recommendation (target duration and ideal bedtime), so that I know what to aim for.

**Acceptance criteria**
- [ ] The target duration is displayed as `Target: 8h 00min`.
- [ ] The user enters the desired wake-up time as `HH:MM`. Invalid input shows `⚠️ Invalid time. Use HH:MM.` and asks again.
- [ ] The ideal bedtime is the desired wake-up time minus 8h 00min.
- [ ] Given a desired wake-up of `07:00`, then `Ideal bedtime: 23:00` is displayed.
- [ ] Given a desired wake-up of `06:00`, then `Ideal bedtime: 22:00` is displayed.
- [ ] Given a desired wake-up of `05:30`, then `Ideal bedtime: 21:30` is displayed.

#### US-10 (old): Get a daily readiness score
**Assigned to:** 

As a user, I want a daily readiness score (0-100) based on my sleep length, quality, and consistency, so that I know how recovered I am.

**Acceptance criteria**
- [ ] The score is the sum of three parts, rounded to a whole number:
  - Duration (max. 50): `min(duration / 8h, 1) × 50`
  - Quality (max. 30): `quality / 5 × 30`, using the morning rating from US-02
  - Consistency (max. 20): 20 if the bedtime differs ≤ 30min from the 7-night average, otherwise 0
- [ ] Given 8h 00min sleep, quality 4, and a bedtime difference of 20min, then the score is 50 + 24 + 20 = **94**.
- [ ] Given 6h 30min sleep, quality 3, and a bedtime difference of 45min, then the score is 40.6 + 18 + 0 = **59** (rounded).
- [ ] Sleeping longer than 8h 00min does not raise the duration part above 50.
- [ ] Given fewer than 3 entries, the consistency part is 0 and `ℹ️ Consistency needs at least 3 nights.` is displayed.
- [ ] Given no quality rating for last night, then `⚠️ Rate your morning first (US-02).` is displayed and no score is shown.
- [ ] The output reads `Readiness score: <score>/100` and states that it is only an estimate.

#### US-11 (old): Get a training recommendation
**Assigned to:** 

As an athlete, I want a training recommendation (hard / easy / rest day) based on my readiness score, so that I train effectively without overtraining.

**Acceptance criteria**
- [ ] The recommendation follows the readiness score:

| Score | Recommendation |
|---|---|
| 75-100 | `💪 Hard workout` |
| 50-74 | `🚶 Easy workout` |
| 0-49 | `🛌 Rest day` |

- [ ] Given a score of 94, then `💪 Hard workout` is displayed. Given 59, then `🚶 Easy workout`. Given 40, then `🛌 Rest day`.
- [ ] Boundary values: 75 → hard, 74 → easy, 50 → easy, 49 → rest.
- [ ] Given no entries, then `⚠️ No data yet. Log a night first.` is displayed.

#### US-12 (old): Get sleep tips based on caffeine and alcohol
**Assigned to:** 

As a user, I want to receive tips based on the caffeine and alcohol I logged, so that I can support better sleep.

**Acceptance criteria**
- [✅] Given `caffeine = Yes` for last night (see US-03), then `☕ Avoid caffeine after 14:00.` is displayed.
- [✅] Given `alcohol = Yes` for last night, then `🍷 Avoid alcohol in the 3 hours before bedtime.` is displayed.
- [✅] Given both are `Yes`, then both tips are displayed.
- [✅] Given both are `No`, then `✅ No caffeine or alcohol logged. Keep it up!` is displayed.
- [🟨] Given no entries, then `⚠️ No data yet. Log a night first.` is displayed.

---

## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
