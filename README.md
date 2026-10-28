# Programming-Project-NNRM-
Programming Foundations Group Project
Topic: Health data tracker (sleep, calories...)

Topic:

Sleep & Lifestyle Tracker
Enter sleep hours, calories, exercise, caffeine, mood, etc.
The program can calculate averages and show whether there seems to be a relationship between things like sleep and calories/mood.

# 😴 Sleep Tracker – Programming Project NNRM (Console)

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

# 😴 TEMPLATE for documentation

## 📝 Analysis

**Problem**

People tend to sleep less than recommended and they dont know how to improve their sleep.

**Scenario**

People who aknowledge that they have to improve their sleep can use our programm to get insight to their sleep behavior and recieve a plan on how to fix their sleeping habits.

### 👤 User Roles

| Role | Description |
|------|-------------|
| **student** | wants to track their sleep and wants to know the wekkly/monthly average and how to improve their sleep.


### 📖 User Stories

> 🚧 **How to write a good user story**
>
> - Use the scheme **"As a *&lt;role&gt;*, I want *&lt;capability&gt;*, so that *&lt;benefit&gt;*."**
>   The benefit ("so that …") explains *why* the story is valuable. If you cannot name a benefit, question whether the story is needed.
> - A story consists of three parts, the "three Cs": the **Card** (the short sentence), the **Conversation** (the details discussed within the team), and the **Confirmation** (the acceptance criteria, which show when the story is done).
> - Check each story against **INVEST**: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable.
> - **Acceptance criteria** must be *specific* and *testable*. Use concrete values (e.g., "CHF 25.00", "two decimal places") and avoid vague words such as "fast", "easy", "correct", or "user-friendly". A good criterion can be turned directly into a test case with an input and an expected output.
> - Write acceptance criteria either as a **checklist** of observable rules or in the **Given–When–Then** structure:
>   *Given* a starting situation, *when* an action happens, *then* a specific, observable result occurs.
> - Include at least one criterion for the **normal case** and one for an **edge case or invalid input** (e.g., a quantity of 0, an empty order, a missing file).
>
> 💡 The stories below are examples for PizzaRP. Replace them with the stories of your own project.


# 😴 Sleep Tracker: User Stories

A simple terminal program in Python (Programming Foundations, BSc Business Information Technology, FHNW). The user enters data in the console and the program saves it to a CSV file.

## User Story Assignment

| Member | User Stories | Status |
|--------|--------------|--------|
| Noel   | US-4,5,6 | 1. ⬜ <br>2. ⬜ <br>3. ⬜ |
| Nils   | US-7,8,9 | 1. ⬜ <br>2. ⬜ <br>3. ⬜ |
| Maryna | US-1,3,12 | 1. 🟨  <br>2. 🟨 <br>3. 🟨  |
| Ronald | US-2,10,11 | 1. ⬜ <br>2. ⬜ <br>3. ⬜ |

**Status legend:** ⬜ To do · 🟨 In progress · ✅ Done

## US-01: Track Time to Fall Asleep
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


## US-02: Rate Morning Sleep Quality
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


## US-03: Track Caffeine and Alcohol Consumption
**Assigned to:** 

As a Fitness Enthusiast, I want to record whether I consumed caffeine or alcohol during the day, so that I can understand how these habits may affect my sleep quality.

**Acceptance Criteria:**
- [✅] The program asks the user whether they consumed caffeine during the day (Yes/No).
- [✅] The program asks the user whether they consumed alcohol during the day (Yes/No).
- [✅] Given valid inputs of Yes for caffeine and No for alcohol, the program saves both answers together with today's date.
- [✅] Given an invalid input such as Maybe or 123, then ⚠️ Invalid input. Please enter Yes or No. is displayed, and the question is asked again.
- [✅] After saving, ✅ Daily habits saved. is displayed.
- [🟨] The user can view previously recorded caffeine and alcohol consumption together with their dates.

---

## US-04: Log bedtime and wake-up time
**Assigned to:** 

As a user, I want to log my bedtime and wake-up time, so that the program knows how long I slept.

**Acceptance criteria**
- [ ] The program asks for bedtime and wake-up time. The date is today's date.
- [ ] Given the input `25:00` or `7pm` as time, then `⚠️ Invalid time. Use HH:MM.` is displayed and the question is asked again.
- [ ] Given bedtime `23:30` and wake-up `07:00`, then the night is saved with a duration of 7h 30min.
- [ ] After saving, `✅ Night saved.` is displayed. If `sleep_log.csv` does not exist, it is created automatically.
- [ ] In none of the invalid cases does the program crash (no Python traceback).

## US-05: See how long I slept last night
**Assigned to:** 

As a user, I want to see how long I slept last night, so that I get immediate feedback.

**Acceptance criteria**
- [ ] After a night is logged, the program displays `You slept 7h 30min.`
- [ ] Given bedtime `22:45` and wake-up `06:15`, then `You slept 7h 30min.` is displayed.
- [ ] Given bedtime `00:15` and wake-up `06:15`, then `You slept 6h 00min.` is displayed.
- [ ] The message includes the difference to the 8h 00min target, e.g., `30min below your target`.
- [ ] Given `sleep_log.csv` has no entries, then `⚠️ No data yet. Log a night first.` is displayed.

