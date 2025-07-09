# M.E.D.U.S.A.

**Mirror Engine for Dissonance, Unconscious Symbolism, and Alignment**

---

## Overview

**M.E.D.U.S.A.** is a symbolic AI engine designed to detect moral dissonance in natural language inputs, such as journal entries. The system interprets ethical conflicts, identifies psychological archetypes, and generates constructive, reflective feedback.

This project integrates rule-based knowledge modeling with light natural language processing and symbolic archetype mapping to support applications in AI ethics, reflective journaling, and behavior analysis.

---

## Features

- **Conflict Detection**  
  Identifies inner moral conflicts using predefined value-pair logic (e.g., Honesty vs Peace).

- **Value Extraction**  
  Parses journal input to extract relevant ethical values.

- **Archetype Mapping**  
  Assigns symbolic psychological roles such as *Ghost*, *Martyr*, or *Rebel* based on conflict type.

- **Personalized Feedback**  
  Provides reflection prompts and structured feedback for ethical alignment.

- **Modular YAML Knowledge Base**  
  Configurable ontology of values, conflicts, archetypes, and examples.

---

## Use Cases

- Reflective journaling and self-analysis  
- Ethical AI research and LLM alignment studies  
- Narrative modeling and character trait inference  
- Digital therapy augmentation (non-clinical)  
- Educational tools on moral reasoning and value conflict

---

## System Architecture

User Input (e.g., journal)
        ↓
YAML Ontology (values, conflicts, archetypes)
        ↓
Analyzer Engine
        ↓
Conflict + Archetype Detection
        ↓
Feedback Generator (Poetic + Practical)
        ↓
Frontend 

Repository Structure

medusa_project/
├── analyzer.py                 # Core engine for conflict detection
├── feedback_generator.py       # Feedback module
├── main.py                     # FastAPI backend (optional)
├── frontend.html               # Journal interface (optional)
├── medusa_manifesto.txt        # Ethical and philosophical statement
├── README.md
└── data/
    ├── values.yaml
    ├── conflicts.yaml
    ├── archetypes.yaml
    └── examples.yaml
Installation
Clone the repository

git clone https://github.com/yourusername/medusa.git
cd medusa
Install dependencies

pip install fastapi uvicorn pyyaml
Run the API server

uvicorn main:app --reload
Launch the frontend
Open frontend.html in your browser. Ensure the API is running at http://localhost:8000.

Example
Input:

"I avoided telling my colleague the truth about their mistake. I didn’t want to hurt them."

Output:

Values: Honesty, Peace

Conflict: Honesty vs Peace

Archetype: Ghost

Reflection: "Was silence protection today, or avoidance?"

Feedback:

Poetic: "You stood between truth and calm — and swallowed both."

Practical: "Try journaling what you wish you had said."

Technologies Used
Python 3.10+

FastAPI

YAML (Knowledge Representation)

Vanilla JS (Frontend Prototype)

NLP (Token Matching / Rule-based)

Future Work
Emotion tagging via speech or biometrics

Archetype timeline visualization

Integration with journaling apps

GDPR-grade privacy wrappers

Secure cloud syncing with user encryption

License
This project is licensed under the MIT License.
You are free to use, modify, and distribute the code with proper attribution.
See the LICENSE file for full details.

⚠️ Ethical Use Notice:
M.E.D.U.S.A. is intended for educational, research, and personal development purposes.
It is not to be used for psychological manipulation, surveillance, or clinical diagnostics.

Contact:
Mrityunjya Sankar
Creator – M.E.D.U.S.A. (Mirror Engine for Dissonance, Unconscious Symbolism, and Alignment)
E-mail:- medusa.ethics.ai@gmail.com
