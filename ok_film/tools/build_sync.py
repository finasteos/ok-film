import json
import argparse
import os

def build_sync_list(manus_path, out_path):
    """
    Reads a timed manuscript and generates an FFmpeg concat file.
    Assumes one frame per line of dialogue.
    """
    with open(manus_path, 'r', encoding='utf-8') as f:
        manus = json.load(f)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, 'w', encoding='utf-8') as f:
        frame_count = 1
        for scene in manus.get('scenes', []):
            scene_id = scene.get('scene_id')
            for line in scene.get('lines', []):
                duration = line.get('duration', 2.5) # Default duration
                # This is a placeholder for frame logic.
                # It assumes a single frame per line of dialogue.
                # A more advanced version would generate multiple frames.
                frame_file = f"../frames/{scene_id}_{frame_count:04d}.png"
                f.write(f"file '{frame_file}'\n")
                f.write(f"duration {duration}\n")
                frame_count += 1
    print(f"✅ FFmpeg concat file written to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build FFmpeg concat file from timed manuscript.")
    parser.add_argument("--manus", default="scripts/our_manus_timed.json", help="Path to the timed manuscript JSON file.")
    parser.add_argument("--out", default="concat/S01_concat.txt", help="Path to the output concat text file.")
    args = parser.parse_args()
    build_sync_list(args.manus, args.out)