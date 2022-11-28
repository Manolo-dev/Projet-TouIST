import re

with open("output.txt", "r") as f:
    all_lines = f.read()

all_lines = re.sub(r"0 \w+\(.+\)\n", "", all_lines)
print(all_lines)
all_lines = re.findall(r"(\w+)\((.+)\)", all_lines)
print(all_lines)
sorted_lines = sorted(all_lines, key=lambda x: (x[1], x[0]))
print(sorted_lines)

with open("output.txt", "w") as f:
    f.write("".join([f"1 {x[0]}({x[1]})\n" for x in sorted_lines]))