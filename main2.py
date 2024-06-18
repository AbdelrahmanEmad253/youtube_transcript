                                                                                # without gcp

from youtube_transcript_api import YouTubeTranscriptApi
import re

# Define your API key (optional)
API_KEY = ''

# Create YouTubeTranscriptApi object with optional API key
transcript_api = YouTubeTranscriptApi()

video_ids = ['_ygUxnPhiQo' , 'qgdgBlOwQ58']

def download_transcript(video_id):
  """
  Downloads transcript for a given YouTube video ID.
  """
  try:
    # Get transcript in English (or adjust 'en' for other languages)
    transcript = transcript_api.get_transcript(video_id, languages=['en'])

    # Combine transcript text into a single string
    transcript_text = " ".join([item['text'] for item in transcript])

    # Save transcript to a file (modify filename as needed)
    with open(f"transcript_{video_id}.txt", "w", encoding="utf-8") as f:
      f.write(transcript_text)

    print(f"Transcript downloaded for video: {video_id}")
  except Exception as e:
    print(f"Error downloading transcript for video {video_id}: {e}")

# Download transcripts for each video ID
for video_id in video_ids:
  download_transcript(video_id)

print("Download complete!")

def clean_transcript(text):
  """
  Cleans and preprocesses the transcript text.
  """
  # Remove special characters
  cleaned_text = re.sub(r'[^\w\s]', '', text)
  # Normalize whitespace
  cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
  return cleaned_text

# Load transcript and clean it
with open("transcript__ygUxnPhiQo.txt", "r", encoding="utf-8") as f:
  transcript_text = f.read()

cleaned_text = clean_transcript(transcript_text)

print("Cleaned Transcript:")
print(cleaned_text)

import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources (may take some time)
nltk.download('punkt')
nltk.download('stopwords')

# Load the cleaned transcript
with open("transcript__ygUxnPhiQo.txt", "r", encoding="utf-8") as f:
  cleaned_text = f.read()

# Tokenize the text into words
tokens = word_tokenize(cleaned_text)

# Find the 10 most frequent words (excluding stop words)
from collections import Counter
stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
word_counts = Counter(filtered_tokens).most_common(10)

# Print the 10 most frequent words
print("10 Most Frequent Words:")
for word, count in word_counts:
  print(f"{word}: {count}")

import spacy

# Load the English model (or a different model if needed)
nlp = spacy.load("en_core_web_sm")

# Load the cleaned transcript
with open("transcript__ygUxnPhiQo.txt", "r", encoding="utf-8") as f:
  cleaned_text = f.read()

# Process the text with spaCy
doc = nlp(cleaned_text)

# Extract named entities
for entity in doc.ents:
  print(f"Entity: {entity.text} ({entity.label_})")
#############################################################################################################################################################################
                                                                            # with gcp

# # Import libraries
# from googleapiclient.discovery import build
#
# # Replace with your downloaded JSON file path
# API_SERVICE_NAME = "youtube"
# API_VERSION = "v3"
# DEVELOPER_KEY = "YOUR_API_KEY"
#
# # Create a resource object
# youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)
#
# def download_transcript(video_id):
#   """Downloads transcript for a given video ID and saves it to a file.
#
#   Args:
#       video_id: The ID of the YouTube video.
#   """
#   try:
#     # Define request parameters
#     request = youtube.videos().list(
#         part="snippet",
#         id=video_id
#     )
#
#     # Execute the request
#     response = request.execute()
#
#     # Extract transcript (if available)
#     transcript = response["items"][0]["snippet"]["localized"]["en"]["transcript"]
#
#     # Save transcript to file (replace with desired filename format)
#     filename = f"transcript_{video_id}.txt"
#     with open(filename, "w", encoding="utf-8") as f:
#       f.write(transcript)
#
#     print(f"Downloaded transcript for video {video_id} to {filename}")
#   except (KeyError, ConnectionError) as e:
#     print(f"Error downloading transcript for video {video_id}: {e}")
#
# # Example usage with a list of video IDs
# video_ids = ["VIDEO_ID_1", "VIDEO_ID_2", "VIDEO_ID_3"]
# for video_id in video_ids:
#   download_transcript(video_id)
'''
Scenario 1: Successful Download
Downloaded transcript for video VIDEO_ID_1 to transcript_VIDEO_ID_1.txt
Downloaded transcript for video VIDEO_ID_2 to transcript_VIDEO_ID_2.txt

Scenario 2: Error Handling
Downloaded transcript for video VIDEO_ID_1 to transcript_VIDEO_ID_1.txt
Error downloading transcript for video VIDEO_ID_3: KeyError
'''

# you can write the same nltk for this code too