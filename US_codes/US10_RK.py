
# US-10: Get a Daily Readiness Score
# Assigned to: Ronald

# User Story:
# As a user, I want a daily readiness score (0-100)
# based on my sleep length, quality, and consistency,
# so that I know how recovered I am.

# Acceptance Criteria:
# - Calculate a readiness score from 0 to 100.
# - Sleep duration contributes max. 50 points.
# - Morning quality contributes max. 30 points.
# - Bedtime consistency contributes max. 20 points.
# - Consistency gives 20 points if bedtime differs
#   by 30 minutes or less from the 7-night average.
# - With fewer than 3 nights, consistency is 0.
# - Without a morning rating, no score is displayed.
# - Round the total score to a whole number.
# - Explain that the score is only an estimate.

# Implementation Plan:
# 1. Get sleep duration from US-04/US-05.
# 2. Get morning quality from US-02.
# 3. Calculate average bedtime using previous nights.
# 4. Calculate the three score components.
# 5. Add the components together and round the score.
# 6. Display the final readiness score (0-100).

# Example:
# 8h sleep = 50 points
# Morning rating 4 = 24 points
# Consistent bedtime = 20 points
# Total readiness score = 94/100
