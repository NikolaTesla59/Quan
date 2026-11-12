"""
High-Fidelity Vietnamese Speech Engine
Primary: Edge-TTS Neural Voice (Studio HD quality)
Secondary: Google Text-to-Speech (gTTS - reliable, unthrottled fallback)
Tertiary: Windows SAPI (pyttsx3 - local offline fallback)
"""

import os
import asyncio
import time
from typing import Optional

class VoiceEngine:
    def __init__(
        self,
        voice_gender: str = "male",
        speed_rate: str = "+0%",
        pitch: str = "+0Hz"
    ):
        self.gender = voice_gender.lower()
        if "female" in self.gender or "nữ" in self.gender:
            self.edge_voice = "vi-VN-HoaiMyNeural"
        else:
            self.edge_voice = "vi-VN-NamMinhNeural"
            
        self.rate = speed_rate
        self.pitch = pitch

    def synthesize(self, text: str, output_mp3_path: str) -> bool:
        """Synthesizes text to MP3 with multi-tier automatic fallback."""
        os.makedirs(os.path.dirname(os.path.abspath(output_mp3_path)), exist_ok=True)
        text = text.strip()
        if not text:
            return False

        # Tier 1: Edge-TTS Neural HD
        try:
            ok = self._call_edge_tts(text, output_mp3_path)
            if ok and os.path.exists(output_mp3_path) and os.path.getsize(output_mp3_path) > 1000:
                return True
        except Exception as e:
            # Microsoft occasionally rate-limits rapid requests
            pass

        # Tier 2: Google TTS (gTTS)
        try:
            from gtts import gTTS
            tts = gTTS(text=text, lang="vi", slow=False)
            tts.save(output_mp3_path)
            if os.path.exists(output_mp3_path) and os.path.getsize(output_mp3_path) > 1000:
                return True
        except Exception as e:
            print(f"[VoiceEngine] gTTS error: {e}")

        # Tier 3: pyttsx3 Windows SAPI
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.save_to_file(text, output_mp3_path)
            engine.runAndWait()
            if os.path.exists(output_mp3_path) and os.path.getsize(output_mp3_path) > 500:
                return True
        except Exception as e:
            print(f"[VoiceEngine] pyttsx3 error: {e}")

        return False

    def _call_edge_tts(self, text: str, output_path: str) -> bool:
        import edge_tts
        
        async def _run():
            comm = edge_tts.Communicate(
                text=text,
                voice=self.edge_voice,
                rate=self.rate,
                pitch=self.pitch
            )
            await comm.save(output_path)
            
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(_run())
            return True
        finally:
            loop.close()
