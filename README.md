# Bresenham-Matching-Functional-Plotter
(x, y) Plot function that matches Bresenham's algorithm for display refresh sync with plotting

The Bresenham algorithm's for Line or Circle plotting is an iterative algorithim which computes the next point based on the previous point.
However for screens that refresh all pixels curve plotting can be done synchronously with the refresh to reduce clock cycles depending on whether the pixel is a point on the Besenham's algorithim curve.
The function can generate a circle to an average accuracy of 99.631% Besenham's over radii of 1 to 1024 pixels.

![matching functional plot](https://raw.githubusercontent.com/Evilmmm/Bresenham-Matching-Functional-Plotter/master/circ_59-missed-280-extra-1.png)