## US-06: See my weekly average sleep time
**Assigned to:** 

As a user, I want to see my weekly average sleep time, so that I can spot trends.

**Acceptance criteria**
- [ ] The program averages the last 7 logged nights and displays `Weekly average: 7h 00min (3 nights)`.
- [ ] Given three nights of 7h 00min, 8h 00min, and 6h 00min, then `Weekly average: 7h 00min (3 nights)` is displayed.
- [ ] Given more than 7 entries, only the 7 most recent are used.
- [ ] Given only one entry, then its duration is shown with `(1 night)`.
- [ ] Given no entries, then `⚠️ No data yet. Log a night first.` is displayed.
- [ ] The average is rounded to the full minute.

## US-07: See my longest and shortest night
**Assigned to:** 

As a user, I want to see my longest and shortest night of the week or month, so that I can identify outliers.

**Acceptance criteria**
- [ ] The user enters `week` or `month`. Any other input shows `⚠️ Invalid choice.` and asks again.
- [ ] The output shows date and duration, e.g., `Longest: 2026-10-12 (9h 10min)` and `Shortest: 2026-10-14 (4h 45min)`.
- [ ] Given nights of 7h 00min, 9h 10min, and 4h 45min, then the longest is 9h 10min and the shortest is 4h 45min.
- [ ] Given only one entry, then it is shown as both longest and shortest.
- [ ] Given no entries, then `⚠️ No data yet. Log a night first.` is displayed.

## US-08: Compare my last night to my average bedtime and wake-up time
**Assigned to:** 

As a user, I want to see my average bedtime and wake-up time and how my last night differs from them, so that I can see how regular my sleep rhythm is.

**Acceptance criteria**
- [ ] The program averages the last 7 logged nights and displays `Average bedtime: 23:00 | Average wake-up: 07:00`.
- [ ] The difference of the last night is shown in minutes, e.g., `Last night: bedtime 30min later, wake-up 15min earlier than average`.
- [ ] Bedtimes around midnight are averaged correctly: given `23:30` and `00:30`, then the average bedtime is `00:00` (not `12:00`).
- [ ] Given the last night matches the average exactly, then `0min` difference is displayed.
- [ ] Given fewer than 3 entries, then `⚠️ At least 3 nights are needed.` is displayed.

## US-09: Get a personal sleep recommendation
**Assigned to:** 

As a user, I want a sleep recommendation (target duration and ideal bedtime), so that I know what to aim for.

**Acceptance criteria**
- [ ] The target duration is displayed as `Target: 8h 00min`.
- [ ] The user enters the desired wake-up time as `HH:MM`. Invalid input shows `⚠️ Invalid time. Use HH:MM.` and asks again.
- [ ] The ideal bedtime is the desired wake-up time minus 8h 00min.
- [ ] Given a desired wake-up of `07:00`, then `Ideal bedtime: 23:00` is displayed.
- [ ] Given a desired wake-up of `06:00`, then `Ideal bedtime: 22:00` is displayed.
- [ ] Given a desired wake-up of `05:30`, then `Ideal bedtime: 21:30` is displayed.

## US-10: Get a daily readiness score
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

## US-11: Get a training recommendation
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

## US-12: Get sleep tips based on caffeine and alcohol
**Assigned to:** 

As a user, I want to receive tips based on the caffeine and alcohol I logged, so that I can support better sleep.

**Acceptance criteria**
- [✅] Given `caffeine = Yes` for last night (see US-03), then `☕ Avoid caffeine after 14:00.` is displayed.
- [✅] Given `alcohol = Yes` for last night, then `🍷 Avoid alcohol in the 3 hours before bedtime.` is displayed.
- [✅] Given both are `Yes`, then both tips are displayed.
- [✅] Given both are `No`, then `✅ No caffeine or alcohol logged. Keep it up!` is displayed.
- [🟨] Given no entries, then `⚠️ No data yet. Log a night first.` is displayed.

**Use cases:**
- Show Menu (from `menu.txt`)
- Create Order (choose pizzas)
- Show Current Order and Total
- Print Invoice (to `invoice_xxx.txt`)

---

# 📝 User Inputs
 
This document lists all inputs the program asks the user for. The date is never asked; it is always today's date (or the date of the night being entered).
 
## 1. Daily Inputs (once per day)
 
| Input | Question | Allowed values | Invalid example | Error message |
|---|---|---|---|---|
| **Morning rating** | How rested do you feel this morning? | Whole number 1–5 | `0`, `6`, `2.5`, `abc` | ⚠️ Invalid rating. Enter a whole number from 1 to 5. |
| **Caffeine** | Did you consume caffeine after 14:00? | `Yes` / `No` | `Maybe`, `123` | ⚠️ Invalid input. Please enter Yes or No. |
| **Alcohol** | Did you consume alcohol after 14:00? | `Yes` / `No` | `Maybe`, `123` | ⚠️ Invalid input. Please enter Yes or No. |
 
**Morning rating scale:**
 
