import yaml
import re
from feedback_generator import generate_feedback

# Load YAML files
def load_yaml(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

# Basic keyword matching for value detection
def detect_values(entry, values_data):
    detected = []
    for item in values_data['core_values']:
        if re.search(rf"\b{item['name'].lower()}\b", entry.lower()):
            detected.append(item['id'])
    return detected

# Conflict detection based on value pair matches
def detect_conflict(entry, conflicts_data, detected_values):
    for conflict in conflicts_data['moral_conflicts']:
        if all(val in detected_values for val in conflict['core_values']):
            if any(re.search(rf"\b{symptom}\b", entry.lower()) for symptom in conflict['symptoms']):
                return conflict
    return None

# Archetype lookup
def get_archetype(archetype_id, archetypes_data):
    for arche in archetypes_data['archetypes']:
        if arche['id'] == archetype_id:
            return arche
    return None

# Main analysis function
def analyze_journal_entry(entry):
    values_data = load_yaml('data/values.yaml')
    conflicts_data = load_yaml('data/conflicts.yaml')
    archetypes_data = load_yaml('data/archetypes.yaml')

    detected_values = detect_values(entry, values_data)
    conflict = detect_conflict(entry, conflicts_data, detected_values)

    if conflict:
        archetype = get_archetype(conflict['archetype_trigger'], archetypes_data)
        result = {
            "entry": entry,
            "detected_values": detected_values,
            "conflict_id": conflict['id'],
            "conflict_type": conflict['name'],
            "dissonance_score": 70,  # Placeholder logic
            "archetype": archetype['name'],
            "archetype_desc": archetype['description'],
            "reflection": conflict['reflection_prompt'],
            "feedback": generate_feedback(conflict, archetype)
        }
    else:
        result = {
            "entry": entry,
            "detected_values": detected_values,
            "conflict_id": None,
            "conflict_type": "No significant conflict detected",
            "dissonance_score": 10,
            "archetype": "None",
            "reflection": "You seem aligned today.",
            "feedback": "No moral dissonance detected."
        }

    return result
