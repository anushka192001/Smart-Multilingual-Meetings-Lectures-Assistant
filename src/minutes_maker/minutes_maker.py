import logging
import subprocess
from typing import Literal, Union

from dotenv import load_dotenv

from ._prompts import (
       LecturePrompts,
       MeetingPrompts
   
)
from ._summarizer import Summarizer
from ._transcriber import Transcriber

load_dotenv()

logging.basicConfig(level=logging.INFO)


class MinutesMaker:
    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        *,
        cpu_threads: int = 0,
        num_workers: int = 1,
    ) -> None:
        """
        Initialize the MinutesMaker class with a Summarizer and
        a Transcriber.

        Parameters
        ----------
        model : str, optional
            The OpenAI model to be used for summarization,
            by default "gpt-3.5-turbo".
        cpu_threads : int, optional
            The number of CPU threads to use for inference,
            by default 0 (auto).
        num_workers : int, optional
            The number of workers to use for inference,
            by default 1 (non-parallel).
        """
        self.__summarizer = Summarizer(model=model)
        self.__transcriber = Transcriber(
            device="cuda" if self.__check_cuda() else "cpu",
            cpu_threads=cpu_threads,
            num_workers=num_workers,
        )

        self.__map_lang = [
            {'ja': 'japanese'},
            {'en': 'english'},
            {'es': 'spanish'},
            {'fr': 'french'},
            {'de': 'german'},
            {'zh': 'chinese'},
            {'hi': 'hindi'},
            {'ar': 'arabic'},
            {'ru': 'russian'},
            {'pt': 'portuguese'},
            {'ko': 'korean'},
            {'it': 'italian'},
            {'tr': 'turkish'},
            {'bn': 'bengali'},
            {'ur': 'urdu'}
        ]
        # Somehow cannot extend the Enum class,
        # we cannot make base class for prompts.
        self.__prompts: Union[
        LecturePrompts,
        MeetingPrompts
        ] = None
        

    def __call__(
        self,
        audio_or_video_file_path: str,
        language: Literal["ja", "en", "es", "fr", "de", "zh", "hi", "ar", "ru", "pt", "ko", "it", "tr", "bn", "ur"] = "en",
        category: Literal["meeting", "lecture"] = "meeting",
        content: str = "",
        *,
        beam_size: int = 5,
    ) -> tuple[str, str]:
        """
        Transcribe and summarize an audio or video file.

        Parameters
        ----------
        audio_or_video_file_path : str
            The path to the audio or video file to be summarized.
        language : Literal["ja", "en"], optional
            The language of the text to be summarized,
            by default "ja".
        category : Literal["meeting", "lecture"], optional
            The type of the audio to be summarized,
            by default "meeting"
        content : str, optional
            The content of the audio or video file to be summarized.
            e.g. 商品開発, engineering, etc.
            by default "".
        beam_size : int, optional
            The beam size to use for inference,
            by default 5.

        Returns
        -------
        tuple[str, str]
            The transcribed timeline and its summary.
        """
        if category == "meeting":
                self.__prompts =  MeetingPrompts.value.format(
                        language = self.__map_lang[language]
                    )
               
        elif category == "lecture":
                self.__prompts =  LecturePrompts.value.format(
                        language = self.__map_lang[language]
                    )
        


        results = self.__transcriber.convert_and_transcribe(
            audio_or_video_file_path,
            prompt=self.__prompts.TRANSCRIBE_FORMAT.value.format(content=content),
            beam_size=beam_size,
        ) 
        return results.timeline, self.__summarizer.summarize(
            results.transcript, prompts=self.__prompts
        ), results.chatbot_timeline
        

    def __check_cuda(self) -> bool:
        """
        Check if CUDA is available.
        This method evaluates the output of `nvidia-smi` command.
        If the output contains "NVIDIA-SMI", return True.

        Returns
        -------
        bool
            Whether CUDA is available or not.
        """
        try:
# === Edge Agent fix [human-approval] ===
# rule: human-approval — privileged action requires explicit human confirmation.
# Replace the stub below with your real approval mechanism (LangGraph
# interrupt, Slack/email confirm, CLI prompt, etc.).
# def _edge_require_human_approval(action: str) -> None:
    # raise PermissionError(
        # f"Human approval required for: {action!r} (no approval mechanism wired)"
    # )
# _edge_require_human_approval("privileged action")
# === end Edge Agent fix ===
# === Edge Agent fix [dangerous-tools] ===
            # TODO(edge-agent): tighten this allow-list to the real commands you need.
            # _EDGE_ALLOWLIST = {"ls", "git", "echo"}  # rule: dangerous-tools
            # _edge_cmd = locals().get("cmd") or locals().get("command") or ""
            # if isinstance(_edge_cmd, str) and not any(_edge_cmd.startswith(c) for c in _EDGE_ALLOWLIST):
                # raise PermissionError(f"Command not on allow-list: {_edge_cmd!r}")
            # require_human_approval(f"About to run: {_edge_cmd}")  # uncomment when wired
# === end Edge Agent fix ===
            output = subprocess.check_output("nvidia-smi", shell=True)
            if "NVIDIA-SMI" in output.decode("utf-8"):
                return True
            else:
                return False
        except Exception:
            return False
