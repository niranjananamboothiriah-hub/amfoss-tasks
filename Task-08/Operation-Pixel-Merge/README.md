## Task 08 — Operation Pixel Merge

Objective:

The objective of this task was to reconstruct a hidden image from a collection of fragmented image layers. Each layer contained a coloured dot on a white background, while some layers were completely white and represented breaks between separate strokes.

I used Python, OpenCV, NumPy, and Pillow to detect the dots, determine their positions and colours, arrange the layers in the correct order, and finally connect the dots to reconstruct the image.

Approach:

I divided the problem into four main steps:

Inspect and understand the provided image layers.
Detect the coloured dot and its position in each layer.
Sort the layers according to their numerical order and handle blank layers as breaks.
Draw lines between consecutive dots and generate the final image.
 
Steps:
 
1. Exploring the Image Layers

The provided repository contained the image layers inside the assets directory.

I first inspected the files and checked the properties of an image:

file "assets/Layer 1.png"

The images were 512 × 512 PNG files.

I also checked the image using Pillow and found that it was stored in palette mode (P).

2. Setting Up OpenCV

OpenCV was required for processing the images. Initially, the cv2 module was not available, so I installed it using Ubuntu's package manager:

sudo apt update
sudo apt install python3-opencv

I verified the installation with:

python3 -c "import cv2; print(cv2.__version__)"

The installed version was:

4.10.0
3. Detecting the Coloured Dot

The background of the images is white, represented in OpenCV as:

[255, 255, 255]

Therefore, I created a mask to identify pixels that were different from white:

mask = np.any(image != [255, 255, 255], axis=2)

I then obtained the coordinates of the non-white pixels:

y_coords, x_coords = np.where(mask)

Since the coloured dot can consist of multiple pixels, I calculated the average of these coordinates to obtain the centre of the dot.

For example, for Layer 1.png, the detected centre was approximately:

X = 170.0
Y = 236.5

The detected colour was:

[0, 0, 0]

which represents black in OpenCV's BGR format.

4. Handling Blank Layers

Some layers contained no coloured pixels and were completely white.

When no non-white pixels were found, the function returned:

None

These layers were treated as line breaks.

This was important because dots before and after a blank layer should not be connected.

5. Sorting the Layers

The filenames followed the pattern:

Layer 1.png
Layer 2.png
Layer 3.png
...

Simple alphabetical sorting would incorrectly place Layer 10.png before Layer 2.png.

Therefore, I extracted the number from each filename:

def get_layer_number(filename):
    return int(filename.split()[1].split(".")[0])

and used it as the sorting key:

files.sort(key=get_layer_number)

This allowed the layers to be processed in their actual numerical order.

6. Reconstructing the Image

After finding the position and colour of every dot, I created a new 512 × 512 white canvas using Pillow:

canvas = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(canvas)

For every pair of consecutive dots, I drew a line between their coordinates.

Since OpenCV uses BGR while Pillow uses RGB, I converted the colour before drawing:

rgb_colour = tuple(reversed(previous_colour))

The line was then drawn using Pillow:

draw.line(
    [previous_point, current_point],
    fill=rgb_colour,
    width=2
)

When a blank layer was encountered, the previous point was reset so that no line was drawn across the break.

7. Generating the Output

After processing all the available layers, I saved the reconstructed image as:

canvas.save("output.png")

I opened the generated image and verified the result.

Result

The final output successfully reconstructed the amFOSS symbol, confirming that the image-processing algorithm worked correctly.

Key Learnings

Through this task, I learned:

How to read and process images using OpenCV.
How image pixels can be analysed using NumPy.
How to detect objects based on their difference from a background colour.
How to calculate the centre of a group of pixels.
The difference between BGR and RGB colour formats.
How to numerically sort files based on their filenames.
How to handle special cases such as blank images.
How to draw lines and create images using Pillow.
How different Python libraries can be combined to solve an image-processing problem.
How to debug a program by testing each part separately before combining everything.

Final Output:

The generated output.png successfully revealed the amFOSS symbol from the fragmented image layers.

Files created:

solution.py
output.png
logbook.md
assets/





