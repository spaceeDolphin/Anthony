import numpy as np

def f(x):
    return 1 + 1/x

x0 = np.random.randint(-9999,9999)
n = 20

xValues = np.zeros(n)

print("x0 = ", x0)

for i in range(n):
    x = f(x0)
    xValues[i] = x0
    x0 = x
    
print(x0)


#%% testing out some chatGPT code

import numpy as np
import matplotlib.pyplot as plt

# Define the size of the identity matrix
n = 5

# Create the identity matrix
I = np.identity(n)

# Calculate e to the power of the identity matrix
eI = np.exp(I)

# Plot the matrix as an image
plt.imshow(eI, cmap='gray')
plt.show()

#%% more code (this is weird)

import numpy as np
import matplotlib.pyplot as plt

# Define the number of terms in the Fourier series
n = 100

# Define the radius of the hexagon
r = 0.5

# Define the angular spacing for the hexagon
theta = np.linspace(0, 2 * np.pi, 10)

# Define the Fourier coefficients for the hexagonal shape
c = [0] * n
for i in range(1, n + 1):
    if i % 3 == 1:
        c[i-1] = r / i
    elif i % 9 == 3:
        c[i-1] = -r / i

# Define the x and y values for the Fourier series
t = np.linspace(0, 2 * np.pi, 1000)
x = np.zeros(len(t))
y = np.zeros(len(t))

# Calculate the Fourier series
for i in range(0, n):
    x += c[i] * np.cos(i * t)
    y += c[i] * np.sin(i * t)

# Plot the Fourier series as a hexagonal shape
plt.plot(x, y, 'k')
plt.axis('equal')
plt.show()

#%% cat generator?

# fourier_synthesis.py

import numpy as np
import matplotlib.pyplot as plt

image_filename = "cat.jpg"

def calculate_2dft(input):
    ft = np.fft.ifftshift(input)
    ft = np.fft.fft2(ft)
    return np.fft.fftshift(ft)

def calculate_2dift(input):
    ift = np.fft.ifftshift(input)
    ift = np.fft.ifft2(ift)
    ift = np.fft.fftshift(ift)
    return ift.real

def calculate_distance_from_centre(coords, centre):
    # Distance from centre is √(x^2 + y^2)
    return np.sqrt(
        (coords[0] - centre) ** 2 + (coords[1] - centre) ** 2
    )

def find_symmetric_coordinates(coords, centre):
    return (centre + (centre - coords[0]),
            centre + (centre - coords[1]))

def display_plots(individual_grating, reconstruction, idx):
    plt.subplot(121)
    plt.imshow(individual_grating)
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(reconstruction)
    plt.axis("off")
    plt.suptitle(f"Terms: {idx}")
    plt.pause(0.01)

# Read and process image
image = plt.imread(image_filename)
image = image[:, :, :3].mean(axis=2)  # Convert to grayscale

# Array dimensions (array is square) and centre pixel
# Use smallest of the dimensions and ensure it's odd
array_size = min(image.shape) - 1 + min(image.shape) % 2

# Crop image so it's a square image
image = image[:array_size, :array_size]
centre = int((array_size - 1) / 2)

# Get all coordinate pairs in the left half of the array,
# including the column at the centre of the array (which
# includes the centre pixel)
coords_left_half = (
    (x, y) for x in range(array_size) for y in range(centre+1)
)

# Sort points based on distance from centre
coords_left_half = sorted(
    coords_left_half,
    key=lambda x: calculate_distance_from_centre(x, centre)
)

plt.set_cmap("gray")

ft = calculate_2dft(image)

# Show grayscale image and its Fourier transform
plt.subplot(121)
plt.imshow(image)
plt.axis("off")
plt.subplot(122)
plt.imshow(np.log(abs(ft)))
plt.axis("off")
plt.pause(2)

# Reconstruct image
fig = plt.figure()
# Step 1
# Set up empty arrays for final image and
# individual gratings
rec_image = np.zeros(image.shape)
individual_grating = np.zeros(
    image.shape, dtype="complex"
)
idx = 0

# All steps are displayed until display_all_until value
display_all_until = 200
# After this, skip which steps to display using the
# display_step value
display_step = 10
# Work out index of next step to display
next_display = display_all_until + display_step

# Step 2
for coords in coords_left_half:
    # Central column: only include if points in top half of
    # the central column
    if not (coords[1] == centre and coords[0] > centre):
        idx += 1
        symm_coords = find_symmetric_coordinates(
            coords, centre
        )
        # Step 3
        # Copy values from Fourier transform into
        # individual_grating for the pair of points in
        # current iteration
        individual_grating[coords] = ft[coords]
        individual_grating[symm_coords] = ft[symm_coords]

        # Step 4
        # Calculate inverse Fourier transform to give the
        # reconstructed grating. Add this reconstructed
        # grating to the reconstructed image
        rec_grating = calculate_2dift(individual_grating)
        rec_image += rec_grating

        # Clear individual_grating array, ready for
        # next iteration
        individual_grating[coords] = 0
        individual_grating[symm_coords] = 0

        # Don't display every step
        if idx < display_all_until or idx == next_display:
            if idx > display_all_until:
                next_display += display_step
                # Accelerate animation the further the
                # iteration runs by increasing
                # display_step
                display_step += 10
            display_plots(rec_grating, rec_image, idx)

plt.show()

