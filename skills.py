import re

# Define a function to mask skills in a sentence
def mask_skills(sentence, skills):
    for skill in skills:
        sentence = re.sub(re.escape(skill), '[MASK]', sentence, flags=re.IGNORECASE)
    return sentence

# Define the sentence and skills
sentence = "We are looking for a skilled Python developer with experience in machine learning."
skills = ["Python", "machine learning"]

# Mask the skills in the sentence
masked_sentence = mask_skills(sentence, skills)

# Print the result
print(masked_sentence)