import re
text = "support@example.com"
emails = re.findall(r'\S+@\S+', text)
urls = re.findall(r'https?://\S+', text)
print("Emails:", emails)
print("URLs:", urls)
