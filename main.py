import pickle
import serial
import synth, chord_classifier

def parse_strum(ser):
    pass

if __name__ == '__main__':
    ports = glob.glob('/dev/ttyUSB[0-9]*')
    if len(ports) == 0:
        print("Device not connected")

    ser = serial.Serial(port=ports[0], baudrate=115200, timeout=1)
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
