import numpy as np
import matplotlib.pyplot as plt

# Ball

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z)

# Set an equal aspect ratio
#ax.set_aspect('equal')

plt.show()

#%% Cylinder

import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

def data_for_cylinder_along_z(center_x,center_y,radius,start_z,height_z):
    z = np.linspace(start_z, height_z, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid=np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return x_grid,y_grid,z_grid


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

Xc,Yc,Zc = data_for_cylinder_along_z(0.2,0.2,0.05,0,0.05)
ax.plot_surface(Xc, Yc, Zc, alpha=0.5)

Xc2,Yc2,Zc2 = data_for_cylinder_along_z(0.2,0.2,0.07,0.2,0.3)
ax.plot_surface(Xc2, Yc2, Zc2, alpha=0.5)

plt.show()

#%% Cylinders with plotly (doesnt work)

import numpy as np
import plotly.graph_objects as go

def cylinder(r, h, a =0, nt=100, nv =50):
    """
    parametrize the cylinder of radius r, height h, base point a
    """
    theta = np.linspace(0, 2*np.pi, nt)
    v = np.linspace(a, a+h, nv )
    theta, v = np.meshgrid(theta, v)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    z = v
    return x, y, z

def boundary_circle(r, h, nt=100):
    """
    r - boundary circle radius
    h - height above xOy-plane where the circle is included
    returns the circle parameterization
    """
    theta = np.linspace(0, 2*np.pi, nt)
    x= r*np.cos(theta)
    y = r*np.sin(theta)
    z = h*np.ones(theta.shape)
    return x, y, z
r1 = 2
a1 = 0
h1 = 5

r2 = 1.35
a2 = 1
h2 = 3

x1, y1, z1 = cylinder(r1, h1, a=a1)
x2, y2, z2 = cylinder(r2, h2, a=a2)

colorscale = [[0, 'blue'],
             [1, 'blue']]

cyl1 = go.Surface(x=x1, y=y1, z=z1,
                 colorscale = colorscale,
                 showscale=False,
                 opacity=0.5)
xb_low, yb_low, zb_low = boundary_circle(r1, h=a1)
xb_up, yb_up, zb_up = boundary_circle(r1, h=a1+h1)

bcircles1 =go.Scatter3d(x = xb_low.tolist()+[None]+xb_up.tolist(),
                        y = yb_low.tolist()+[None]+yb_up.tolist(),
                        z = zb_low.tolist()+[None]+zb_up.tolist(),
                        mode ='lines',
                        line = dict(color='blue', width=2),
                        opacity =0.55, showlegend=False)

cyl2 = go.Surface(x=x2, y=y2, z=z2,
                 colorscale = colorscale,
                 showscale=False,
                 opacity=0.7)

xb_low, yb_low, zb_low = boundary_circle(r2, h=a2)
xb_up, yb_up, zb_up = boundary_circle(r2, h=a2+h2)

bcircles2 =go.Scatter3d(x = xb_low.tolist()+[None]+xb_up.tolist(),
                        y = yb_low.tolist()+[None]+yb_up.tolist(),
                        z = zb_low.tolist()+[None]+zb_up.tolist(),
                        mode ='lines',
                        line = dict(color='blue', width=2),
                        opacity =0.75, showlegend=False)

layout = go.Layout(scene_xaxis_visible=False, scene_yaxis_visible=False, scene_zaxis_visible=False)
fig =  go.Figure(data=[cyl2, bcircles2, cyl1, bcircles1], layout=layout)

fig.update_layout(scene_camera_eye_z= 0.55)
fig.layout.scene.camera.projection.type = "orthographic" #commenting this line you get a fig with perspective proj

fig.show()


#%% Contour 3D Graph

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-18, 18, 100)
y = np.linspace(-18, 18, 100)
#z = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');