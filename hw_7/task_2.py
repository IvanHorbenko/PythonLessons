def correct_sentence(text):
    first_letter_upper = text[0].upper()
    rest_of_text = text[1:]
    corrected_text = first_letter_upper + rest_of_text
    if not corrected_text.endswith('.'):
        corrected_text += '.'
    return corrected_text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')