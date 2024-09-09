"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["4137 8947 1175 5904"],
            "answer": True,
        },
        {
            "input": ["5468 1234 5678 9123"],
            "answer": False,
        },
        {
            "input": ["4539 1488 0343 6467"],
            "answer": True,
        },
    ],
    "Extra": [
        {
            "input": ["4716 9376 3984 7011"],
            "answer": True,
        },
        {
            "input": ["4929 5123 8547 6102"],
            "answer": False,
        },
        {
            "input": ["5123 6547 2987 1221"],
            "answer": False,
        },
        {
            "input": ["4586 2920 7824 1129"],
            "answer": True,
        },
        {
            "input": ["6762 1234 5678 4321"],
            "answer": False,
        },
        {
            "input": ["3746 3269 1272 8732"],
            "answer": True,
        },
        {
            "input": ["6011 2354 8765 9876"],
            "answer": False,
        },
    ]
}
