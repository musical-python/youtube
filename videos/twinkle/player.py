import musicalbeeps

print('Initializing player object.')
player = musicalbeeps.Player(volume=0.3, mute_output=False)

print('Reading in output melody.')
with open('output_melody.txt') as f:
    output_melody_text = f.read().strip()

output_melody = output_melody_text.split(' ')

print('Playing meolody.')
for note in output_melody:
    player.play_note(note, 0.4)
