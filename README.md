# Video Audio Enhancer with Azure OpenAI

This project enhances the audio quality of videos by extracting the audio, converting it into a transcript, correcting grammar, and eliminating filler words using Azure OpenAI. The modified transcript is then converted back into audio and precisely mapped to the original video, ensuring seamless synchronization. 

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Workflow](#project-workflow)
- [Dependencies](#dependencies)
- [License](#license)

## Features

- **Automatic Speech-to-Text**: Extracts audio from the input video and converts it into text using a speech recognition engine.
- **Grammar Correction**: Corrects grammatical errors in the transcript using Azure OpenAI.
- **Filler Word Removal**: Removes common filler words such as "uh", "um", and "hmm" from the transcript to improve clarity.
- **Text-to-Speech**: Converts the cleaned transcript back into audio.
- **Seamless Audio-Video Synchronization**: Ensures the new audio is perfectly synchronized with the original video, without any delay or mismatch.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/skstanwar/Curious-PM-.git
    cd YOUR_PROJECT
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Azure OpenAI API**:
    - Create an account and get your API key from [Azure OpenAI](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/).
    - Set up your API key in the environment file .env:
    ```bash
    azure_openai_key="**********"
    ```

## Usage

1. **Provide your input video**: Place the video file in the `input` directory or specify the path in the script.

2. **Run the script**:
    ```bash
    python main.py input_video_path.mp4
    ```
    - wait for 20 to 30 secs 
   

## Project Workflow

1. **Audio Extraction**: 
    The script extracts the audio track from the input video using `MoviePy` and saves it as a separate audio file.

2. **Speech-to-Text Conversion**: 
    The extracted audio is processed using a speech recognition engine to convert it into a transcript. This step generates a text version of the spoken content.

3. **Grammar Correction and Filler Word Removal**:
    The transcript is sent to Azure OpenAI, where grammatical errors are corrected, and filler words such as "umm", "uh", and "hmm" are removed for a more professional-sounding transcript.

4. **Text-to-Speech Conversion**:
    The cleaned transcript is converted back into an audio file using a text-to-speech engine.

5. **Remapping Audio to Video**:
    The newly generated audio is remapped back to the original video. The script ensures perfect synchronization between the new audio and the video, with no delays or mismatches.

## Dependencies

- **Python**: 3.8+
- **MoviePy**: For video processing
- **Azure OpenAI**: For interacting with Azure OpenAI API
- **deepgram**: For converting audio to text
- **deepgram**: For converting text to speech

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

