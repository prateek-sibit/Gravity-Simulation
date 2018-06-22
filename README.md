# Gravity-Simulation

'''
The three body problem is a mechanics problem of taking an initial set of data that specifies the positions, velocities and masses of three bodies for some specific points in space and time and then determining and studying the trajectories of those bodies ,in accordance with newton’s laws of motion (classical mechanics) The three body problem is essential nothing but a special case of the n-body problem. Historically it is seen that the first 3 body problem to have undergone an extensive study was that of the Earth Sun and the moon. In 1883 two mathematicians namely Heinrich Bruns and Henri Poincare showed that there exissts no general analytical solution for the three-body problem given by an algebraic expression or integrals.
'''

## Problem Statement :

As it was found out , it was not possible to obtain analytical solutions in the form of algebraic expressions for the three body or the n-body problem thus these problems could only be tackled through a numerical analysis.
The problem hence put forward is knowing the initial parameters of three heavenly bodies namely their masses, velocities, initial positions can we compute their trajectories and somehow visualize or display them as they traverse on these paths.

## Objectives : 

- Creating stellar objects with parameters mass, initial velocity, position
- Simulating the gravitational force
- Considering the mutual interactions of the objects
- Constantly computing and updating their trajectories
- Implementing trajectory calculations through vector methods
- Texturing and displaying planets in 3D Format
- Incorporating trajectories into VPython module for 3D Simulation
- Constructing real-time energy plots for a two body earth-sun system.

## Why and how the project was chosen :

It was a morning physics lecture on mechanics and the topic for the day was rotational motion and its aspects in context to astronomical study and planetary motion. It was after we had analyzed the study of 2 bodies under a mutual force of gravitation that our Professor told us about the complexity involved for extending this idea to three bodies. It was then that he suggested that it would be a good idea for some student to try and recreate a three body simulation as no analytical solution existed.
Merely this thought that even the greatest minds of physics could not come up with an analytical solution and yet it was possible numerically struck my mind. Upon thinking on this fact I found that the greatest machine for numerical computation was one that we all use everyday , the Computer. Upon researching further on the mathematics involved and the computational power required I decided to take up this problem as my computer science project.

## Functionality of the project :

-	It is a user interactive simulation environment
-	The user gets to choose which simulation he wants to run through the main menu 
-	The code enables the user to modify the gravitational parameters
-	Astronomical data and the values of universal constants have been manually fed into the program
-	Upon the users choice the program redirects the user to the corresponding simulation
-	The simulation provides the user with the user controls, using which the user can control his viewing perspective 
-	The potential and kinetic energy plots provide the user with a graphical interpretation of the gravitational force
-	The simulation runs on an infinite loop , thus it nevers ends on itself. Upon closing the simulation window the program returns back    to the main screen
-	From the main screen the user can then choose to either Exit the program or run another simulation

## Learnings and Reflections :

-	To actually solve a problem numerically that was considered not solvable analytically by the great minds of physics is a great feeling in itself
-	How to implement vectors in python 
-	Calculating planetary trajectories using loops
-	Visualizing how gravity works
-	Incorporating 3D models into a python program and operating on them
-	Plotting graphs in python
-	Overall this project was an eye-opener and a great learning experience as it challenged me to venture into domains unexplored by me. Had it not been for this project I would have probably not explored a new domain of python ie : VPython (Visual python) which allows us to create three dimensional intractable objects.

## HOW TO USE

1. Run the Gravity_Simulation_Project.py file
2. Follow along the main menu for controls and how to view the simulation

