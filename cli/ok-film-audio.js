#!/usr/bin/env node
// cli/ok-film-audio.js
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import dotenv from "dotenv";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: path.resolve(__dirname, "..", ".env") });
const root    = path.resolve(__dirname, "..");
const manus   = JSON.parse(fs.readFileSync(path.join(root, "scripts", "our_manus.json"), "utf-8"));
const outDir  = path.join(root, "audio");

if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

const GOOGLE_CLOUD_API_KEY = process.env.GOOGLE_CLOUD_API_KEY;
if (!GOOGLE_CLOUD_API_KEY) {
  console.error("❗ Set GOOGLE_CLOUD_API_KEY in .env");
  process.exit(1);
}

// ---------- TTS helper ----------
async function synthesize(text, voice, fileName) {
  const url = `https://texttospeech.googleapis.com/v1/text:synthesize?key=${GOOGLE_CLOUD_API_KEY}`;
  const body = {
    input: { text },
    voice: { languageCode: "sv-SE", name: voice },
    audioConfig: { audioEncoding: "MP3", speakingRate: 1.0, pitch: 0 }
  };
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  if (!res.ok) throw new Error(await res.text());
  const { audioContent } = await res.json();
  const out = path.join(outDir, fileName);
  fs.writeFileSync(out, Buffer.from(audioContent, "base64"));
  console.log(`✅ ${fileName}`);
}

// ---------- Voice mapping ----------
const voiceMap = {
  VI:   "sv-SE-Wavenet-C",   // neutral, klar (Female)
  KIMI: "sv-SE-Wavenet-D"    // lite mörkare, glitchig (Male)
};

// ---------- Main ----------
for (const scene of manus.scenes) {
  for (const l of scene.lines) {
    const voice = voiceMap[l.character];
    if (!voice) continue;
    const file = `${scene.scene_id}_${l.character}_${l.line_id}.mp3`;
    await synthesize(l.line, voice, file);
  }
}
console.log("🎬 Alla röstspår klara – redo för sync!");