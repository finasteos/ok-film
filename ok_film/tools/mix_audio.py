import argparse
import glob
from pydub import AudioSegment

def mix_audio_files(scene, inputs, out_path):
    """
    Mixes multiple audio files for a scene into a single file.
    Adds a small amount of silence between clips.
    """
    # Find all audio files for the scene
    files = sorted(glob.glob(inputs))
    if not files:
        print(f"⚠️ No audio files found for scene {scene} matching '{inputs}'")
        return

    # Create a silent segment to add between clips
    silence = AudioSegment.silent(duration=200) # 200ms

    # Concatenate all audio files with silence in between
    mixed = AudioSegment.empty()
    for f in files:
        mixed += AudioSegment.from_mp3(f) + silence

    # Export the mixed audio
    mixed.export(out_path, format="mp3")
    print(f"✅ Mixed audio for scene {scene} saved to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mix audio files for a scene.")
    parser.add_argument("--scene", required=True, help="The scene ID to process (e.g., S01).")
    parser.add_argument("--inputs", required=True, help="Glob pattern for the input audio files (e.g., 'audio/S01_*.mp3').")
    parser.add_argument("--out", required=True, help="Path to the output mixed audio file.")
    args = parser.parse_args()
    mix_audio_files(args.scene, args.inputs, args.out)