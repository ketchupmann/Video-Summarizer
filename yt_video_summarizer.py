import re
import os
from youtube_transcript_api import YouTubeTranscriptApi
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
   
def get_youtube_transcript(youtube_url):   
    # extract video ID with regex
    video_id_regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(video_id_regex, youtube_url)

    if match:
        video_id = match.group(1)
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id)
        raw_transcript = fetched_transcript.to_raw_data() 
        
        # Combine all text entries
        #transcript_text = " ".join([entry['text'] for entry in transcript_data])
        return raw_transcript

    else:
        return None

def summarize_transcript(transcript_text):
    prompt = f"Create a comprehensive summary of this video transcript that is given in json. Include:\n1. Main topic and purpose of the video\n2. Key arguments or points made\n3. Important examples or evidence provided\n4. Conclusion or main takeaways\nTranscript:{transcript_text}\nPlease structure your summary with clear sections and bullet points for readability."
    
    client = Groq(api_key=GROQ_API_KEY)

    response = client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}], temperature=0, max_tokens=1024)
    summary_output = response.choices[0].message.content
    return summary_output

#test 1
url1 = "https://www.youtube.com/watch?v=tMiQIxSX64c&t=154s"
transcript1 = get_youtube_transcript(url1)
summary1 = summarize_transcript(transcript1)
print("Summary 1:\n", summary1)
    