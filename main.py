import pickle
import serial
import synth, chord_classifier

def parse_strum(ser):
    line = ser.readline().replace("\r\n", "")
    print(line)
    words = line.split(',')
    dist, direction = words[0], words[1]
    flex = map(int, words[2:])
    return dist, direction, flex

if __name__ == '__main__':
    ser = serial.serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
    print('Connected to ' + ser.name)

    # Load classifier
    clf = pickle.load(open('chord_classifier.pkl'))
    print('Loaded chord classifier')

    while True:
        dist, direction, flex = parse_strum(ser)
        print(dist)
        flex = np.reshape(flex, (-1,1))
        chord = chord_classifier.chords[clf.predict(flex)[0]]
        octave = np.clip((dist - 30) // 10, -2, 2)

        chord = synth.chord(chord, octave, True)

        play_chord_async(chord, 2, direction)
