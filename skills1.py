# Import the regular expression library
import re

# Define a function to mask skills in a sentence and return masked positions
def mask_skills_with_positions(sentence, skills):
    masked_positions = []
    for skill in skills:
        pattern = re.escape(skill)
        for match in re.finditer(pattern, sentence, flags=re.IGNORECASE):
            start, end = match.span()
            masked_positions.extend(range(start, end))
        sentence = re.sub(pattern, '[MASK]', sentence, flags=re.IGNORECASE)
    return sentence, masked_positions

# Define the sentence and skills
sentence = "We are looking for a skilled Python developer with experience in machine learning."
skills = ["Python", "machine learning"]

# Mask the skills in the sentence and get masked positions
masked_sentence, masked_positions = mask_skills_with_positions(sentence, skills)

# Print the result
print("Masked Sentence:", masked_sentence)
print("Masked Positions:", masked_positions)
