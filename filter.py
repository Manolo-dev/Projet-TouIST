import re

with open("output.txt", "r") as f:
    all_lines = f.read()

all_lines = re.sub(r"0 p\(\d,\d,\d,\w+\)\n", "", all_lines)
print(all_lines)
all_lines = re.findall(r"p\((\d),(\d),(\d),(\w+)\)", all_lines)
print(all_lines)
sorted_lines = sorted(all_lines, key=lambda x: (x[0], x[1], x[2]))
print(sorted_lines)

with open("output.txt", "w") as f:
    f.write("".join([f"1 p({x[0]},{x[1]},{x[2]},{x[3]})\n" for x in sorted_lines]))