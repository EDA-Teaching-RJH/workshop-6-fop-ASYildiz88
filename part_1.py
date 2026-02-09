# Task1.1: The Storage Bay
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

print(sample_bay[0])          # first item (index 0)
print(sample_bay[-1])         # last item (negative index)
print(len(sample_bay))        # total number of samples


# Task1.2: Analyzing SSamples (Iteration)
for sample in sample_bay:
    print(f"Transmitting data for : {sample}")


# Task1.3: Collection Duty (Appending)
new_findings = []

for _ in range(3):
    rock = input("Enter rock type: ")
    new_findings.append(rock)

print(new_findings)


# Task1.4: Jettisoning Waste (Extansion)

if "Dust" in sample_bay:
    sample_bay.remove("Dust")

print("FINAL sample_bay:", sample_bay)
