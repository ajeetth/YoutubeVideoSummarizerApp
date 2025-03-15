import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
load_dotenv()

Prompt = """You are a highly intelligent and concise YouTube video summarizer.
Your task is to assist users by summarizing YouTube videos effectively.
When provided with a YouTube video link, you will:  
1. Fetch the transcript of the video.  
2. Generate a clear, accurate, and well-organized summary of the entire video.  

Your summary should:
- Highlight the most important points and key takeaways.  
- Present the information in bullet points for easy readability.  
- Be concise and within a limit of 400 words.  

Focus on maintaining relevance and avoiding unnecessary details.
"""

def extract_transcript(yt_video_url):
    """
    Extracts the transcript text of a YouTube video using its URL.
    Args: yt_video_url (str): The URL of the YouTube video.
    Returns: str: The concatenated transcript text of the video.
    Raises Exception: If an error occurs while fetching the transcript, the exception is raised for debugging.
    """
    try:
        video_id = yt_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id)
        transcript = " ".join([i['text'] for i in transcript_text])
        return transcript
    except Exception as e: 
        raise e
    
def generate_summary(transcript, prompt):
    """
    Generates a summary of the given transcript using a generative AI model.
    Args:
        transcript (str): The transcript text of the video.
        prompt (str): A prompt providing context or instructions for generating the summary.
    Returns:
        str: The generated summary text.
    Note:
        This function uses the models/gemini-2.0-flash-thinking-exp-01-21 generative model to generate content.
    """
    model = genai.GenerativeModel('models/gemini-2.0-flash-thinking-exp-01-21')
    response = model.generate_content(prompt+transcript)
    return response.text