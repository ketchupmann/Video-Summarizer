# Video-Summarizer
Where the video summarizer project rests

Website: https://loveable-yt-spark.lovable.app

Input YouTube video link, video ID will not be accepted.
regex is used to obtain the video id, which is then used to obtain the video transcript using YouTubeTranscriptAPI.
the raw transcript is then summarized by using Groq. 

