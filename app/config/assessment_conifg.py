ASSESSMENT_CONFIG = {
    "duration_minutes": 120,

    "mcq": {
        "duration_minutes": 45,
        "total": 40,
        "sections": {
            "aptitude": 8,
            "analytical": 8,
            "english": 7,
            "technical": 17
        }
    },

    "coding": {
        "duration_minutes": 75,

        "dsa": [
            {
                "difficulty": "easy",
                "time_minutes": 12
            },
            {
                "difficulty": "easy-medium",
                "time_minutes": 20
            },
            {
                "difficulty": ["medium", "medium-hard"],
                "time_minutes": 28
            }
        ],

        "sql": {
            "difficulty": ["easy-medium", "medium"],
            "time_minutes": 15
        }
    }
}