import unittest

from opening_hours import OpeningHours

# input as key and expected value as value
test_dict = {"""
{
    "monday": [],
    "tuesday": [
        {"type": "open", "value": 36000},
        {"type": "close", "value": 64800}
    ],
    "wednesday": [], 
    "thursday": [
        {"type": "open", "value": 36000},
        {"type": "close", "value": 64800}
    ],
    "friday": [
        {"type": "open", "value": 36000}
    ],
    "saturday": [
        {"type": "close", "value": 3600},
        {"type": "open", "value": 36000}
    ],
    "sunday": [
        {"type": "close", "value": 3600},
        {"type": "open", "value": 43200},
        {"type": "close", "value": 75600}
    ]
}
""": """
Monday: Closed
Tuesday: 10 AM - 6 PM
Wednesday: Closed
Thursday: 10 AM - 6 PM
Friday: 10 AM - 1 AM
Saturday: 10 AM - 1 AM
Sunday: 12 PM - 9 PM
""", """
{
    "friday": [
        {"type": "open", "value": 64800}
    ],
    "saturday": [
        {"type": "close", "value": 3600},
        {"type": "open", "value": 32400},
        {"type": "close", "value": 39600},
        {"type": "open", "value": 57600},
        {"type": "close", "value": 82800}
    ]
}""": """
Friday: 6 PM - 1 AM
Saturday: 9 AM - 11 AM, 4 PM - 11 PM
""",
# Special case: open on Sunday, closed on Monday
"""{
    "sunday": [
        {"type": "open", "value": 64800}
    ],
    "monday": [
        {"type": "close", "value": 24800}
    ]
}""": """
Monday: Closed
Sunday: 6 PM - 6 AM
"""
}


class TestOpeningHours(unittest.TestCase):
    def test_fixed_results(self):
        for input_str, expected in test_dict.items():
            self.assertEqual(expected.strip(), OpeningHours(input_str).__str__())


if __name__ == "__main__":
    unittest.main()
