from string import ascii_lowercase

groups = open('input.txt').read().split('\n\n')
groups = [group.split('\n') for group in groups]
merged_groups = ["".join(group) for group in groups]

unique_groups = []
for group in merged_groups:
    unique_chars = set()
    for char in group:
        unique_chars.add(char)
    unique_groups.append(unique_chars)
sum = [sum([len(group) for group in unique_groups])]
print(sum[0])

# supposed to be Part 2 > 3428
sum_of_same_yes = 0
for group in groups:
    for c in ascii_lowercase:
        if all(c in person for person in group):
            sum_of_same_yes += 1

print(sum_of_same_yes)

