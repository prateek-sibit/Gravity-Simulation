# Three body problem simulation

def three_body_problem(): # Function for simulating three gravitational bodies

    scene.fullscreen=True
    scene.title='Three body Problem'
    scene.autoscale=0
    scene.range=2
    ##   create three objects, set their initial
    ##   position, radius, color, and other
    ##   properties: mass, momentum("p")
    giant = sphere(pos=vector(-0.201,0.020,0),color=color.orange,material=materials.wood,radius=0.075) # creating a giant star
    giant.mass = 1 # mass assignment
    giant.p = vector(0, 0.051, -0.01) * giant.mass # setting the momentum vector
    lamp = local_light(pos=giant.pos)
    dtheta=pi/1000 # differential angle theta to be step incremented for rotation
    giant.rotate(angle=pi/4) # initial rotation of angle=pi/4

    dwarf = sphere(pos=vector(1.5,0,0),radius=0.056,material=materials.BlueMarble) # creating a dwarf star
    dwarf.mass = 0.125 # mass assignment
    dwarf.p = -giant.p # momentum assignment
    dwarf.rotate(angle=pi/4) # initial rotation of angle=pi/4

    moon = sphere(pos=vector(0,0.5,0.5),radius=0.04,color=color.red,material=materials.wood) # creating the moon
    moon.mass = 0.00125 # mass assignment
    moon.p = 0.035 * dwarf.p # momentum assignment
    moon.rotate(angle=pi/2) # intial rotation of angle=pi/2

    ## tweak initial condition so that total momentum is zero
    giant.p -= moon.p

    ## create 'curve' objects showing where we've been
    for a in [giant, dwarf, moon]:
      a.orbit = curve(color=a.color, radius = 0.01) # similar approach like the 3 body problem

    def pstep( giant, dwarf ):
      dist = dwarf.pos - giant.pos # position vector joing the pos. vectors of dwarf and giant
      force = G * giant.mass * dwarf.mass * dist / mag(dist)**3 # computing the gravitational force vectorially
      giant.p = giant.p + force*dt # again implementing the leapfrog method for computing velocities and positions
      dwarf.p = dwarf.p - force*dt
      dist = dwarf.pos - giant.pos

    dt = 0.01 # defining a time differential dt
    G = 1
    while True:
      ## set the picture update rate (100 times per second)
      rate(100)
      giant.rotate(angle=dtheta)# these three commandss
      dwarf.rotate(angle=dtheta)# are used to add rotations to the stellar objects
      moon.rotate(angle=dtheta+50)# about their own axis

      pstep( giant, dwarf ) # function calls to pstep
      pstep( giant, moon )  # for mutual pairs
      pstep( moon, dwarf )  # to take into account the mutual attractions

      for a in [giant, dwarf, moon]:
        a.pos = a.pos + a.p/a.mass * dt # updating the position vectors
        a.orbit.append(pos=a.pos) # appending the updated vectors
