# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np
from numpy.random import default_rng
import math

rng = default_rng()
import matplotlib.pyplot as plt

edge = [[]]
parliament = cv2.imread("parliament_clock.jpg")
many_circles = cv2.imread("concentric_circles.jpg")

circle = cv2.imread("circle.jpg")
circles_copy = np.copy(circle)
canny = cv2.Canny(circles_copy, 100, 200)


#result = cv2.circle(parliament, (150,100), 50, (0,255,0), 3)
result = cv2.circle(many_circles, (154,152), 145, (0,255,0), 3)


def showImage(Img, window_name='image'):
    cv2.imshow(window_name, Img)

    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()

showImage(result, "test")
# 1.1 Edge Image
def Edge_image():
    circle = cv2.imread("circle.jpg")
    circles_copy = np.copy(circle)

    canny = cv2.Canny(circles_copy, 100, 200)

    showImage(canny), "edge image"


# 1.2 Three Point Fitting Circle

# get three random points

def generate(image):
    h = image.shape[0]
    w = image.shape[1]
    global edge
    for y in range(0, h):
        for x in range(0, w):
            if image[y, x] == 255:  # checks if value is white
                edge.append([y, x])





def rand_points(image):
    generate(image)

    p1, p2, p3 = rng.choice(len(edge), size=3,
                            replace=False)  # creates random non repetitive points, thus all the points will lie at different places and be collinear

    x1, y1 = edge[p1]
    x2, y2 = edge[p2]
    x3, y3 = edge[p3]
    lists = [[x1, y1], [x2, y2], [x3, y3]]
    return x1, y1, x2, y2, x3, y3


# loop through image and if the values are white add them to an array then using a random function get the points
# represent a line as y=mx+b?
# p1=[x1,y1]


def circle_fitting(x1, y1, x2, y2, x3, y3):
    # line 1 (x1,y1) ->(x2,y2) and line 2 (x1,y1) ->(x3,y3)
    midx1, midy1 = midpoints(x1, y1, x2, y2)  # line1
    slope1 = perpendicular_slope(x1, y1, x2, y2)
    b1 = y_intercept(slope1, midx1, midy1)

    # line 2 (x1,y1) ->(x3,y3)
    midx2, midy2 = midpoints(x1, y1, x3, y3)
    slope2 = perpendicular_slope(x1, y1, x3, y3)
    b2 = y_intercept(slope2, midx2, midy2)

    # center vals
    center_x, center_y = intersection_lines(slope1, b1, slope2, b2)
    # radius
    rad = radius(center_x, center_y, x1, y1)

    return rad, center_x, center_y


# 1.2.2 midpoints
def midpoints(x1, y1, x2, y2):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return mid_x, mid_y


# 1.2.3 slope and perpendicular slop
def perpendicular_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)

    slope_perp = -1 / slope
    return slope_perp


# 1.2.4 find the equation of the perpendicular line, gets the y-intercept
def y_intercept(slope, mid_x, mid_y):
    # mid_y = slope*mid_x+b
    b = mid_y - (slope * mid_x)
    return b


# 1.2.5  find the center value (i.e intersection of two lines
def intersection_lines(slope1, b1, slop2, b2):
    x = (b2 - b1) / (slope1 - slop2)
    y = slope1 * x + b1
    return x, y


def radius(c_x, c_y, x1, y1):
    r = math.sqrt((c_x - x1) ** 2 + (c_y - y1) ** 2)
    return r


# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
# image = cv2.circle(canny, center_coordinates, rad, color, thickness)
# showImage(image)
# Demontsrate functionality of The Circle drawing method

def test(image):
    canny_image = cv2.Canny(image, 100, 700)
    generate(canny_image)
    x1, y1, x2, y2, x3, y3 = rand_points(canny_image)
    print("first point is :" + str(x1) + "," + str(y1))
    print("second point is :" + str(x2) + "," + str(y2))
    print("third point is :" + str(x3) + "," + str(y3))
    rad, center_x, center_y = (circle_fitting(x1, y1, x2, y2, x3, y3))

    center_coordinates = (int(center_x), int(center_y))

    # Radius of circle
    rad = int(rad)

    # Blue color in BGR
    color = (0, 255, 0)

    # Line thickness of 2 px
    thickness = 3
    image_copy = np.copy(image)
    result = cv2.circle(image_copy, center_coordinates, rad, color, thickness)
    showImage(result, "test")



# 1.3 Ransac

def Ransac(image):
    # 1 initalize variables
    I = 0
    C = -1
    max_iterations = 50

    best_center, best_r = (0, 0), 0
    image_canny = cv2.Canny(image, 500, 700)
    Exit = True
    # 2.a ranodmly select 3 edge points and estimate circle parameters
    while (Exit):
        inliers = 0
        x1, y1, x2, y2, x3, y3 = rand_points(image_canny)
        rad, center_x, center_y = (circle_fitting(x1, y1, x2, y2, x3, y3))

        center_coordinates = (int(center_x), int(center_y))
        rad = int(rad)
        # 2.b count the number K inliers,  find distance from center if x is close to the radius +- ei then increment counter

        for pixel in edge:
            distance = radius(pixel[1], pixel[0], center_x,
                              center_y)  # finds the distance from the edge point to the center of the circle
            if rad - 5 <= distance <= rad + 5:  # checks if it's within a certain range from the circle
                inliers += 1

        # 2.c IF K>C update variable
        if inliers > C:
            best_center, best_r = center_coordinates, rad
            C = inliers

        # exit if criteria has been met
        '''
        if certain level of inliers is met:
            Exit=false 
        '''
        I += 1
        # exit if max iterations is reached
        if I == max_iterations:
            Exit = False


    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 3
    image_copy = np.copy(image)
    result = cv2.circle(image_copy, best_center, best_r, color, thickness)
    showImage(result, "test")

    print("number of inlier points")

    print("radius")
    print(rad)
    print("center coordinates")
    print(center_coordinates)
    print("/n")
    print("/n")


# 1.4
'''
returned a list of rand_points
x=0
for p in points:
 x +=p[0]
 y +=p[1]

centroid = (sum(x)/len(points), sum(y) / len(points))

'''
#Ransac(circle)
