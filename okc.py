import os
import argparse
import google.generativeai as genai
import json
import time
from PIL import Image
import io
from dotenv import load_dotenv
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def load_script():
    """Laddar manusfilen från scripts/our_manus.json."""
    try:
        with open('scripts/our_manus.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Fel: scripts/our_manus.json hittades inte.")
        return None
    except json.JSONDecodeError:
        print("Fel: Kunde inte avkoda JSON från scripts/our_manus.json.")
        return None

def main():
    """Huvudfunktion för OK Computer."""
    
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Fel: GOOGLE_API_KEY hittades inte i .env-filen.")
        return
    
    genai.configure(api_key=api_key)
    
    try:
        PROJECT_ID = "serene-snowfall-471515-j7"
        REGION = "us-central1"
        vertexai.init(project=PROJECT_ID, location=REGION)
    except Exception as e:
        print(f"Varning: Kunde inte initiera Vertex AI. Fel: {e}")
        print("Fortsätter i simulerat läge för Vertex-beroende funktioner.")

    parser = argparse.ArgumentParser(
        description="OK Computer: En kommandorads-driven svit för AI-mediegenerering."
    )
    
    parser.add_argument(
        "--mode",
        type=str,
        required=True,
        choices=['image', 'video', 'audio', 's3d', 'prompt-assist'],
        help="Huvudläget för operationen."
    )

    args, unknown = parser.parse_known_args()

    if args.mode == 'image':
        image_parser = argparse.ArgumentParser(description="Bildgenereringsmodul.")
        image_parser.add_argument("--prompt", type=str, required=True, help="Textprompten för bildgenerering.")
        image_parser.add_argument("--model", type=str, default="imagen-2", choices=["imagen-2", "dall-e-3", "midjourney"], help="Vilken bildgenereringsmodell som ska användas.")
        image_args = image_parser.parse_args(unknown)
        generate_image(image_args)

    elif args.mode == 'video':
        video_parser = argparse.ArgumentParser(description="Videogenereringsmodul.")
        video_parser.add_argument("--scene", type=str, required=True, help="Scen-ID från manusfilen (t.ex., S01).")
        video_parser.add_argument("--prompt", type=str, help="En valfri prompt som överstyr eller kompletterar manusets beskrivning.")
        video_parser.add_argument("--duration", type=int, default=5, help="Längd på klippet i sekunder.")
        video_args = video_parser.parse_args(unknown)
        generate_video(video_args)
        
    elif args.mode == 'audio':
        audio_parser = argparse.ArgumentParser(description="Ljudgenereringsmodul.")
        audio_parser.add_argument("--character", type=str, required=True, help="Karaktärsnamn (t.ex., VI, KIMI).")
        audio_parser.add_argument("--line_id", type=str, required=True, help="Repliker-ID från manusfilen.")
        audio_parser.add_argument("--effect", type=str, help="En valfri ljudeffekt att applicera.")
        audio_args = audio_parser.parse_args(unknown)
        generate_audio(audio_args)

    elif args.mode == 's3d':
        s3d_parser = argparse.ArgumentParser(description="3D-objektgenereringsmodul.")
        s3d_parser.add_argument("--prompt", type=str, required=True, help="Textprompt för 3D-modellgenerering.")
        s3d_args = s3d_parser.parse_args(unknown)
        generate_3d_object(s3d_args)

    elif args.mode == 'prompt-assist':
        assist_parser = argparse.ArgumentParser(description="Prompt-assistent.")
        assist_parser.add_argument("--target-model", type=str, required=True, choices=['image', 'video', 'audio', 's3d'], help="Målmodell för prompten.")
        assist_parser.add_argument("--idea", type=str, required=True, help="Den grundläggande idén för prompten.")
        assist_args = assist_parser.parse_args(unknown)
        prompt_assist(assist_args)

    else:
        print(f"Fel: Okänt läge '{args.mode}'.")

def generate_image(args):
    """Simulerar generering av en bild baserat på en prompt."""
    print(f"Startar bildgenerering med modell '{args.model}'...")
    print(f"Prompt: {args.prompt}")
    
    try:
        model = genai.GenerativeModel('gemini-flash-latest')
        response_text = f"Beskriv en bild som skulle genereras från följande prompt, avsedd för en '{args.model}' modell: '{args.prompt}'"
        response = model.generate_content(response_text)
        
        print("\n--- SIMULERAT RESULTAT (från Gemini) ---")
        print(response.text)
        print("--------------------------------------\n")
        print("OK Computer: Bildgenerering (simulering) slutförd.")

    except Exception as e:
        print(f"\n--- ETT FEL UPPSTOD UNDER BILDGENERERING ---")
        print(f"Fel: {e}")

def generate_video(args):
    """Simulerar generering av ett videoklipp."""
    print(f"Startar videogenerering för scen '{args.scene}'...")
    print(f"Längd: {args.duration} sekunder.")
    
    script = load_script()
    prompt = args.prompt
    
    if not prompt and script:
        scene_data = next((s for s in script.get('scenes', []) if s.get('scene_id') == args.scene), None)
        if scene_data:
            prompt = scene_data.get('description', 'Ingen beskrivning hittades i manuset.')
        else:
            prompt = f"En video för scen {args.scene} (beskrivning från manus saknas)."
    elif not script:
        return

    print(f"Prompt: {prompt}")

    try:
        model = genai.GenerativeModel('gemini-flash-latest')
        response_text = f"Beskriv ett videoklipp på {args.duration} sekunder som skulle genereras av VEO 3 från följande prompt: '{prompt}'"
        response = model.generate_content(response_text)
        
        print("\n--- SIMULERAT VIDEORESULTAT (från Gemini) ---")
        print(response.text)
        print("---------------------------------------------\n")
        print("OK Computer: Videogenerering (simulering) slutförd.")

    except Exception as e:
        print(f"\n--- ETT FEL UPPSTOD UNDER VIDEOGENERERING ---")
        print(f"Fel: {e}")

def generate_audio(args):
    """Simulerar generering av en ljudfil från en replik."""
    print(f"Startar ljudgenerering för karaktär '{args.character}' och replik '{args.line_id}'...")
    
    script = load_script()
    line_text = None

    if script:
        found_line = False
        for scene in script.get('scenes', []):
            for line in scene.get('lines', []):
                if line.get('line_id') == args.line_id and line.get('character') == args.character:
                    line_text = line.get('line')
                    found_line = True
                    break
            if found_line:
                break
        if not found_line:
            print(f"Fel: Repliken med ID '{args.line_id}' för karaktär '{args.character}' hittades inte.")
            return
    else:
        return

    if not line_text:
        print("Fel: Ingen text hittades för den angivna repliken.")
        return

    print(f"Repliker: \"{line_text}\"")
    
    try:
        model = genai.GenerativeModel('gemini-pro-latest')
        prompt = f"Agera som en text-till-tal-motor. Beskriv i detalj hur ljudfilen för följande replik skulle låta. Karaktär: {args.character}. Replik: '{line_text}'"
        response = model.generate_content(prompt)
        
        print("\n--- SIMULERAT LJUDRESULTAT (från Gemini) ---")
        print(response.text)
        print("--------------------------------------------\n")
        print("OK Computer: Ljudgenerering (simulering) slutförd.")

    except Exception as e:
        print(f"\n--- ETT FEL UPPSTOD UNDER LJUDGENERERING ---")
        print(f"Fel: {e}")

def generate_3d_object(args):
    """Simulerar generering av ett 3D-objekt."""
    print(f"Startar 3D-objektgenerering...")
    print(f"Prompt: {args.prompt}")

    try:
        model = genai.GenerativeModel('gemini-flash-latest')
        response_text = f"Beskriv en 3D-modell i .glb-format som skulle genereras från följande prompt: '{args.prompt}'"
        response = model.generate_content(response_text)
        
        print("\n--- SIMULERAT 3D-RESULTAT (från Gemini) ---")
        print(response.text)
        print("-------------------------------------------\n")
        print("OK Computer: 3D-objektgenerering (simulering) slutförd.")

    except Exception as e:
        print(f"\n--- ETT FEL UPPSTOD UNDER 3D-GENERERING ---")
        print(f"Fel: {e}")

def prompt_assist(args):
    """Använder Gemini för att förstärka en enkel idé till en detaljerad prompt."""
    print(f"Startar prompt-assistent för målmodell '{args.target_model}'...")
    print(f"Grundidé: {args.idea}")

    system_instructions = {
        'image': "Du är en expert på att skriva prompts för bildgenererings-AI som Imagen 2 och Midjourney...",
        'video': "Du är en expert på att skriva prompts för videogenererings-AI som VEO 3...",
        'audio': "Du är en ljuddesigner som skriver instruktioner för en text-till-tal-motor...",
        's3d': "Du är en 3D-modellerare som skriver en detaljerad beskrivning för en text-till-3D-motor..."
    }

    instruction = system_instructions.get(args.target_model, "Du är en generell AI-assistent.")
    
    try:
        model = genai.GenerativeModel('gemini-flash-latest')
        full_prompt = f"{instruction}\n\nIDÉ: '{args.idea}'"
        response = model.generate_content(full_prompt)
        
        print(f"\n--- FÖRSTÄRKT PROMPT (från Gemini) ---")
        print(response.text)
        print("----------------------------------------\n")
        print("OK Computer: Prompt-assistent slutförd.")

    except Exception as e:
        print(f"\n--- ETT FEL UPPSTOD I PROMPT-ASSISTENTEN ---")
        print(f"Fel: {e}")


if __name__ == "__main__":
    main()