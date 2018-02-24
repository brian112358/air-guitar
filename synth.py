# import glob
import itertools
# import serial
import subprocess
import time

chords = {
    'Am': ['E2', 'A2', 'E3', 'A3', 'C4', 'E4'],
    'G':  ['G2', 'B2', 'D3', 'G3', 'B3', 'G4'],
    'Em': ['E2', 'B2', 'E3', 'G3', 'B3', 'E4'],
    'F':  ['E2', 'A2', 'F3', 'A3', 'C4', 'F4']
}

chords_capo = {
    'Am': ['G2', 'C2', 'G3', 'C4', 'D#4', 'G4'],
    'G':  ['A#2', 'D3', 'F3', 'A#3', 'D4', 'A#4'],
    'Em': ['G2', 'D3', 'G3', 'A#3', 'D4', 'G4'],
    'F':  ['G2', 'C3', 'G#3', 'C4', 'D#4', 'G#4']
}

def gen_chord(name):
    pass

def play_chord(notes, duration=1, delay=0.05):
    cmd = ['play', '-n', 'synth']
    cmd += list(itertools.chain(*zip(['pl'] * len(notes), notes)))
    cmd += ['delay']
    cmd += [str(delay * i) for i in range(len(notes))]
    cmd += ['remix -', 'fade 0 %f .1' % duration, 'norm -1']
    cmd += ['> /dev/null 2>&1']
    cmd = ' '.join(cmd)
    subprocess.Popen(cmd, shell=True
)

if __name__ == '__main__':
    # play_chord(['G2', 'B2', 'D3', 'G3', 'D4', 'G4'])
    play_chord(chords_capo['Am'], 2)
    time.sleep(1)
    play_chord(chords_capo['Am'])
    time.sleep(.5)
    play_chord(chords_capo['G'])
    time.sleep(.5)
    play_chord(chords_capo['Am'], 2)
    time.sleep(2)

