Text-to-Video Generator
A Python application that generates videos from text descriptions using OpenAI's GPT API for text analysis and Pexels API for stock video content.
Features

AI-Powered Text Analysis: Uses OpenAI GPT to analyze text and extract visual concepts, themes, and keywords
Stock Video Integration: Automatically searches and downloads relevant videos from Pexels
Video Composition: Creates cohesive videos with text overlays using MoviePy
Customizable Output: Configurable clip duration, number of clips, and output settings
Command Line Interface: Easy-to-use CLI for quick video generation

Prerequisites

Python 3.7 or higher
OpenAI API key (Get one here)
Pexels API key (Get one here)
FFmpeg installed on your system (required by MoviePy)

Installation

Clone this repository:

bashgit clone https://github.com/yourusername/text-to-video-generator.git
cd text-to-video-generator

Install required packages:

bashpip install -r requirements.txt

Set up your API keys:

bashexport OPENAI_API_KEY="your_openai_api_key_here"
export PEXELS_API_KEY="your_pexels_api_key_here"
Alternatively, you can pass API keys as command line arguments.
Usage
Basic Usage
bashpython text_to_video.py "A beautiful sunset over a calm lake with mountains in the background"
Advanced Usage
bashpython text_to_video.py "A bustling city street at night with neon lights" \
  --output my_video.mp4 \
  --clips 5 \
  --duration 7 \
  --openai-key YOUR_OPENAI_KEY \
  --pexels-key YOUR_PEXELS_KEY
Command Line Options

text: The text description to convert to video (required)
-o, --output: Output video file path (default: output_video.mp4)
--openai-key: OpenAI API key (or set OPENAI_API_KEY env var)
--pexels-key: Pexels API key (or set PEXELS_API_KEY env var)
--clips: Maximum number of video clips to use (default: 3)
--duration: Duration of each clip in seconds (default: 5)

How It Works

Text Analysis: The input text is sent to OpenAI's GPT model to extract:

Main theme and concepts
Relevant keywords for video search
Emotional tone and mood
Suggested scenes and shots


Video Search: Using the extracted keywords, the application searches Pexels for relevant stock videos
Video Processing:

Downloads the best matching videos
Trims clips to specified duration
Resizes videos to standard resolution (720p)
Adds text overlay with the original description


Final Composition: Combines all clips into a single cohesive video with smooth transitions

Configuration
You can customize the behavior by modifying the TextToVideoGenerator class parameters:

max_clips: Maximum number of video clips to combine
clip_duration: Duration of each individual clip
Video resolution and quality settings
Text overlay styling (font, size, position)

Examples
Example 1: Nature Scene
bashpython text_to_video.py "A peaceful morning in a forest with sunlight filtering through the trees"
Example 2: Urban Setting
bashpython text_to_video.py "A modern office building with people walking in the lobby during rush hour" --clips 4 --duration 6
Example 3: Abstract Concept
bashpython text_to_video.py "The concept of innovation and creativity in technology" --output innovation.mp4
API Costs

OpenAI: Approximately $0.001-0.002 per text analysis (using GPT-3.5-turbo)
Pexels: Free tier includes 200 requests per hour, 20,000 per month

Limitations

Video quality depends on available stock footage matching your text
Processing time varies based on video length and complexity
Requires active internet connection for API calls and video downloads
Text overlay is basic and may need customization for specific use cases

Contributing

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

Troubleshooting
Common Issues
FFmpeg not found error:

Install FFmpeg:

Windows: Download from ffmpeg.org
macOS: brew install ffmpeg
Linux: sudo apt install ffmpeg or sudo yum install ffmpeg



API key errors:

Ensure your API keys are valid and have sufficient quota
Check that environment variables are set correctly

Video download failures:

Check your internet connection
Verify Pexels API key permissions
Some videos may have geographic restrictions

Memory issues with large videos:

Reduce the number of clips (--clips parameter)
Decrease clip duration (--duration parameter)
Close other applications to free up RAM

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

OpenAI for GPT API
Pexels for stock video content
MoviePy for video processing

Support
If you encounter any issues or have questions, please open an issue on GitHub or contact the maintainers.
