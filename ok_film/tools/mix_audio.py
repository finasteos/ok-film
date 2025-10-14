import argparse
import glob
import os
from pydub import AudioSegment
from pydub.generators import Sine

def apply_kimi_effects(segment):
    """
    Applies pitch shifting and digital sparkles to Kimi's voice.
    """
    # Pitch shift down by 2 semitones (approx -200 cents)
    # A lower frame rate results in a lower pitch.
    new_sample_rate = int(segment.frame_rate * (2.0 ** (-2.0 / 12.0)))
    pitched_segment = segment._spawn(segment.raw_data, overrides={'frame_rate': new_sample_rate})
    pitched_segment = pitched_segment.set_frame_rate(segment.frame_rate)

    # Add digital sparkles (1kHz sine wave, very quiet)
    sparkle = Sine(1000).to_audio_segment(duration=len(pitched_segment), volume=-25)
    final_segment = pitched_segment.overlay(sparkle)

    return final_segment

def mix_audio_files(scene, inputs, out_path):
    """
    Mixes multiple audio files for a scene into a single file.
    Adds silence between clips and applies effects to Kimi's voice.
    """
    files = sorted(glob.glob(inputs))
    if not files:
        print(f"⚠️ No audio files found for scene {scene} matching '{inputs}'")
        return

    silence = AudioSegment.silent(duration=200) # 200ms silence
    mixed = AudioSegment.empty()

    for f in files:
        segment = AudioSegment.from_mp3(f)
        
        # Check if the character is KIMI to apply effects
        if "KIMI" in os.path.basename(f):
            segment = apply_kimi_effects(segment)
            
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