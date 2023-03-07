import numpy as np
import musicalbeeps
import music21


def main():
    player = musicalbeeps.Player(volume=0.3, mute_output=False)

    duration = 9
    period = 1.5
    note_frequency = 12
    scale = 'whole_tone'
    starting_height = 55
    floor_height = 90

    time = np.linspace(period/2, duration + period /
                       2, duration*note_frequency)

    pitches = (starting_height - floor_height) * \
        (1 - (((time % period) - period/2)**2 / (period/2)**2)) + floor_height

    for pitch in pitches:
        scale_pitch = apply_scale(pitch, scale)
        note = music21.note.Note()
        note.pitch.midi = scale_pitch
        name = note.nameWithOctave
        if len(name) == 3:
            name = name[0] + name[2] + name[1]
        name = name.replace('-', '')

        player.play_note(name, 1/note_frequency)


def apply_scale(pitch, scale):
    if scale is None:
        return pitch
    elif scale == 'whole_tone':
        return round(pitch/2) * 2
    elif scale == 'chromatic':
        return round(pitch)


if __name__ == '__main__':
    main()
