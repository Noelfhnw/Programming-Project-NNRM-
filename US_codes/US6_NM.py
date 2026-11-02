## US-06: See my weekly average sleep time
#**Assigned to:** 
#
#As a user, I want to see my weekly average sleep time, so that I can spot trends.
#
#**Acceptance criteria**
#- [ ] The program averages the last 7 logged nights and displays `Weekly average: 7h 00min (3 nights)`.
#- [ ] Given three nights of 7h 00min, 8h 00min, and 6h 00min, then `Weekly average: 7h 00min (3 nights)` is displayed.
#- [ ] Given more than 7 entries, only the 7 most recent are used.
#- [ ] Given only one entry, then its duration is shown with `(1 night)`.
#- [ ] Given no entries, then `⚠️ No data yet. Log a night first.` is displayed.
#- [ ] The average is rounded to the full minute.