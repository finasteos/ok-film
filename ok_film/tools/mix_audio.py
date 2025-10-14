import argparse
import glob
import os
from pydub import AudioSegment
from pydub.generators import Sine

def apply_audio_effects(segment, character):
    """
    Applies character-specific audio effects.
    """
    effects = {
        "KIMI": {
            "pitch_semitones": -3,
            "sparkle_freq": 1000,
            "sparkle_volume": -25
        },
        "VI": {
            "pitch_semitones": +2,
            "sparkle_freq": 1200,
            "sparkle_volume": -30
        }
    }

    if character not in effects:
        return segment

    fx = effects[character]

    # Pitch shift
    new_sample_rate = int(segment.frame_rate * (2.0 ** (fx["pitch_semitones"] / 12.0)))
    pitched_segment = segment._spawn(segment.raw_data, overrides={'frame_rate': new_sample_rate})
    pitched_segment = pitched_segment.set_frame_rate(segment.frame_rate)

    # Add digital sparkles
    sparkle = Sine(fx["sparkle_freq"]).to_audio_segment(duration=len(pitched_segment), volume=fx["sparkle_volume"])
    final_segment = pitched_segment.overlay(sparkle)

    return final_segment

def mix_audio_files(scene, inputs, out_path):
    """
    Mixes multiple audio files for a scene into a single file.
    Adds silence between clips and applies character-specific effects.
    """
    files = sorted(glob.glob(inputs))
    if not files:
        print(f"⚠️ No audio files found for scene {scene} matching '{inputs}'")
        return

    silence = AudioSegment.silent(duration=200) # 200ms silence
    mixed = AudioSegment.empty()

    for f in files:
        segment = AudioSegment.from_mp3(f)
        
        # Determine character from filename
        basename = os.path.basename(f)
        character = None
        if "KIMI" in basename:
            character = "KIMI"
        elif "VI" in basename:
            character = "VI"
            
        if character:
            segment = apply_audio_effects(segment, character)
            
        mixed += segment + silence

    mixed.export(out_path, format="mp3")
    print(f"✅ Mixed and processed audio for scene {scene} saved to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mix audio files for a scene.")
    parser.add_argument("--scene", required=True, help="The scene ID to process (e.g., S01).")
    parser.add_argument("--inputs", required=True, help="Glob pattern for the input audio files (e.g., 'audio/S01_*.mp3').")
    parser.add_argument("--out", required=True, help="Path to the output mixed audio file.")
    args = parser.parse_args()
    mix_audio_files(args.scene, args.inputs, args.out)