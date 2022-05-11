from PIL import Image

def generate_art():
    print("Hello world")
    image = Image.new("RGB", (128,128), (255,255,255))
    image.save("test.png")

if __name__ == "__main__":
    generate_art()