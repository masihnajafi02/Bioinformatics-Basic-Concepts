seq_dict = {}
temp_key = ''
gc_content = {}
while True:
    user_input = input()
    if "Rosalind" in user_input:
        seq = ''
        seq_dict[user_input] = ''
        temp_key = user_input
    elif user_input == "end":
        break
    else:
        seq_dict[temp_key] = seq_dict[temp_key] + user_input

for k, v in seq_dict.items():
    seq_dict[k] = (v.count("G") + v.count("C")) / len(v)

key = max(seq_dict, key=seq_dict.get)
print(key[1:])
print(seq_dict[key]*100)
