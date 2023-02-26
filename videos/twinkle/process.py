import random

print('Reading input melody.')
with open('input_melody.txt') as f:
    input_text = f.read().strip()

input_melody = input_text.split(' ')


print('Generating Markov dictionary.')
markov_dict = dict()
for i in range(0, len(input_melody) - 1):
    current_note = input_melody[i]
    next_note = input_melody[i+1]
    if current_note in markov_dict.keys():
        markov_dict[current_note].append(next_note)
    else:
        markov_dict[current_note] = [next_note]

print('Writing out Markov dictionary.')
with open('markov_dict.txt', 'w') as f:
    f.write(str(markov_dict))


# print('Generating Markov chain melody.')
# random.seed(41)

# current_note = 'G'
# output_melody = []
# for _ in range(32):
#     output_melody.append(current_note)
#     current_note = random.choice(markov_dict[current_note])

# output_melody_text = ' '.join(output_melody)

# print('Writing out Markov chain melody.')
# with open('output_melody.txt', 'w') as f:
#     f.write(output_melody_text + '\n')
