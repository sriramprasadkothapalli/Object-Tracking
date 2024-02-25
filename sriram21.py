import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Creating empty lists to store x and y coordinates
x_centers = []
y_centers = []

# Read the video file using OpenCV
cap = cv.VideoCapture("/home/sriram/ENPM673/object_tracking.mp4")

# Loop through each frame


while True:
    ret, frame = cap.read()

    if not ret: 
        break
  # Condition for low intensity pixels (RGB values less than 30)
    low_intensity_condition = np.all(frame < 30, axis=2)  

    # Find indices of pixels meeting the condition
    low_intensity_indices = np.where(low_intensity_condition)

    # Separate x and y coordinates (transpose for correct order)
    y_coords = low_intensity_indices[0] 
    x_coords = low_intensity_indices[1]

    # Approximate Area Calculation (optional)
    area = len(x_coords)  

    # Centroid Calculation 
    if area > 0: 
        center_x = int(np.mean(x_coords))
        center_y = int(np.mean(y_coords))

        x_centers.append(center_x)
        y_centers.append(center_y)

        # Mark the centroid on the original frame 
        cv.circle(frame, (center_x, center_y), radius=3, color=(0, 255, 0), thickness=-1)  

        # ... (Debugging print statements)

    cv.imshow("Low Intensity Tracking", frame) 



    if cv.waitKey(10) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv.destroyAllWindows()
# Plot the trajectory of the black object
plt.scatter(x_centers, y_centers, c='r')
plt.gca().invert_yaxis() 
plt.show()


# Standard equation of parabola is y = ax*2 + bx + c

x_squares = np.array([x**2 for x in x_centers])

x_centers = np.array(x_centers)
y_centers = np.array(y_centers)
x_squares = np.array(x_squares)

length = len(x_centers)

# Using least square method
X = np.column_stack((x_squares, x_centers, np.ones(length)))

inverse = np.linalg.inv(X.T @ X)

B = inverse @ X.T @ y_centers

a, b, c = B
x = 1000
y = a * x**2 + b * x + c

print("The y coordinate when x is 1000 is:", y)
plt.scatter(x_centers, y_centers, c='r')
plt.plot(x_centers, a*x_squares + b*x_centers +c)

# Mark the extrapolated point
plt.scatter(x, y, color='green', marker='*', s=100) 
plt.gca().invert_yaxis()  

plt.show()

x = None
y = None

equation= f'y = {a}*x**2 + {b}*x + {c}'
print("Equation of the curve is: ")
print(equation)
