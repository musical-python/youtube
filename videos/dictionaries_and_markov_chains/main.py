import musicalbeeps
import random

random.seed(43)  # change me

player = musicalbeeps.Player(volume=0.3, mute_output=False)

markov_chain = {'A': ['A', 'G'], 'G': ['A']}  # maybe change me too?

note = 'A'

for _ in range(16):
    player.play_note(note, 0.5)
    note = random.choice(markov_chain[note])
