# Pixel Neighbor Relationship Histograms

This Python script evaluates the intensity difference between two pixels based on a relationship selected by the user and generates a greyscale, RGB, HSV, and Lab histogram to illustrate the results.

## Installation

Use the package manager pip to install Opencv and Matplotlib

```bash
pip install opencv-python
pip install matplotlib
```

## Usage

After running the program in Python, several prompts will appear.

```
1 - Horizontal Left / (y,x-1)
2 - Horizontal Right / ((y,x+1)
3 - Vertical Up / (y-1,x)
4 - Vertical Down / (y+1,x)
5 - Diagonal Top Left / (y-1,x-1)
6 - Diagonal Top Right / (y-1,x+1)
7 - Diagonal Bottom Left / (y+1,x-1)
8 - Diagonal Bottom Right / (y+1,x+1)
Type a number for the pixel neighbor relationship you'd like to select:
```

Enter a number between 1 and 8 to represent the pixel relationship you would like to evaluate.

```
Type the path for the image you would like to use:
```

Enter an absolute or relative path for your image.

The program will then begin to evaluate the selected pixel relationship in the image and generate each histogram. The histograms will appear in succession and the next histogram will not appear until after the previous histogram is closed.
