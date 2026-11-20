
# US-11: Get a Training Recommendation
# Assigned to: Ronald

# User Story:
# As an athlete, I want a training recommendation
# (hard / easy / rest day) based on my readiness score,
# so that I train effectively without overtraining.

# Acceptance Criteria:
# - Readiness score 75-100: Hard workout.
# - Readiness score 50-74: Easy workout.
# - Readiness score 0-49: Rest day.
# - Boundary values must work correctly.
# - If no sleep data exists, display a warning.

# Implementation Plan:
# 1. Get the readiness score from US-10.
# 2. Use if / elif / else to check the score.
# 3. Select the correct training recommendation.
# 4. Display the recommendation to the user.
# 5. Handle missing sleep data.

# Example:
# Score = 94 -> Hard workout
# Score = 59 -> Easy workout
# Score = 40 -> Rest day
