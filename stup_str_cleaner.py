```
Stupdendous String Cleaner

made by Luke Holcombe.
```

# First attempt, only clears 1 specified deliniator

raw_string = input("Give me a string - use only -\n")

def stripper(raw_string):
    string_clip = raw_string.split('-')
    clean_string = ''
    for i in range(len(string_clip)):
        clean_string += string_clip[i].capitalize()
    return clean_string

stripper(raw_string)

# Second attempt, removes del dyanmically (can be set once off).

def string_cleaner():
    chars_to_remove = [',','-']
    raw_string = input('Give me a string with , or - as separators: \n')

    for char in chars_to_remove:
        raw_string = raw_string.replace(char, '-')

    clean_string = raw_string.split('-')
    result = ''

    for i in range(len(clean_string)):
        result += clean_string[i].capitalize()

    return result

string_cleaner()

# Third attempt - runs a basic test suite, adds interactivity in the shell.

def string_cleaner(raw_string):
    chars_to_remove = [',','-','|','_']

    for char in chars_to_remove:
        raw_string = raw_string.replace(char, '-')

    clean_string = raw_string.split('-')
    result = ''

    for i in range(len(clean_string)):
        result += clean_string[i].capitalize()

    return result

# string_cleaner()
print('Welcome to Luke\'s stupenduos String Stripper!!!\n')
print('First test case loading.....\n')

print('this-uses_multiple|separators')
print(string_cleaner('this-uses_multiple|separators'))

# Fourth Attempt: adds basic testing, but can be expanded in the future.
# Stumped if deliniator is nothing or non-char

def string_cleaner(raw_string):
    chars_to_remove = [',','-','|','_']
    
    for char in chars_to_remove:
        raw_string = raw_string.replace(char, '-')
    
    clean_string = raw_string.split('-')
    result = ''

    for i in range(len(clean_string)):
        result += clean_string[i].capitalize()

    return result

def user_intro():
    import time 
    
    print('Welcome to Luke\'s stupenduos String Stripper!!!\n')
    print('First test case loading.....\n')
    time.sleep(1)

    test_cases = ['this,one-has-allsorts|of_separators','this,ONE-has-some-letters|CAPITALISED']

    for i in test_cases:
        print('Case: \n')
        print(string_cleaner(i))
    return

user_intro()
