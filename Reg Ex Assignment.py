#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
text = 'Python Exercises, PHP exercises'
x = (re.sub("[.,]", ":", text))
print(x)


# In[2]:


import pandas as pd
import re

data = {'SUMMARY': ['hello world', 'test', 'four five six']}
df = pd.DataFrame(data)
df['SUMMARY'] = df['SUMMARY'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
print(pd.DataFrame(data))


# In[3]:


import re

def find_words_at_least_4_chars(input_string):
    pattern = re.compile(r'\b\w{4,}\b')
    words = pattern.findall(input_string)
    return words


# In[44]:


import re

def find_words_of_length(input_string):
    # Compile a regular expression pattern to match words of lengths 3, 4, and 5 characters
    pattern = re.compile(r'\b\w{3,5}\b')

    # Use the findall method to extract all matching words from the input string
    words = pattern.findall(input_string)

    return words


# In[45]:


import re

def find_words_of_length(input_string):
    pattern = re.compile(r'\b\w{3,5}\b')
    words = pattern.findall(input_string)
    return words
    


# In[46]:


import re

def remove_parentheses(strings):
    
    pattern = re.compile(r'\([^)]*\)')
    cleaned_strings = [re.sub(pattern, '', string) for string in strings]
    return cleaned_strings



# In[47]:


import re

text = "ImportanceOfRegularExpessionsInPython"
result = re.split(r'([A-Z][a-z]*)', text)[1:-1]
output = [result[i] + result[i + 1] for i in range(0, len(result), 2) if result[i] and result[i + 1]]
print(output)


# In[48]:


import re

def insert_spaces_between_numbers_and_words(text):
    modified_text = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)
    return modified_text



# In[15]:


import re

def insert_spaces(text):
    modified_text = re.sub(r'([A-Z0-9][a-z0-9]*)', r' \1', text)
    return modified_text.strip()  # Remove leading space if any



# In[16]:


import pandas as pd

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)
df['first_five_letters'] = df['Country'].str[:6]
print(df[['Country', 'first_five_letters']])


# In[50]:


import re

def is_valid_string(input_string):
    pattern = re.compile(r'^[A-Za-z0-9_]+$')
    if pattern.match(input_string):
        return True
    else:
        return False




# In[51]:


def starts_with_number(string, number):
    return string.startswith(str(number))




# In[52]:


def remove_leading_zeros(ip_address):
    parts = ip_address.split(".")
    parts_without_zeros = [str(int(part)) for part in parts]
    cleaned_ip = ".".join(parts_without_zeros)
    return cleaned_ip



# In[53]:


import re

with open('sample.txt', 'r') as file:
    text = file.read()
pattern = r'(?P<date>(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4})'
matches = re.findall(pattern, text)
for match in matches:
    print(match)



# In[25]:


def search_literals(text, searched_words):
    found_words = []
    for word in searched_words:
        if word in text:
            found_words.append(word)
    return found_words

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

found_words = search_literals(sample_text, searched_words)

print("Found words:", found_words)


# In[27]:


def find_word_location(text, word):
    locations = []
    start = -1
    while True:
        start = text.find(word, start + 1)
        if start == -1:
            break
        locations.append(start)
    return locations

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

locations = find_word_location(sample_text, searched_word)

if locations:
    print(f"The word '{searched_word}' was found at positions:", locations)
else:
    print(f"The word '{searched_word}' was not found in the text.")



# In[28]:


import re

def find_substrings(text, pattern):
    substrings = re.findall(pattern, text)
    return substrings

sample_text = 'Python exercises, PHP exercises, C# exercises'
search_pattern = 'exercises'

substrings = find_substrings(sample_text, search_pattern)

if substrings:
    print("Substrings found:", substrings)
else:
    print("No substrings found.")


# In[29]:


import re

def find_substring_occurrences(text, substring):
    occurrences = []
    for match in re.finditer(substring, text):
        start = match.start()
        end = match.end()
        occurrences.append((substring, start, end))
    return occurrences

sample_text = 'Python exercises, PHP exercises, C# exercises, more Python exercises'
search_substring = 'exercises'

substring_occurrences = find_substring_occurrences(sample_text, search_substring)

if substring_occurrences:
    print("Occurrences of the substring:")
    for substring, start, end in substring_occurrences:
        print(f"Substring '{substring}' found at position {start}-{end}")
else:
    print("No occurrences found.")


# In[55]:


from datetime import datetime

def convert_date_format(input_date):
    try:
        date_object = datetime.strptime(input_date, '%Y-%m-%d')
        formatted_date = date_object.strftime('%d-%m-%Y')
        return formatted_date
    except ValueError:
        return "Invalid date format. Please use yyyy-mm-dd."



# In[56]:


import re

def find_decimal_numbers(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    decimal_numbers = pattern.findall(text)
    return decimal_numbers



# In[57]:


import re

def find_numbers_with_positions(text):
    pattern = re.compile(r'\d+')
    number_matches = pattern.finditer(text)

    for match in number_matches:
        number = match.group()  # Get the matched number
        start = match.start()  # Get the start position of the number
        end = match.end()      # Get the end position of the number
        print(f"Number: {number}, Position: {start}-{end}")



# In[33]:


import re

def extract_max_numeric_value(text):
    pattern = re.compile(r'\d+')
    numeric_values = pattern.findall(text)
    max_numeric_value = max(map(int, numeric_values))
    return max_numeric_value




# In[34]:


import re

def insert_spaces_before_capitals(text):
   
    modified_text = re.sub(r'([A-Z][a-z]*)', r' \1', text).strip()
    return modified_text


sample_text = "RegularExpressionIsAnImportantTopicInPython"
result = insert_spaces_before_capitals(sample_text)
print(result)


# In[35]:


import re

text = "This is a Sample Text With Some Uppercase Words and More."

pattern = re.compile(r'[A-Z][a-z]+')

matches = pattern.findall(text)

for match in matches:
    print(match)


# In[58]:


import re

def remove_continuous_duplicates(text):
    
    pattern = r'\b(\w+)\s+\1\b'
    modified_text = re.sub(pattern, r'\1', text)
    return modified_text




# In[59]:


import re

def is_ending_with_alphanumeric(input_string):
    pattern = re.compile(r'.*\w$')
    if pattern.search(input_string):
        return True
    else:
        return False



# In[60]:


import re

def extract_hashtags(text):
    pattern = re.compile(r'#\w+')
    hashtags = pattern.findall(text)
    return hashtags



# In[61]:


import re

def remove_unicode_symbols(text):
    pattern = re.compile(r'<U\+[0-9A-Fa-f]+>')
    cleaned_text = pattern.sub('', text)
    return cleaned_text



# In[62]:


import re

def extract_dates_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    date_pattern = r'\d{2}-\d{2}-\d{4}'
    dates = re.findall(date_pattern, text)
    return dates




# In[63]:


import re

def extract_dates_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    date_pattern = r'\d{2}-\d{2}-\d{4}'
    dates = re.findall(date_pattern, text)
    return dates



# In[ ]:





# In[ ]:




