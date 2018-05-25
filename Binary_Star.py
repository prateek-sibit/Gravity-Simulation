# Binary Star system simulation

def binary_star_system(): # Function for simulating two gravitation bodies
    scene.fullscreen=True
    scene.title='Binary Star System'

    lamp = local_light(pos=(-1.0,0.20,0))
    giant = sphere(pos=vector(-1.0,0.20,0),radius=0.075,color=color.cyan,material=materials.wood) # defining a gas-giant(Star)
    giant.mass = 2.5 # mass assignment
    giant.p = vector(0, 0.2, -0.3) * giant.mass # defining the momentum vector for the giant

    dwarf = sphere(pos=vector(1,0,0),radius=0.04,color=color.orange,material=materials.wood) # defining a dwarf star
    dwarf.mass = 1 # mass assignment
    dwarf.p = -giant.p # defining the momentum vector for the dwarf

    for a in [giant, dwarf]:
      a.orbit = curve(color=a.color, radius = 0.01)
    dt = 0.02
    G = 1
    while True:
        rate(100)

        dist = dwarf.pos - giant.pos # distance vector joing position vectors of dwarf to giant
        force = G * giant.mass * dwarf.mass * dist / mag(dist)**3 # vector form of the gravitational force
        ## leapfrog method
        giant.p = giant.p + force*dt # F=dp/dt dp=Fdt pf=p0+Fdt
        dwarf.p = dwarf.p - force*dt # As Force of gravity is mutually attractive , pf(dwarf)=p0(dwarf)-Fdt

        '''potential_energy=-G*giant.mass*dwarf.mass/mag(dist)
        total_energy=G*giant.mass*dwarf.mass/mag(dist)
        potential.plot(pos=(mag(dist),potential_energy))
        total.plot(pos=(mag(dist),total_energy))
        '''

        for a in [giant, dwarf]:
            a.pos = a.pos + a.p/a.mass * dt # dr/dt=v , dr=vdt => rf=r0+vdt , since vdt=mvdt/m=pdt/m
            a.orbit.append(pos=a.pos) # updating the position vector
