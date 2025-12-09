import re

pattern = r"\d{3}-\d{3}-\d{4}"
text = "Call me at 123-456-7890 or 987-654-3210."
matches = re.findall(pattern, text)
print(matches) # ['123-456-7890', '987-654-3210']