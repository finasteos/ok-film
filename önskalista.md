# Manifest för "OK Film" – den fullständiga önskelistan

## 1. Grundläggande existensberättigande
- 100 % öppen källkod (OSI-godkänd licens) – går att kompilera från source utan blobbar
- Plattformsagnostik: Linux, macOS, Windows, Web (WASM), Docker, Flatpak, AppImage, Homebrew
- Offline-first – fungerar bakom luftgap; online-läge endast för API-nycklar
- PWA + Tauri-wrapper → "installera" som desktop-app, mobil-tablet-läge för rough-cut på resan
- UI i två skepnader: "Pro-Dark" (Nuke-lik) och "Creator-Light" (Final-Cut-lik) – växla med ett klick
- Fullständig svensk översättning (inklusive alla menykommandon, verktygstips, felmeddelanden)

## 2. Ingest & import – alla format som någonsin funnits
- 8K R3D, 6K ARRI, Blackmagic BRAW, Canon RAW, Sony RAW / X-OCN
- ProRes varianter (Proxy → XQ), DNxHR, DNxHD, CineForm, H.264/5, AV1, VP9, WebM, GIF
- Bildsekvenser: EXR 32-bit float, DPX, TIFF, PNG, JPG, HEIF/HEIC, PSD med lager
- HDR: PQ (ST-2084), HLG, HDR10+, Dolby Vision XML
- VR/360: equirectangular 8K 60 fps, side-by-side, over-under
- 3D-kamera: stereoscopic EXR med disparity-kanal
- Ljud: WAV, BWF, AIFF, FLAC, OGG, MP3, AAC, AC-3, Dolby Atmos ADM, Ambisonic (1-3 ordningen)
- Undertext: SRT, VTT, TTML, STL, EBU-TT-D, Netflix IMF Timed-Text
- Stills & vektorer: SVG, PDF, AI, EPS → automatisk rasterisering vid önskad upplösning

## 3. AI-generering inbyggd
- Text-to-video: Veo-2, Kling 1.5, Runway Gen-3, Pika 1.5, Stable-Video-Diffusion, Mochi-1, HunyuanVideo, WAN-2.1, Open-Sora 2.0
- Image-to-video: alla ovan + personaliserade LoRA/Checkpoint
- Consistent-character motor – spara face-set, kläd-set, props; håll karaktär över scener
- Camera-control: dolly, crane, drone, handheld, roll, pan, orbit via Blender-style kameraobjekt
- Frame-interpolation: RIFE, FILM, XVFI – valfri target fps upp till 120 fps
- Slow-motion: 1000 fps super-slow med fysikbaserad blending
- Inpainting & outpainting på videokanaler (mask följer rörelse)
- Upscaling: Real-ESRGAN, Real-HAT, SwinIR, Imagen-3-ultra, Topaz Video-AI-modeller (om användaren har licens)
- Downscaling med AI-baserad anti-alias (för social-media export)
- Modell-manager: dra-och-släpp safetensors/ONNX direkt i appen → automatisk installation i Comfy-miljö
- Prompt-bibliotek: gemensamt repo, taggbart, inbäddad CC-search för referensbilder

## 4. Redigering – klassisk + AI-assist
- Full icke-linjär tidslinje med obegränsade videokanaler, obegränsade ljudkanaler
- Track-färg, track-grupper, nästlade sekvenser (After-Effects-style pre-comp)
- Blade, roll, slip, slide, ripple, trim-fönster med JKL-shuttle
- Multicam-sync via ljudvågform, timecode eller in/out-punkter – upp till 64 kameror
- Proxy-redigering: auto-generera ¼-res ProRes-proxy, växla med ett klick
- AI-rough-cut: mata in råmaterial + manus → får föreslagen klippföljd baserad på dialog
- AI-b-roll-sökare: läser manus, letar matchande CC0-film och lägger på tidslinjen
- Auto-sync extern ljud (plural-eyes-algoritm) med sub-frame-noggrannhet
- Kommentarspår (Frame.io-lik) – integrerad med Blender Cloud, Kitsu, ftrack, ShotGrid
- Versionshantering: Git-LFS-backend, visuell diff mellan klipp-versioner
- Oändligt ångra (persistent disk-cache), spara snapshots med miniatyrer

## 5. Transitioner & effekter
- AI-morph-transition: generera semantiska mellanbilder mellan två shots (egen modell)
- Match-cut-detektor: hittar automatiskt ramar där komposition/kameravinkel matchar
- 3D-DVE (position, rotation, skala) med motion-blur, vektor-baserad istället för raster
- Speed-ramp Bezier-kurvor, omedelbar optical-flow-baserad tid-stretch
- Chromatic-aberration, lens-distortion, barrel, anamorfic-flare med bild-följande ljuspunkter
- Partikel-system (OpenCL-accelererat): dimma, regn, snö, glitter, fyrverkeri
- AI-genererade overlays: film-repor, damm, kodak-fade, VHS-tracking
- LUT-manager: previz på miniatyr, drag-and-drop .cube, .3dl, .look
- Real-time scopes: waveform, RGB-parade, vectorscope, histogram, CIE-xy chromaticity
- HDR-tonemapping-preview för SDR-monitor, med HDR-simuleringsfönster

