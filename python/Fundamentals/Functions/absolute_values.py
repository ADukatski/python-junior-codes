sequence_of_numbers = input().split()
final_sequence = []

for n in sequence_of_numbers:
    number = float(n)
    final_sequence.append(abs(number))

print(final_sequence)


