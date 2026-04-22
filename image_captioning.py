from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import os

def load_captioning_model():
    print("Loading AI model... (This may take a minute if downloading for the first time)")
    # Initialize the processor and model from Hugging Face
    # This fulfills the "transformer-based model" requirement
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def generate_caption(image_path, processor, model):
    # Check if the file exists
    if not os.path.exists(image_path):
        return "Error: Could not find the image file. Please check the path."

    try:
        # Load and convert the image to standard RGB
        raw_image = Image.open(image_path).convert('RGB')
    except Exception as e:
        return f"Error loading image: {e}"

    # Preprocess the image and prepare inputs for the model
    inputs = processor(raw_image, return_tensors="pt")

    # Generate the caption
    print("Analyzing image and generating caption...")
    out = model.generate(**inputs)
    
    # Decode the output into a human-readable string
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def main():
    print("-" * 50)
    print("Welcome to the Image Captioning AI")
    print("-" * 50)
    
    # Load the model once so we can reuse it for multiple images
    processor, model = load_captioning_model()
    
    while True:
        print("\n")
        image_path = input("Enter the path to your image file (or type 'quit' to exit): ")
        
        if image_path.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
            
        # Strip quotation marks just in case you drag-and-dropped the file into the terminal
        image_path = image_path.strip('"').strip("'")
        
        result = generate_caption(image_path, processor, model)
        print(f"\nGenerated Caption: {result.capitalize()}")

if __name__ == "__main__":
    main()