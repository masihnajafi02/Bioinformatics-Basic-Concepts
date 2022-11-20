def reverse(string):
    return string[::-1]


sequence = input()
reverse_compliment = ""
sequence = reverse(sequence)
for i in range(len(sequence)):
    if sequence[i] == 'A':
        reverse_compliment += 'T'
    elif sequence[i] == 'T':
        reverse_compliment += 'A'
    elif sequence[i] == 'G':
        reverse_compliment += 'C'
    else:
        reverse_compliment += 'G'

print(reverse_compliment)
