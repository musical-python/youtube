import music21

# Load MIDI file
midi_file = music21.converter.parse("grand_piano.mid")

# Change C4 to D4
for note in midi_file.flat.notes:
    if note.name == "C" and note.octave == 4:
        note.name = "D"

# make velocity increase gradually
length = len(midi_file.flat.notes)
for i, note in enumerate(midi_file.flat.notes):
    pass
    velocity = 1 + 120 * (i/length)
    note.volume.velocity = velocity

    # Write to MIDI file
midi_file.write("midi", "grand_piano_edit.mid")
