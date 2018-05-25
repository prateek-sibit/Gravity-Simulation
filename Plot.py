# Energy Plotting

def energy_plot_system():

    scene.fullscreen=True
    scene.title='Earth Sun Energy Plot'
    gdisplay(xtitle='Distance(r)',ytitle='(+Y,-Y):(Total energy,Potential energy)', x=400, y=0, width=500,height=500)
    sun=sphere(pos=(0,0,0),color=color.orange,radius=100)
    earth=sphere(pos=(-520,0,0),radius=30,material=materials.BlueMarble,make_trail=true)
    potential=gcurve(color=color.cyan)
    total=gcurve(color=color.yellow)

    earthv=vector(0,0,5.6)

    while(True):
        rate(50)
        earth.pos+=earthv
        dist=(earth.x**2+earth.y**2+earth.z**2)**0.5
        RadialVector=(earth.pos-sun.pos)/dist
        FGrav=-10000*RadialVector/dist**2
        earthv+=FGrav
        potential_energy=-10000/dist
        total_energy=10000/dist
        potential.plot(pos=(dist,potential_energy))
        total.plot(pos=(dist,total_energy))

        if dist<=sun.radius:
            print("Earth collapsed!")
            break
