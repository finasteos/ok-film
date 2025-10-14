![Mint-Public](https://img.shields.io/badge/repo-public-mint?style=flat-square&amp;logo=github)
![Agents](https://img.shields.io/github/issues/finasteos/ok-film?color=00ff22&amp;label=open%20tasks)

# Projektplan: OK Film

Detta dokument bryter ner manifestet i `önskalista.md` till en handlingsplan.

## FAS 0: Grundläggande Motor (Slutförd)
- [x] Projektinitiering (`ok_computer` mapp)
- [x] Virtuell miljö och grundläggande beroenden
- [x] API-nyckelhantering (`.env`)
- [x] Kärnskript (`okc.py`) med argumentparser
- [x] Simulerad implementering av alla kärnmoduler (image, video, audio, s3d, prompt-assist)
- [x] Manusintegration (`our_manus.json`)
- [x] Autentisering mot Google Cloud (ADC) löst

## FAS 1: Kärnfunktionalitet - Verklig Generering

### 1.1 Ljudgenerering (Högst prioritet)
- **Mål:** Implementera verklig ljudgenerering med Chirp 3 HD via Google Cloud TTS API.
- **Uppgifter:**
    - [ ] Felsök `google-cloud-texttospeech` importproblem.
    - [ ] Om importproblem kvarstår, implementera direkt REST-anrop till `texttospeech.googleapis.com` baserat på Node.js-exemplet.
    - [ ] Lägg till stöd för att välja olika röster (t.ex. `sv-SE-Chirp3-HD-A`) via kommandoradsargument.
    - [ ] Implementera grundläggande SSML-stöd för pauser.

### 1.2 Bildgenerering
- **Mål:** Implementera verklig bildgenerering med Imagen via Vertex AI.
- **Uppgifter:**
    - [ ] Vänta på att kvotökning för `aiplatform.googleapis.com` godkänns.
    - [ ] När kvoten är godkänd, verifiera att den befintliga Vertex AI-koden i `okc.py` fungerar.
    - [ ] Lägg till argument för bildstorlek och kvalitet.

### 1.3 Videogenerering
- **Mål:** Implementera verklig videogenerering med Veo.
- **Uppgifter:**
    - [ ] Bekräfta att fakturering är aktiverat på Google Cloud-kontot.
    - [ ] Implementera anrop till Veo-modellen via Vertex AI, liknande bildgenereringen.
    - [ ] Hantera den asynkrona naturen hos `predictLongRunning`-metoden.

## FAS 2: Projektstruktur & Automation

- **Mål:** Bygga ut skriptet för att hantera en komplett projektstruktur och automatisera arbetsflöden.
- **Uppgifter:**
    - [ ] Implementera logik för att hantera den fullständiga `assets`-strukturen (t.ex., `assets/video/S01/`).
    - [ ] Skapa en "render queue" som kan bearbeta flera kommandon i sekvens.
    - [ ] Bygg en "shot"-modul som kombinerar video, ljud och effekter baserat på en definition i `our_manus.json`.

## FAS 3: AI-agenter & Assistenter

- **Mål:** Implementera de specialiserade "bot"-agenterna från manifestet.
- **Uppgifter:**
    - [ ] **Director-bot:** Skapa ett nytt `--mode director` som tar ett synopsis och genererar ett utkast till `our_manus.json`.
    - [ ] **B-roll-bot:** Implementera sökning mot Pexels/Pixabay API.
    - [ ] **Continuity-bot:** Kräver bildanalys. Planera hur detta ska implementeras (t.ex. med Gemini Vision).

## FAS 4: Användargränssnitt & Plattformsexpansion

- **Mål:** Börja bygga mot ett grafiskt användargränssnitt och bredare plattformsstöd.
- **Uppgifter:**
    - [ ] Utvärdera UI-ramverk (Tauri, Electron, web-baserat).
    - [ ] Skapa en grundläggande "Pro-Dark" UI-prototyp.
    - [ ] Paketera applikationen för macOS (Homebrew) och skapa en Dockerfile.

---

Denna plan är en levande dokumentation och kommer att uppdateras när vi fortskrider. Nästa omedelbara steg är att lösa ljudgenereringen (FAS 1.1).