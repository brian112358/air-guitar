import itertools
import math
import subprocess
import time

bpm = 110

chords = {
    'Am': ['E2', 'A2', 'E3', 'A3', 'C4', 'E4'],
    'G':  ['G2', 'B2', 'D3', 'G3', 'B3', 'G4'],
    'Em': ['E2', 'B2', 'E3', 'G3', 'B3', 'E4'],
    'F':  ['F2', 'C3', 'F3', 'A3', 'C4', 'F4']
}

chords_capo = {
    'Am': ['G2', 'C2', 'G3', 'C4', 'D#4', 'G4'],
    'G':  ['A#2', 'D3', 'F3', 'A#3', 'D4', 'A#4'],
    'Em': ['G2', 'D3', 'G3', 'A#3', 'D4', 'G4'],
    'F':  ['G#2', 'D#3', 'G#3', 'C4', 'D#4', 'G#4']
}

def chord(name, octave=0, capo=False):
    notes = (chords_capo if capo else chords)[name]
    notes = [n[:-1] + str(int(n[-1])+octave) for n in notes]
    return notes

def play_chord_async(notes, sustain=1, delay=0.03, order=1):
    cmd = ['play', '-n', 'synth', str(sustain*60./bpm)]
    cmd += list(itertools.chain(*zip(['pl'] * len(notes), notes[::order])))
    cmd += ['delay']
    cmd += [str(delay * i) for i in range(len(notes))]
    cmd += ['remix -', 'fade 0 %.3f 0.1' % (sustain*60./bpm), 'norm -1']
    cmd += ['> /dev/null 2>&1']
    cmd = ' '.join(cmd)
    subprocess.Popen(cmd, shell=True)

def play_chord(notes, duration=1, sustain=None, delay=0.03, order=1):
    if not sustain:
        sustain = duration + 0.5
    play_chord_async(notes, sustain, delay, order)
    time.sleep(duration*60./bpm)

if __name__ == '__main__':
    play_chord(chords_capo['Am'], 2)
    play_chord(chords_capo['Am'], 1)
    play_chord(chords_capo['G'],  1, order=-1)
    play_chord(chords_capo['Am'], 2)
