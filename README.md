# YouTube Transcript NLP

Downloads YouTube video transcripts and runs NLP on them: cleaning, tokenisation, word-frequency analysis and named-entity recognition.

**Stack:** Python, youtube-transcript-api, spaCy, NLTK

## Pipeline

Setup and imports -> define video IDs -> download transcripts -> clean text -> tokenise and analyse words -> named entity recognition (`main2.py`). The slide deck `youtube_transcript_presentation.pdf` explains each step; this is the non-GCP version.

## Run

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python main2.py
```
Edit the video IDs near the top of `main2.py`.
