## US-05: See how long I slept last night
#**Assigned to:** 
#
#As a user, I want to see how long I slept last night, so that I get immediate feedback.
#
#**Acceptance criteria**
#- [ ] After a night is logged, the program displays `You slept 7h 30min.`
#- [ ] Given bedtime `22:45` and wake-up `06:15`, then `You slept 7h 30min.` is displayed.
#- [ ] Given bedtime `00:15` and wake-up `06:15`, then `You slept 6h 00min.` is displayed.
#- [ ] The message includes the difference to the 8h 00min target, e.g., `30min below your target`.
#- [ ] Given `sleep_log.csv` has no entries, then `⚠️ No data yet. Log a night first.` is displayed.