| Rating | Meaning |
|---|---|
| 1 | Very tired (bad) |
| 2 | Tired |
| 3 | Neutral |
| 4 | Rested |
| 5 | Very rested (good) |
 
## 2. Sleep Inputs (weekly data input)
 
The sleep data is entered for a time horizon of one week (7 nights). For each night, the program asks:
 
| Input | Question | Allowed values | Invalid example | Error message |
|---|---|---|---|---|
| **Bedtime** | When did you go to bed? | `HH:MM` (00:00–23:59) | `25:00`, `7pm` | ⚠️ Invalid time. Use HH:MM. |
| **Wake-up time** | When did you wake up? | `HH:MM` (00:00–23:59) | `25:00`, `7pm` | ⚠️ Invalid time. Use HH:MM. |
| **Time to fall asleep** | How long did it take you to fall asleep? | `short` / `medium` / `long` | `fast`, `20` | ⚠️ Invalid choice. Enter short, medium or long. |
 
**Time to fall asleep categories:**
 
| Category | Duration |
|---|---|
| short | less than 15 min |
| medium | 15–30 min |
| long | more than 30 min |
 
### Calculated sleep time
 
The actual sleep time is calculated from the inputs, not entered by the user:
 
```
Sleep start   = Bedtime + time to fall asleep
Sleep time    = Wake-up time − sleep start
```
 
The sleep time is rounded to 15 minutes.
 
🚧 To decide: which number of minutes is used for each category in the calculation (e.g. short = 0 min, medium = 15 min, long = 30 min).
 
## 3. Other Inputs
 
| Input | Question | Allowed values | Error message |
|---|---|---|---|
| **Time period** (US-07) | Show week or month? | `week` / `month` | ⚠️ Invalid choice. |
| **Desired wake-up time** (US-09) | When do you want to wake up? | `HH:MM` | ⚠️ Invalid time. Use HH:MM. |
| **Main menu** | Choose an option | Number of a menu option | ⚠️ Invalid choice. |
 
## 4. Validation Summary
 
All inputs can be checked with four reusable functions (e.g. in `utils.py`):
 
| Function | Used for |
|---|---|
| Whole number in a range | Morning rating, main menu |
| Yes / No | Caffeine, alcohol |
| Time `HH:MM` | Bedtime, wake-up time, desired wake-up time |
| Choice from a list | Time to fall asleep, week/month |
 
In none of the invalid cases does the program crash; it shows the error message and asks the question again.




## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

> 🚧 In this section, document how your project fulfills each criterion.  
---
The application interacts with the user via the console. Users can:
- View the pizza menu
- Select pizzas and quantities
- See the running total
- Receive an invoice generated as a file

---


### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `main-invoice.py` as follows:

- **Menu selection:** When the user enters a pizza number, the program checks if the input is a digit and within the valid menu range:
	```python
	if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
			print("⚠️ Invalid choice.")
			continue
	```
	This ensures only valid menu items can be ordered.

- **Quantity input:** After a pizza is selected, the program asks for the quantity until a whole number of at least 1 is entered:
	```python
	if not quantity.isdigit() or int(quantity) < 1:
			print("⚠️ Invalid quantity.")
			continue
	```
	This rejects `0`, negative numbers, decimal numbers, and text.

- **Menu file validation:** When reading the menu file, the program checks for valid price values and skips invalid lines:
	```python
	try:
			menu.append({"name": name, "size": size, "price": float(price)})
	except ValueError:
			print(f"⚠️ Skipping invalid line: {line.strip()}")
	```

- **Main menu options:** The main menu checks for valid options and handles invalid choices gracefully:
	```python
	else:
			print("⚠️ Invalid choice.")
	```

These checks prevent crashes and guide the user to provide correct input, matching the validation requirements described in the project guidelines.

---

---


### 3. File Processing

The application reads and writes data using files:

- **Input file:** `menu.txt` — Contains the pizza menu, one item per line in the format `PizzaName;Size;Price`.
	- Example:
		```
		Margherita;Medium;12.50
		Salami;Large;15.00
		Funghi;Small;9.00
		```
	- The application reads this file at startup to display available pizzas.

- **Output file:** `invoice_001.txt` (and similar) — Generated when an order is completed. Contains a summary of the order, including items, quantities, prices, discounts, and totals.
	- Example:
		```
		🍕 PIZZA RP INVOICE
		---------------------
		3x Diavola (Large) - CHF 52.50
		---------------------
		Discount: 10% discount (-CHF 5.25)
		TOTAL: CHF 47.25
		```
		- The output file serves as a record for both the user and the pizzeria, ensuring accuracy and transparency.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # main program logic (console application)
├── menu.txt            # pizza menu (input data file)
├── invoice_001.txt     # example of a generated invoice (output file)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones
```

### How to Run
> 🚧 Adjust if needed.
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Used for file and path operations, such as checking if the menu file exists and creating new files.
- `glob`: Used to find all invoice files matching a pattern (e.g., `invoice_*.txt`) to determine the next invoice number.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Contributions

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Student A  | Menu reading (file input) and displaying menu|
| Student B  | Order logic and data validation              |
| Student C  | Invoice generation (file output) and slides  |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
