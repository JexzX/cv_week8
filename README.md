# CV WEEK8 REPORT: Computer Vision with Python and OpenCV

**Annyeonghaseyo!**

## Project Description

This project implements Computer Vision practical assignments using Python and OpenCV based on the 4th edition of "Practical Python and OpenCV" by Adrian Rosebrock. This report covers 8 fundamental computer vision topics from image loading to edge detection.

**GitHub Repository:** https://github.com/JexzX/cv_week8

## Project Structure

```
cv_week8/
├── src/
│   ├── bab_03_loading_displaying_saving/
│   │   └── load_display_save.py
│   ├── bab_04_image_basics/
│   │   ├── akses_pixel.py
│   │   └── crop_image.py
│   ├── bab_05_drawing/
│   │   ├── gambar_bentuk.py
│   │   └── gambar_lingkaran.py
│   ├── bab_06_image_processing/
│   │   ├── transformasi.py
│   │   ├── resize_flip.py
│   │   ├── aritmatika.py
│   │   ├── bitwise.py
│   │   └── masking.py
│   ├── bab_07_histograms/
│   │   ├── histogram_grayscale.py
│   │   ├── histogram_color.py
│   │   └── equalization.py
│   ├── bab_08_smoothing_blurring/
│   │   ├── average_blur.py
│   │   ├── gaussian_blur.py
│   │   └── median_blur.py
│   ├── bab_09_thresholding/
│   │   ├── simple_threshold.py
│   │   ├── adaptive_threshold.py
│   │   └── otsu_threshold.py
│   ├── bab_10_gradients_edge_detection/
│   │   ├── laplacian_sobel.py
│   │   └── canny_edge.py
│   ├── images/
│   └── laporan/
├── README.md
└── requirements.txt
```

## Implementation by Chapter

### CHAPTER 3: Loading, Displaying, Saving

**Concepts:** Basic image operations with OpenCV - reading images from disk, displaying them, and saving in different formats.

**Implementation:** `load_display_save.py`

```python
from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)
```

**Analysis:**

- `cv2.imread()` successfully reads images and returns NumPy arrays
- `shape` attribute provides dimension information (height, width, channels)
- `cv2.imshow()` displays images in windows with `cv2.waitKey(0)` control
- `cv2.imwrite()` performs automatic format conversion (PNG to JPG)
- OpenCV stores colors in BGR format instead of RGB

### CHAPTER 4: Image Basics

**Concepts:** Digital image fundamentals - pixels, coordinate systems, direct pixel access and manipulation.

**Implementation:** `akses_pixel.py`, `crop_image.py`

```python
# akses_pixel.py
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)  # Change to red color
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# crop_image.py
cropped = image[30:120, 240:335]  # Crop specific region
cv2.imshow("T-Rex Face", cropped)
```

**Analysis:**

- Successful individual pixel access at coordinates (0,0) in BGR format
- Direct pixel value modification changes image colors
- NumPy array slicing for cropping specific regions
- OpenCV coordinate system: (0,0) at top-left, x to right, y downward
- Vectorized NumPy operations more efficient than per-pixel access

### CHAPTER 5: Drawing

**Concepts:** Drawing geometric shapes directly on images - lines, rectangles, circles.

**Implementation:** `gambar_bentuk.py`, `gambar_lingkaran.py`

```python
# gambar_bentuk.py
canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.rectangle(canvas, (10, 10), (60, 60), green)

# gambar_lingkaran.py
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)
```

**Analysis:**

- BGR color format: green=(0,255,0), red=(0,0,255), blue=(255,0,0)
- `cv2.line()` for lines with start point, end point, color, thickness parameters
- `cv2.rectangle()` with thickness -1 for solid shapes
- `cv2.circle()` for concentric and random circles
- Coordinate system uses (x,y) not (y,x) with (0,0) at top-left
- Drawing order matters as new shapes overwrite previous pixels

### CHAPTER 6: Image Processing

**Concepts:** Advanced image processing techniques - transformations, arithmetic operations, bitwise operations, masking, color spaces.

**Implementation:** `transformasi.py`, `resize_flip.py`, `aritmatika.py`, `bitwise.py`, `masking.py`

```python
# transformasi.py
def translasi(gambar, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(gambar, M, (gambar.shape[1], gambar.shape[0]))

# resize_flip.py
def resize(gambar, lebar=None, tinggi=None):
    if lebar is None:
        r = tinggi / float(h)
        dim = (int(w * r), tinggi)
    else:
        r = lebar / float(w)
        dim = (lebar, int(h * r))
    return cv2.resize(gambar, dim, interpolation=cv2.INTER_AREA)

# aritmatika.py
M = np.ones(gambar.shape, dtype="uint8") * 75
ditambah = cv2.add(gambar, M)
dikurang = cv2.subtract(gambar, M)

# bitwise.py
bitwiseAND = cv2.bitwise_and(persegi, lingkaran)
bitwiseOR = cv2.bitwise_or(persegi, lingkaran)

# masking.py
mask = np.zeros(gambar.shape[:2], dtype="uint8")
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
masked = cv2.bitwise_and(gambar, gambar, mask=mask)
```

**Analysis:**

- **Transformations:** Translation with matrix [1,0,tx] and [0,1,ty], rotation with `cv2.getRotationMatrix2D()`
- **Resize:** Maintains aspect ratio with width/height ratio calculations
- **Flip:** Parameters 0 (vertical), 1 (horizontal), -1 (both directions)
- **Arithmetic:** `cv2.add()` and `cv2.subtract()` perform automatic clipping, NumPy does wrap-around
- **Bitwise:** AND, OR, XOR, NOT operations at binary pixel level
- **Masking:** Focus on specific areas using binary mask images

