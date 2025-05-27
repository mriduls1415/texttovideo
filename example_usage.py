#!/usr/bin/env python3
"""
Example usage script for the Text-to-Video Generator
Demonstrates various ways to use the TextToVideoGenerator class
"""

import os
import sys
from text_to_video import TextToVideoGenerator
from config import Config, VIDEO_PRESETS, TEXT_STYLES

def example_basic_usage():
    """Basic example of generating a video from text"""
    print("=== Basic Usage Example ===")
    
    # Initialize generator
    generator = TextToVideoGenerator(
        openai_key=os.getenv('OPENAI_API_KEY'),
        pexels_key=os.getenv('PEXELS_API_KEY')
    )
    
    # Generate video
    text = "A beautiful sunset over a calm ocean with gentle waves"
    output_path = "examples/sunset_video.mp4"
    
    success = generator.generate_video(text, output_path)
    
    if success:
        print(f"✅ Video generated successfully: {output_path}")
    else:
        print("❌ Failed to generate video")
    
    return success

def example_custom_settings():
    """Example with custom settings"""
    print("\n=== Custom Settings Example ===")
    
    generator = TextToVideoGenerator(
        openai_key=os.getenv('OPENAI_API_KEY'),
        pexels_key=os.getenv('PEXELS_API_KEY')
    )
    
    # Generate longer video with more clips
    text = "A busy city street at night with neon lights and people walking"
    output_path = "examples/city_night_video.mp4"
    
    success = generator.generate_video(
        text=text,
        output_path=output_path,
        max_clips=5,  # Use more clips
        clip_duration=8  # Longer clips
    )
    
    if success:
        print(f"✅ Custom video generated: {output_path}")
    else:
        print("❌ Failed to generate custom video")
    
    return success

def example_batch_generation():
    """Example of generating multiple videos"""
    print("\n=== Batch Generation Example ===")
    
    generator = TextToVideoGenerator(
        openai_key=os.getenv('OPENAI_API_KEY'),
        pexels_key=os.getenv('PEXELS_API_KEY')
    )
    
    texts_and_outputs = [
        ("A peaceful mountain landscape with snow-capped peaks", "examples/mountains.mp4"),
        ("A cozy coffee shop with people reading books", "examples/coffee_shop.mp4"),
        ("A futuristic cityscape with flying cars", "examples/futuristic_city.mp4")
    ]
    
    successful_generations = 0
    
    for text, output_path in texts_and_outputs:
        print(f"Generating: {text[:50]}...")
        success = generator.generate_video(text, output_path, max_clips=2, clip_duration=4)
        
        if success:
            print(f"✅ Generated: {output_path}")
            successful_generations += 1
        else:
            print(f"❌ Failed: {output_path}")
    
    print(f"Successfully generated {successful_generations}/{len(texts_and_outputs)} videos")
    return successful_generations == len(texts_and_outputs)

def example_with_analysis_only():
    """Example showing just the text analysis feature"""
    print("\n=== Text Analysis Only Example ===")
    
    generator = TextToVideoGenerator(
        openai_key=os.getenv('OPENAI_API_KEY'),
        pexels_key=os.getenv('PEXELS_API_KEY')
    )
    
    texts = [
        "A romantic dinner by candlelight",
        "An intense action scene with explosions",
        "A serene meditation session in nature"
    ]
    
    for text in texts:
        print(f"\nAnalyzing: '{text}'")
        analysis = generator.analyze_text_with_openai(text)
        
        print(f"Main Theme: {analysis.get('main_theme', 'N/A')}")
        print(f"Keywords: {', '.join(analysis.get('keywords', []))}")
        print(f"Mood: {analysis.get('mood', 'N/A')}")
        print(f"Scenes: {analysis.get('scenes', [])}")

def example_with_error_handling():
    """Example with comprehensive error handling"""
    print("\n=== Error Handling Example ===")
    
    try:
        # Try with invalid API keys to demonstrate error handling
        generator = TextToVideoGenerator(
            openai_key="invalid_key",
            pexels_key="invalid_key"
        )
        
        text = "This will fail due to invalid API keys"
        output_path = "examples/error_test.mp4"
        
        success = generator.generate_video(text, output_path)
        
        if not success:
            print("✅ Error handling worked correctly - invalid keys were handled gracefully")
        
    except Exception as e:
        print(f"Exception caught: {e}")
    
    # Now try with missing text
    try:
        if os.getenv('OPENAI_API_KEY') and os.getenv('PEXELS_API_KEY'):
            generator = TextToVideoGenerator(
                openai_key=os.getenv('OPENAI_API_KEY'),
                pexels_key=os.getenv('PEXELS_API_KEY')
            )
            
            # Empty text should be handled gracefully
            success = generator.generate_video("", "examples/empty_text.mp4")
            print("✅ Empty text was handled gracefully")
        
    except Exception as e:
        print(f"Exception with empty text: {e}")

def main():
    """Run all examples"""
    print("Text-to-Video Generator - Example Usage")
    print("=" * 50)
    
    # Check if API keys are available
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='your_key_here'")
        return
    
    if not os.getenv('PEXELS_API_KEY'):
        print("⚠️  PEXELS_API_KEY environment variable not set")
        print("Set it with: export PEXELS_API_KEY='your_key_here'")
        return
    
    # Create examples directory
    os.makedirs("examples", exist_ok=True)
    
    # Run examples
    try:
        example_basic_usage()
        example_custom_settings()
        example_batch_generation()
        example_with_analysis_only()
        example_with_error_handling()
        
        print("\n" + "=" * 50)
        print("✅ All examples completed!")
        print("Check the 'examples' directory for generated videos.")
        
    except KeyboardInterrupt:
        print("\n⚠️  Examples interrupted by user")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
