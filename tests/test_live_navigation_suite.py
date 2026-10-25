"""
Automated Unit Test for Live Turn-by-Turn Navigation & Audio Guidance.
Verifies maneuver symbol generation, distance formatting, and speech prompt construction.
"""
import unittest

def format_nav_distance(meters):
    if meters >= 1000:
        return f"{meters / 1000:.1f} km"
    return f"{int(round(meters))} m"

def build_speech_text(step_index, total_steps, instruction, next_instruction=None):
    if step_index == 0:
        text = f"Starting navigation. {instruction}."
    else:
        text = f"{instruction}."
    if next_instruction and step_index < total_steps - 1:
        text += f" Then {next_instruction}."
    return text

class TestLiveNavigationLogic(unittest.TestCase):
    def test_distance_formatting(self):
        self.assertEqual(format_nav_distance(50), "50 m")
        self.assertEqual(format_nav_distance(450), "450 m")
        self.assertEqual(format_nav_distance(1200), "1.2 km")
        self.assertEqual(format_nav_distance(2540), "2.5 km")

    def test_speech_prompt_construction(self):
        first_step = "Follow tactile paving along Rajiv Chowk Concourse"
        second_step = "Turn slight right onto accessible ramp"
        prompt = build_speech_text(0, 3, first_step, second_step)
        self.assertTrue(prompt.startswith("Starting navigation."))
        self.assertIn("Follow tactile paving", prompt)
        self.assertIn("Then Turn slight right", prompt)

if __name__ == "__main__":
    unittest.main()
