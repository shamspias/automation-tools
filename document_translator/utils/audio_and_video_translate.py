from .strategy import Strategy


class AudioVideoTranslate:
    """
    Convert Video to Audio and Audio to text
    """

    strategy = Strategy()

    def translate_video(self, video_file, source_lan="auto", target_lan="de", duration=None, language=None):
        text = self.strategy.video_to_text(video_file=video_file, duration=duration, language=language)
        return self.strategy.translate_strings(text=text, source_lan=source_lan, target_lan=target_lan)

    def translate_audio(self, audio_file, source_lan="auto", target_lan="de", duration=None, language=None):
        text = self.strategy.audio_to_text(audio_file=audio_file, duration=duration, language=language)
        return self.strategy.translate_strings(text=text, source_lan=source_lan, target_lan=target_lan)
