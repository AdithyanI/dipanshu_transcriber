# Simple Audio Transcriber

A Python-based audio transcription tool that uses Modal's WhisperX service to transcribe and diarize audio files. The tool can process audio files and generate transcripts with speaker identification and timestamps.

## Prerequisites

- Python 3
- pip (Python package installer)
- A Modal account and API credentials

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Modal credentials:
   ```plaintext
   MODAL_TOKEN_ID=your_token_id
   MODAL_TOKEN_SECRET=your_token_secret
   ```

## Usage

1. Basic usage with the SimpleTranscriber:
   ```python
   from simple_transcriber import SimpleTranscriber

   transcriber = SimpleTranscriber()
   transcript = transcriber.transcribe_and_diarize(
       "path/to/your/audio/file.mp3",
       "output_transcript.txt"
   )
   ```

2. Or run the script directly:
   ```bash
   python simple_transcriber.py
   ```

## Output Format

The transcription output includes:
- Timestamps in [HH:MM:SS] format
- Speaker identification
- Transcribed text

Example output: