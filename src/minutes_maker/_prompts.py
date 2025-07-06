import inspect
from enum import Enum


class MeetingPrompts(Enum):
    """
    Enum for storing prompts for meeting minutes in desired language.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """

    TRANSCRIBE_FORMAT: str = "Transcription of the meeting regarding {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        The following text is a transcription of a meeting in {language}.
        The transcription is done by a machine learning model, and its accuracy is not 100%.
        Also, the transcription results may include not only the participants' remarks, but also background noise and descriptions of the meeting's progress.
        Please ensure your responses do not include, generate, or highlight any abusive, offensive, or inappropriate language in any language. Focus on respectful, relevant, and constructive content only.
        Bearing this in mind, please read the transcription below and answer the user's question.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        From the content of the meeting transcription, please summarize the following three points in {language}.
        Please ensure your responses do not include, generate, or highlight any abusive, offensive, or inappropriate language in any language. Focus on respectful, relevant, and constructive content only.
        Please note, describe it in markdown format, emphasizing important points in bold, making the title parts bigger, and so on, for easier reading.

        ## 1. Meeting Summary
        ## 2. Decisions Made in the Meeting
        ## 3. ToDos or Next Actions from Meeting Conclusions
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        This transcription is too long, please summarize it while ensuring the key points are captured.
        Please ensure your responses do not include, generate, or highlight any abusive, offensive, or inappropriate language in any language. Focus on respectful, relevant, and constructive content only.
        Please note that this transcription may be a part cut out from a longer transcription.
        """
    )
    
    


class LecturePrompts(Enum):
    """
    Enum for storing prompts for lecture transcripts and summaries in desired language.

    Attributes
    ----------
    TRANSCRIBE_FORMAT : str
        The format string for the prompt for transcribing the audio.
        Used in `src/minutes_maker/_transcriber.py`.

    SUMMARIZE_SYSTEM_PROMPT : str
        The system message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SUMMARY : str
        The user message for summarizing the audio.
        Used in `src/minutes_maker/_summarizer.py`.

    SUMMARIZE_USER_PROMPT_FOR_SHORTENING : str
        The user message for shortening the transcript.
        Used in `src/minutes_maker/_summarizer.py`.
    """

    TRANSCRIBE_FORMAT: str = "Transcription of the lecture regarding {content}."
    SUMMARIZE_SYSTEM_PROMPT: str = inspect.cleandoc(
        """
        The following text is a transcription of a lecture in {language}.
        The transcription is done by a machine learning model, and its accuracy is not 100%.
        Also, the transcription results may include not only the speakers' remarks, but also background noise and descriptions of the lecture's progress.
        Please ensure your responses do not include, generate, or highlight any abusive, offensive, or inappropriate language in any language. Focus on respectful, relevant, and constructive content only.
        Bearing this in mind, please read the transcription below and answer the user's question.

        '''
        {transcript}
        '''
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SUMMARY: str = inspect.cleandoc(
        """
        From the content of the lecture transcription, please summarize the following three points in {language}.
        Please ensure your responses do not include, generate, or highlight any abusive, offensive, or inappropriate language in any language. Focus on respectful, relevant, and constructive content only.
        Please note, describe it in markdown format, emphasizing important points in bold, making the title parts bigger, and so on, for easier reading.

        ## 1. Lecture Summary
        ## 2. Key Points Explained in the Lecture
        ## 3. Lecture Conclusions
        ## 4. Other Notes on the Lecture Content
        """
    )
    SUMMARIZE_USER_PROMPT_FOR_SHORTENING: str = inspect.cleandoc(
        """
        This transcription is too long, please summarize it while ensuring the key points are captured.
        Please note that this transcription may be a part cut out from a longer transcription.
        Please ensure your responses do not include, generate, or highlight any abusive, offensive, or inappropriate language in any language. Focus on respectful, relevant, and constructive content only.
        """
    )
