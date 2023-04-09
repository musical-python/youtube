import random
import music21
import musicalbeeps

RANDOM_SEED = 27
STARING_POINT = 4
CHOICES_A = [-1, -1, 0]
CHOICES_B = [-1, -1, 0, 1, 1]
CHOICES_C = [-2, -1, 1, 2, 3]
META_CHOICES = [CHOICES_A, CHOICES_B, CHOICES_C]


def main():
    player = musicalbeeps.Player(volume=0.3,
                                 mute_output=False)
    choices = CHOICES_A
    current_point = STARING_POINT
    random.seed(RANDOM_SEED)
    # print('starting point:', current_point)
    points = [current_point]
    for i in range(8*8*3):
        if i % 8 == 0:
            choices = random.choice(META_CHOICES)
        current_point += random.choice(choices)
        # print(current_point)
        points.append(current_point)
    print(points)

    scale = music21.scale.DorianScale('d')
    pitches = list(str(p) for p in scale.pitches)
    points = [point % len(pitches) for point in points]
    print(points)
    melody_pitches = [pitches[point] for point in points]
    print(melody_pitches)
    for melody_pitch in melody_pitches:
        player.play_note(melody_pitch, 0.6)


if __name__ == '__main__':
    main()