### CHAPTER 7: Histograms

**Concepts:** Pixel value distribution analysis - grayscale histograms, color histograms, histogram equalization.

**Implementation:** `histogram_grayscale.py`, `histogram_color.py`, `equalization.py`

```python
# histogram_grayscale.py
gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(hist)

# histogram_color.py
chans = cv2.split(gambar)
colors = ("b", "g", "r")
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)

# equalization.py
gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(gray)
```

**Analysis:**

- `cv2.calcHist()` with bins and value range parameters
- Grayscale histograms show dark-to-bright intensity distribution
- Color histograms show separate BGR channel distributions
- Histogram equalization improves contrast by spreading pixel values
- Equalization works in grayscale domain; for color, convert to HSV first

### CHAPTER 8: Smoothing and Blurring

**Concepts:** Noise reduction and detail smoothing - averaging blur, Gaussian blur, median blur, bilateral filter.

**Implementation:** `average_blur.py`, `gaussian_blur.py`, `median_blur.py`

```python
# average_blur.py
blur3 = cv2.blur(gambar, (3, 3))
blur5 = cv2.blur(gambar, (5, 5))
blur7 = cv2.blur(gambar, (7, 7))

# gaussian_blur.py
gaussian3 = cv2.GaussianBlur(gambar, (3, 3), 0)
gaussian5 = cv2.GaussianBlur(gambar, (5, 5), 0)

# median_blur.py
median3 = cv2.medianBlur(gambar, 3)
median5 = cv2.medianBlur(gambar, 5)
```

**Analysis:**

- **Averaging:** Simple mean within kernel, uniform blur effect
- **Gaussian:** Weighted average, more natural and smooth results
- **Median:** Median value within kernel, effective for salt-and-pepper noise
- Larger kernel sizes produce stronger blur effects but require more computation
- Method selection depends on requirements: speed vs natural vs noise removal

### CHAPTER 9: Thresholding

**Concepts:** Grayscale to binary image conversion - simple thresholding, adaptive thresholding, Otsu thresholding.

**Implementation:** `simple_threshold.py`, `adaptive_threshold.py`, `otsu_threshold.py`

```python
# simple_threshold.py
(T, thresh) = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
(T, threshInv) = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

# adaptive_threshold.py
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY_INV, 11, 4)

# otsu_threshold.py
(T, thresh) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

**Analysis:**

- **Simple:** Manual thresholding with `cv2.threshold()`, results depend on T selection
- **Adaptive:** Automatic thresholding per region, robust for uneven lighting
- **Otsu:** Statistically finds optimal T in valley between histogram peaks
- Threshold results can be used as masks for object isolation
- Method selection based on image characteristics and lighting consistency

### CHAPTER 10: Gradients and Edge Detection

**Concepts:** Identifying areas of significant pixel intensity changes - Laplacian, Sobel, Canny edge detector.

**Implementation:** `laplacian_sobel.py`, `canny_edge.py`

```python
# laplacian_sobel.py
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

# canny_edge.py
canny = cv2.Canny(image, 30, 150)
```

**Analysis:**

- **Laplacian:** Edge detection in all directions, responsive but noise-sensitive
- **Sobel:** Direction-specific edge detection (X=vertical, Y=horizontal)
- **Canny:** Multi-stage pipeline (noise reduction, gradient, non-maximum suppression, hysteresis)
- Float data type (`CV_64F`) required to capture negative transitions
- Canny produces cleanest and most accurate edges for advanced applications

## Technologies Used

- **Python 3.8+**
- **OpenCV 4.5+**
- **NumPy** - Array operations and mathematics
- **Matplotlib** - Plotting and visualization
- **argparse** - Command line argument parsing

## Requirements

```txt
contourpy==1.3.3
cycler==0.12.1
fonttools==4.60.1
kiwisolver==1.4.9
matplotlib==3.10.7
numpy==2.2.6
opencv-python==4.12.0.88
packaging==25.0
pillow==12.0.0
pyparsing==3.2.5
python-dateutil==2.9.0.post0
six==1.17.0
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/JexzX/cv_week8.git
cd cv_week8
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run specific scripts:

```bash
# Example for chapter 3
python src/bab_03_loading_displaying_saving/load_display_save.py --image images/trex.png

# Example for chapter 4
python src/bab_04_image_basics/akses_pixel.py --image images/trex.png
```

## Results and Output

All implementations successfully produced the expected results:

- Image loading, display, and saving functionality working correctly
- Pixel manipulation and cropping operations performed accurately
- Geometric shapes drawn properly on canvases
- Image transformations (translation, rotation, resize, flip) applied successfully
- Arithmetic and bitwise operations produced correct outputs
- Masking techniques effectively isolated regions of interest
- Histograms accurately represented pixel intensity distributions
- Blurring techniques reduced noise as expected
- Thresholding methods successfully created binary images
- Edge detection algorithms identified image edges correctly

## Conclusion

After completing all computer vision practical assignments from chapters 3 to 10, the following conclusions can be drawn:

1. **Strong fundamentals** in basic image operations with OpenCV have been successfully mastered
2. **Pixel manipulation** and NumPy array operations provide high flexibility in image processing
3. **Drawing techniques** enable effective annotation and visualization
4. **Image processing** techniques like transformations and masking are powerful tools for image manipulation
5. **Histogram analysis** helps understand image characteristics and improve contrast
6. **Blurring methods** each have specific advantages for different requirements
7. **Thresholding techniques** evolved from manual to automatic with varied condition handling
8. **Edge detection** with Canny provides the best results for advanced computer vision applications

This practical work has successfully built comprehensive understanding of computer vision fundamentals using Python and OpenCV, providing a solid foundation for developing more complex vision applications.

**Gowamoyo!**