## 6. Färg & mastering
- Full ACES 2.0-pipeline (IDT, RRT, ODT) – valfri ACES-version
- HDR-grade: 1000-nit, 4000-nit, 10 000-nit mastering-nit-nivåer
- Dolby Vision: generera mezzanine + XML, analyse-export för Dolby CM
- Color-matching med ett klick: AI läser färgspektrum i ref-bild, applicerar på hela sekvens
- Grain-management: AI-denoise + syntetisk grain (Kodak 2383, Fuji F-CP)
- CDL (Color Decision List) import/export, EDL med färgmetadat
- Network-grade: Netflix, Amazon, BBC, iTunes-delivery-mallar färdiga
- Ljud-mastering: loudness-normalisering EBU R-128, ATSC A/85, Netflix Loudness -27 LKFS
- True Peak-limiter, 5.1 → stereo downmix-matrix, Dolby Atmos 9.1.6 stöd
- Batch-master: droppa 100 timelines → vakna till färdiga mezzanine-filer

## 7. Ljud – djupt
- AI-dubbning & voice-cloning: Chirp-2, XTTS-2, OpenVoice, ElevenLabs, Kokoro-82M
- Automatisk språk-ID på käll-ljud, föreslå röstbank med matchande accent/ålder
- Lip-sync: Wav2Lip, Video-Retalk, SynTalk, Viseme-analys med 60 fps-trackning
- ADR-spår: inspelning med live video-overlay, loop-record, pre-roll count-down
- Ljud-restaurering: AI-brush, brus-reducering, klick/pop-borttagning, hum-borttagning 50/60 Hz
- Ambience-match: AI extraherar room-tone, förlänger automatiskt till önskad längd
- Foley-generator: skriv "high heels on concrete" → får AI-genererat ljud som matchar steg
- Musik-stem-split (vokal/drums/bas/annat) för enkel dialog-underdubb
- Surround-panner 3D: objekt-baserat, export till ADM BWF
- MIDI-spår: koppla VST-instrument, skriv noter direkt på tidslinjen

## 8. Text, grafik & motion
- AI-title-generator: stilord → får 10 förslag på typo + animation
- Vector-text med variable-fonts, emoji-color-fonts, right-to-left-layouter
- Subtitle-burn med AI-baserad rad-brytning (språkmedveten)
- Lower-thirds, roll-credits, crawl, bumpers – färdiga mallar
- SVG-import bevarar vektor, kan animeras med keyframes
- 3D-text med PBR-material, reflektioner, miljö-map
- Live-data-overlay: CSV, JSON, Google Sheet → uppdateras vid export
- QR-kod-generator direkt i appen, med färg- och logotyp-anpassning
- GIF-meme-export, med optimerad palett och dither

## 9. Komposition & 3D
- Inbyggd 3D-scen (Vulkan-baserad) – lägg plans, ljus, kamera
- Importera USD, glTF, OBJ, FBX, Blender-scen (via companion add-on)
- Tracka rörelse i 3D-space (camera-tracking) med AI-marker-förbättring
- Shadow-catcher, HDR-environment, screen-space-reflections
- Partikel/volumetric-fog, god-rays, real-time DOF
- Export 3D-data till Blender (round-trip) för avancerade grepp

## 10. AI-assistenter & agenter
- "Director-bot" – läser synopsis, föreslår storyboard, shot-list, mood-board
- "Continuity-bot" – varnar om klädsel, hår, föremål ändras mellan tagningar
- "B-roll-bot" – söker i Pexels/Pixabay/CC0 efter matchande klipp, lägger på tidslinjen
- "Music-bot" – skapar stem-baserad soundtrack baserad på klipplängd och mood-kurva
- "Export-bot" – övervakar Netflix-tech-check, varnar för illegal-gamut, fel-loudness
- "Archive-bot" – efter export flyttar rå-material till vald cold-storage (S3 Glacier, Backblaze)

## 11. Collaboration & review
- Real-time multi-user (WebRTC + CRDT) – se varandras markörer
- Kommentarer direkt på ramen, rita med pen-tablet, nämn användare → e-post/Slack
- Review-länkar: genererar krypterad URL, play-only, valbar upplösning
- Godkänn / reject / revision-status, export till PDF-shot-list
- Roll-baserade rättigheter: viewer, editor, colorist, audio, admin
- Inbyggd chatt med röstmemon, dela filer < 2 GB

## 12. Automation & scripting
- Python-API (matchar OTIO-Py) – skriva egna paneler
- Lua & JS för expressions på keyframes (After-Effects-lik)
- CLI: `okfilm render myproj.otio --preset Netflix-4K --watch`
- Batch-script: droppa mapp → auto rough-cut baserad på scene-detection
- Webhooks: färdig-render → trigga Slack, Discord, MS Teams
- Plugin-arkitektur: dynamisk laddning av .so/.dll, mall i C++ & Rust

