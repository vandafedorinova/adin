import re

text = "Hello, world! This is a test string."
punct = r'[^\w\s]'
result = re.sub(punct, '', text)

print(result)
