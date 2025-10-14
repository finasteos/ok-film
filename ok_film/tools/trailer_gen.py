import argparse
import json
import os

def generate_trailer(manus_path, out_path):
    """
    Analyzes the manuscript to find high-impact lines and generates a placeholder trailer.
    """
    with open(manus_path, 'r', encoding='utf-8') as f:
        manus = json.load(f)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    high_impact_lines = []
    for scene in manus.get('scenes', []):
        for line in scene.get('lines', []):
            text = line.get('line', '')
            if any(c in text for c in '?!') or text.isupper():
                high_impact_lines.append(line)

    # Placeholder: Create a text file describing the trailer
    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write("OK Film - Auto-Generated Trailer\n")
        f_out.write("="*30 + "\n")
        f_out.write(f"Found {len(high_impact_lines)} high-impact lines.\n")
        f_out.write("Trailer would be a fast-paced cut of the following:\n\n")
        for line in high_impact_lines:
            f_out.write(f"- {line['character']}: {line['line']}\n")
        f_out.write("\n(This is a placeholder for the final trailer video)\n")

    print(f"✅ Generated placeholder trailer script at {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a trailer from high-impact manuscript lines.")
    parser.add_argument("--manus", default="scripts/our_manus.json", help="Path to the manuscript JSON file.")
    parser.add_argument("--out", default="releases/OK_Film_Trailer.txt", help="Path to save the trailer.")
    args = parser.parse_args()
    generate_trailer(args.manus, args.out)