## 13. Arkiv & DAM
- Inbyggd media-manager med AI-tagging (objekt, ansikten, text, tal-till-text)
- Thumbnail-scrub i browsern, proxy-stream över https
- Duplicate-detector: visuell hash, tar bort dubbla raw-filer
- Projekt-mallar: feature, dokumentär, tiktok, 9:16, 1:1, 360 VR
- Backup-policy: 3-2-1 wizard, verifierings-hash, e-post-rapport

## 14. Export & leverans
- Video: H.264, H.265, VP9, AV1, ProRes, DNxHD/HR, CineForm, XAVC, MPEG-2
- Container: MP4, MOV, MKV, MXF (OP-1a, OP-Atom), IMF, DCP (SMPTE/Interop)
- Upp till 16K, 120 fps, 4:4:4, 12-bit, 32-bit float
- Audio: WAV, BWF, AIFF, FLAC, AAC, AC-3, E-AC-3, Dolby Atmos (ADM), DTS-X
- Still: PNG, JPG, TIFF, DPX, EXR, PSD-layer, SVG
- Social: YouTube, Vimeo, TikTok, Instagram, Twitter, LinkedIn, Snapchat-presets
- Spel: Unity-package, Unreal Engine-seq, Godot-tscn
- Kod för blind/syntolkad ljudspår, syntolkning skriven av AI
- Bränn Blu-ray / DVD-image med meny (tack till FFmpeg + dvdauthor)
- Krypterad leverans: AES-256 zip, Aspera-cli, Signiant, S3 pre-signed

## 15. Performance & hårdvarustöd
- GPU: CUDA, ROCm, Intel Arc, Apple Metal, Vulkan, DirectCompute
- CPU-fall-back med SIMD (AVX-512, NEON) – alla kodvägar
- Utnyttja flera GPU:er (NVLink/SLI oberoende) för generering + playback
- Extern SSD-cache, NVM-cache, RAM-disk option
- Progressiv download: spela medan 8K-proxy laddas i bakgrunden
- Stöd för eGPU, Thunderbolt 4, 10/25/40/100 GbE nätverksdisk
- ARM64 (Apple Silicon, Raspberry Pi 5), x86_64, loongarch (för kinesiska datorer)

## 16. Hjälp & lärande
- Interaktiv tutorial inbyggd – steg-för-steg projekt
- Context-help: tryck "?" på varje knapp → kort video (15 s)
- AI-chat-support (Gemini) direkt i appen – fråga på svenska
- Community-forum, Discord, Matrix-room, Reddit
- Öppen roadmap på GitHub – rösta med 👍
- Översätt dokumentation till 20 språk (Crowdin)
- Öppna kurser: color grading, ljud-master, AI-generering
- Certifiering: "OK Film Colorist", "OK Film Sound Designer"

## 17. Tillgänglighet
- Skärmläsare, högkontrast-tema, tangentbords-only-läge
- Anpassningsbara genvägar, stöd för X-keys, Loupedeck, StreamDeck
- Voice-control: "OK Film, add cross dissolve", "render 4K"
- Eye-tracking UI – meny följer blicken (valfritt)
- Stöd för braille-display för textredigering

## 18. Säkerhet & integritet
- Lokala modeller som standard – ingen data skickas utan godkännande
- Kryptering i vila för projekt-cache
- Ingen telemetri utan opt-in
- Signerade binärer (Windows Authenticode, Apple Notary, GPG för Linux)
- Sandbox för plugins – begränsad filsystem-access
- 2FA-inloggning för team-samarbete

## 19. Teman & kul grejer
- Retro-tema: Final Cut 7, Avid 90-tal, Vegas 3.0 för nostalgi
- Game-tema: Minecraft-pixels, Cyberpunk-neon, Halo-Mjolnir
- Ljud-tema: varje knapptryck ger Valheim-"tick" eller Nintendo-"coin"
- Påskägg: skriv "import antigravity" i Python-konsolen → öppna XKCD
- Festligt: rendera färdigt → spela Zelda-item-fanfar
- Dark-mode-owl: efter midnakt byter appen automatiskt till "true-black"

## 20. Vision & community
- Stiftelse-driven – ingen risk för plötslig pay-wall
- Öppen finansiering: Open-Collective, GitHub Sponsors, EU-kultur-fond
- Contributor-license-agreement som inte tar copyright
- Code of Conduct (Contributor Covenant)
- Mentor-program för nykomlingar, "good first issue"-etikett
- Årlig fysisk konferens "OK-Con" med hackathon
- T-shirt, klistermärke, 3D-printad logotyp
- Svenska utvecklar-träffar varje månad (Live eller Hubben i Göteborg)

…och självklart: när filmen är klar ska export-knappen blinka "OK Filmen är färdig – världen är din biograf!" 🎬