import random

def generate_feedback(conflict, archetype):
    poetic_lines = [
        f"In the mirror of {archetype['name']}, silence grows louder.",
        f"You stood between {conflict['core_values'][0]} and {conflict['core_values'][1]} — and trembled.",
        f"Even {archetype['name']} cannot hide forever.",
        f"Your heart knew what your lips feared.",
        f"Alignment is not perfection — it's honesty."
    ]
    
    practical_nudges = [
        "Revisit the situation — what would a braver version of you do?",
        "Try journaling what you wish you had said.",
        "Reflect: What value did you protect most? What did you betray?",
        "Speak your truth safely to someone neutral.",
        "Create a micro-action that honors your suppressed value today."
    ]

    return {
        "poetic": random.choice(poetic_lines),
        "practical": random.choice(practical_nudges)
    }
