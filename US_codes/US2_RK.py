
# US-02: Rate Morning Sleep Quality
# Assigned to: Ronald

# User Story:
# As a Student, I want to rate how rested I feel each
# morning on a scale from 1 to 5, so that I can track
# my sleep quality, not just my sleep duration.

# Acceptance Criteria:
# - Ask the user for a morning rating (1-5).
# - Explain what each rating means.
# - Accept only whole numbers from 1 to 5.
# - Invalid inputs (0, 6, 2.5, abc) must be rejected.
# - Save the rating together with today's date.
# - Display a confirmation after saving.
# - Allow the user to view previous ratings.

# Implementation Plan:
# 1. Create a function to ask for the morning rating.
# 2. Use a while loop to validate the input.
# 3. Convert the valid input into an integer.
# 4. Store the rating with the date.
# 5. Connect the function to the shared sleep data.
# 6. Display previously saved ratings when requested.
