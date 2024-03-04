# Beat tracking example
import librosa

# 1. Get the file path to an included audio example
filename_0 = 'data/file_0.wav'
filename_1 = 'data/file_1.wav'


def estimate(fn):
    # 2. Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`
    y, sr = librosa.load(fn)

    # 3. Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

    # 4. Convert the frame indices of beat events into timestamps
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    print(f'Beat_times: {beat_times}')


if __name__ == '__main__':
    estimate(filename_0)
    estimate(filename_1)