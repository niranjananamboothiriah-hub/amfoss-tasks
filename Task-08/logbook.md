# Task 08 - Operation Pixel Merge

## Objective

The objective of this task was to reconstruct an image from multiple fragmented images using OpenCV and Pillow.

Each image contained a single coloured dot on a white background. The images had to be sorted according to their numbers, the coordinates and colours of the dots had to be detected, and lines had to be drawn between consecutive dots. Completely white images represented line breaks.

## Tools and Libraries Used

- Python 3
- OpenCV (`cv2`)
- NumPy
- Pillow (`PIL`)
- Git and GitHub
- Ubuntu Linux

---

## Steps Performed

### 1. Cloned the Repository

I cloned the given Operation Pixel Merge repository into my Task-08 directory.

```bash
git clone https://github.com/hrideshmg/Operation-Pixel-Merge.git
This command downloads the repository from GitHub to the local system.

2. Inspected the Assets

I entered the cloned repository and inspected the assets directory.

cd Operation-Pixel-Merge
ls assets

The assets contained multiple PNG images named in the format:

Layer 1.png
Layer 2.png
Layer 3.png
...

The images were 512 × 512 pixels.

3. Checked an Image

I used the file command to inspect the image properties.
file "assets/Layer 1.png"

The image was confirmed to be a 512 × 512 PNG image.

I also used Pillow and OpenCV to verify the image dimensions and colour channels.

4. Installed and Verified OpenCV

Initially, OpenCV was not installed and Python produced a ModuleNotFoundError.

I installed the required OpenCV package and verified it using:

python3 -c "import cv2; print(cv2.__version__)"

The installed OpenCV version was:

4.10.0
5. Detected the Coloured Dot

OpenCV was used to identify pixels that were different from the white background.

A mask was created using NumPy:

mask = np.any(image != [255, 255, 255], axis=2)

The coordinates of the non-white pixels were obtained using:

y_coords, x_coords = np.where(mask)

The mean of the coordinates was used to determine the centre of the coloured dot.

For example, for Layer 1.png, the detected centre was approximately:

X = 170.0
Y = 236.5
Colour = [0, 0, 0]

The colour was obtained in OpenCV's BGR format.

6. Sorted the Images Numerically

The filenames could not simply be sorted alphabetically because that would place Layer 10.png before Layer 2.png.

I created a function to extract the number from each filename:

def get_layer_number(filename):
    return int(filename.split()[1].split(".")[0])

The images were then sorted using:

files.sort(key=get_layer_number)

This ensured that the layers were processed in the correct order.

7. Detected Line Breaks

Some images were completely white.

For these images, no non-white pixels were found, so the function returned:

None

These images were treated as line breaks according to the task instructions.

When a None value was detected, the previous point was reset so that a line was not drawn across the line break.

8. Used Pillow to Draw the Lines

Pillow was used to create a new 512 × 512 white canvas:

canvas = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(canvas)

Lines were drawn between consecutive detected dots using:

draw.line(
    [previous_point, current_point],
    fill=rgb_colour,
    width=2
)

Since OpenCV stores colours in BGR format while Pillow uses RGB format, the colour was converted before drawing:

rgb_colour = tuple(reversed(previous_colour))

The colour of each line was taken from the starting dot, as required by the task.

9. Generated the Final Image

The completed image was saved as:

canvas.save("output.png")

I opened the generated image using:

xdg-open output.png

The resulting image successfully revealed the amFOSS symbol.

Final Result

The fragmented images were successfully processed and connected in the correct order.

The final output.png revealed the intended amFOSS symbol, confirming that the image reconstruction was successful.

What I Learned

Through this task, I learned:

How to read and process images using OpenCV.
How to identify non-white pixels using NumPy.
How to calculate the centre of an object from pixel coordinates.
How OpenCV represents colours using BGR.
How to convert BGR colours to RGB for Pillow.
How to numerically sort filenames.
How to detect special cases such as completely white images.
How to draw lines and create images using Pillow.
How to combine OpenCV, NumPy and Pillow in a Python program.
How to use terminal commands and Python scripts to automate image processing.

### Where to put it

Inside:

```text
~/amfoss-tasks/Task-08/Operation-Pixel-Merge/

Create the file:

touch logbook.md

touch creates a new empty file.

Then open it:

code logbook.md

code opens the file in VS Code.

