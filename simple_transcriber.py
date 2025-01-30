import os
from dotenv import load_dotenv
import modal
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

stub = modal.Stub("transcription-app")

class SimpleTranscriber:
    def __init__(self):
        # Update to use the new recommended way to lookup Modal classes
        self.whisperx = modal.Cls.from_name("aip-processor", "WhisperX")()

    def transcribe_and_diarize(self, audio_file_path: str, output_file: str = None):
        """
        Transcribe and diarize an audio file, optionally saving to a text file.

        Args:
            audio_file_path: Path to the audio file
            output_file: Optional path to save the transcription
        """
        # Transcribe
        transcription = self.whisperx.transcribe.remote(audio_file_path)

        # Align transcription
        aligned = self.whisperx.align.remote(transcription, audio_file_path)

        # Diarize
        result = self.whisperx.diarize.remote(audio_file_path, aligned)

        # Format output
        formatted_transcript = []
        for segment in result["segments"]:
            speaker = segment.get("speaker", "Unknown Speaker")
            text = segment.get("text", "").strip()
            timestamp = f"[{datetime.fromtimestamp(segment['start']).strftime('%H:%M:%S')}]"
            formatted_line = f"{timestamp} {speaker}: {text}"
            formatted_transcript.append(formatted_line)

        # Join all lines
        final_transcript = "\n".join(formatted_transcript)

        # Save to file if output_file is specified
        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(final_transcript)

        return final_transcript


# Example usage:
if __name__ == "__main__":
    transcriber = SimpleTranscriber()
    transcript = transcriber.transcribe_and_diarize(
        "https://storage.aipodcast.ing/cache/trimmed_output.mp3",
        "output_transcript.txt"
    )
    print(transcript)