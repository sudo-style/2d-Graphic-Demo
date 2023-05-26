# 2D Graphic Demo

## Project Description
The 2D Graphic Demo is a project that showcases the concept of Fourier series and the Discrete Fourier Transform in a visual and interactive manner. The demo will first calculate the intital starting values of the dft, once calculated it will run and draw the path by getting the intersection of the x and y outputs of the epicyles.

## Programming Learned
- Layering graphics on the screen to create visual effects
- Implementing a clock to maintain a constant game rate
- Calculating the x and y coordinates of svg to polar coordinates

## Mathematics Learned
- Conversion from polar coordinates to Cartesian coordinates using the formula: `(r * cos(theta) + circleCenterX, r * sin(theta) + circleCenterY)`
- Manipulating the frequency (theta) to control the speed of animation and create different visual effects
- Adjusting the weights of different frequency components to reproduce specific signals

## Goal of the Project
The goal of the project is to create a visual demonstration resembling the provided GIF image, showcasing the Fourier series and its decomposition of signals into various frequency components. By interacting with the demo, users can observe how changing frequencies and weights affect the generated graphics.

![Goal Image](https://miro.medium.com/v2/resize:fit:584/0*l0zoTQqaOFAFw_6H.gif)

## Resources
- [3blue1Brown](https://www.youtube.com/watch?v=r6sGWTCMz2k)
- [Wikipedia: Fourier Series](https://en.wikipedia.org/wiki/Fourier_series)
- [Khan Academy: Fourier Series](https://www.youtube.com/watch?v=UKHBWzoOKsY)

## Libraries Used
The project utilizes the Pygame library in Python to create the graphical elements and handle user interactions.

## Documentation
To run the project, you will need python, pygame, and svgpathtools installed on your machine. 

```shell
pip install pygame
pip install svg2ppaths
pip install svgpathtools
```


Once you have the dependencies installed, you can run the project by running the FourierTransformEpicycles.py. Make sure all the source files are in the same directory. Or by downloading the zip file from GitHub.

type in the file that you want to choose, or hit enter and it will chose Andy.svg for you. You should see the program execute.
