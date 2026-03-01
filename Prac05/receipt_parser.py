import re
import json

#1
pattern1 = r"^ab*$"
test1 = "abbb"
print("1:", bool(re.match(pattern1, test1)))

#2
pattern2 = r"^ab{2,3}$"
test2 = "abb"
print("2:", bool(re.match(pattern2, test2)))

#3
pattern3 = r"\b[a-z]+_[a-z]+\b"
test3 = "snake_case example_test wrongCase"
print("3:", re.findall(pattern3, test3))

#4
pattern4 = r"\b[A-Z][a-z]+\b"
test4 = "Hello world My Name Is Python"
print("4:", re.findall(pattern4, test4))

#5
pattern5 = r"^a.*b$"
test5 = "axxxb"
print("5:", bool(re.match(pattern5, test5)))

#6
test6 = "Hello, world. This is a test"
result6 = re.sub(r"[ ,\.]", ":", test6)
print("6:", result6)

#7
def snake_to_camel(text):
    parts = text.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

print("7:", snake_to_camel("snake_case_string"))

#8
def split_at_uppercase(text):
    return re.findall(r"[A-Z][^A-Z]*", text)

print("8:", split_at_uppercase("SplitThisStringAtUppercase"))

#9
def insert_spaces(text):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", text)

print("9:", insert_spaces("InsertSpacesBetweenWords"))

#10
def camel_to_snake(text):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()

print("10:", camel_to_snake("CamelCaseString"))

#Receipt Parsing
with open("raw.txt", "r", encoding="utf-8") as file:
    receipt_text = file.read()

#Extract prices
prices = re.findall(r"\d+\s?\d*,\d{2}", receipt_text)

#Find product names
products = re.findall(r"\d+\.\n(.+)", receipt_text)

#Calculate total
clean_prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices]
calculated_total = sum(clean_prices)

#Extract date and time
datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", receipt_text)
datetime_value = datetime_match.group() if datetime_match else None

#Find payment method
payment_match = re.search(r"(Банковская карта|Наличные)", receipt_text)
payment_method = payment_match.group() if payment_match else None

structured_output = {
    "products": products,
    "prices": prices,
    "calculated_total": calculated_total,
    "date_time": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(structured_output, ensure_ascii=False, indent=4))