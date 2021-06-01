import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

def plot3d(points, xlim, ylim, zlim, figsize, xlabel, ylabel, zlabel):
    # source:
    # https://stackoverflow.com/questions/36700196/plot-contours-of-distribution-on-all-three-axes-in-3d-plot


    # generate some points of a 3D Gaussian
    # points = np.array([x_in, y_in, z_in])
    # points = np.random.normal(size=(3, 50))
    
    fig = plt.figure(figsize = figsize)
    ax = fig.add_subplot(111, projection='3d')

    # ax = plt.subplot(projection='3d', figsize=(8, 8))
    # ax.plot(x_in, y_in, z_in, 'o')
    ax.plot(points[0,:], points[1,:], points[2,:], 'o')

    # do kernel density estimation to get smooth estimate of distribution
    # make grid of points
    x, y, z = np.mgrid[points.min():points.max():100j, points.min():points.max():100j, points.min():points.max():100j]
    kernel = sp.stats.gaussian_kde(points)
    positions = np.vstack((x.ravel(), y.ravel(), z.ravel()))
    density = np.reshape(kernel(positions).T, x.shape)

    # plot projection of density onto z-axis
    plotdat = np.sum(density, axis=2)
    plotdat = plotdat / np.max(plotdat)
    plotx, ploty = np.mgrid[points.min():points.max():100j, points.min():points.max():100j]
    ax.contour(plotx, ploty, plotdat, offset=zlim[0], zdir='z', cmap=cm.autumn)

    #plot projection of density onto y-axis
    plotdat = np.sum(density, axis=1) #summing up density along y-axis
    plotdat = plotdat / np.max(plotdat)
    plotx, plotz = np.mgrid[points.min():points.max():100j, points.min():points.max():100j]
    ax.contour(plotx, plotdat, plotz, offset=ylim[1], zdir='y', cmap=cm.autumn)

    #plot projection of density onto x-axis
    plotdat = np.sum(density, axis=0) #summing up density along z-axis
    plotdat = plotdat / np.max(plotdat)
    ploty, plotz = np.mgrid[points.min():points.max():100j, points.min():points.max():100j]
    ax.contour(plotdat, ploty, plotz, offset=xlim[0], zdir='x', cmap=cm.autumn)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    
    ax.set_xlim(xlim)
    # ax.set_ylim(ylim[1], ylim[0])
    ax.set_ylim(ylim)
    ax.set_zlim(zlim)

    return ax


def plot3d_columns_df(df, a, b, c, x, y, z, figsize, xlabel, ylabel, zlabel):
    q = np.array([ df[df.columns[a]], df[df.columns[b]], df[df.columns[c]] ])
    return plot3d(q, x, y, z, figsize, xlabel, ylabel, zlabel)


def plot3d_vectors(a, b, c, xlim, ylim, zlim, figsize, xlabel, ylabel, zlabel):
    q = np.array([a, b, c])[:, 0, :]
    return plot3d(q, xlim, ylim, zlim, figsize, xlabel, ylabel, zlabel)





def load_activity_signal(from_, to_):
    with open('./UCI_HAR_Dataset/train/Inertial Signals/body_acc_x_train.txt') as f:
        for i in range(from_ - 1):
            f.readline()
        
        x_time = []
        for j in range(to_ - from_):
            l = f.readline()
            l = [float(x) for x in l.split()]
            if len(x_time) == 0:
                x_time = l
            else:
                x_time = x_time + l[64:]
        
    with open('./UCI_HAR_Dataset/train/Inertial Signals/body_acc_y_train.txt') as f:
        for i in range(from_ - 1):
            f.readline()
        
        y_time = []
        for j in range(to_ - from_):
            l = f.readline()
            l = [float(x) for x in l.split()]
            if len(y_time) == 0:
                y_time = l
            else:
                y_time = y_time + l[64:]
        
    with open('./UCI_HAR_Dataset/train/Inertial Signals/body_acc_z_train.txt') as f:
        for i in range(from_ - 1):
            f.readline()
        
        z_time = []
        for j in range(to_ - from_):
            l = f.readline()
            l = [float(x) for x in l.split()]
            if len(z_time) == 0:
                z_time = l
            else:
                z_time = z_time + l[64:]
        
    return x_time, y_time, z_time

def plot_activity(x_time, y_time, z_time, title):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize = (8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_time, y_time, z_time)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title(title)
    
    return ax

def plot_activity_on_ax(ax, x_time, y_time, z_time, title):
    ax.plot(x_time, y_time, z_time)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title(title)
    
    return ax


def plot_four_activities(a, b, c, d):
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize = (8, 8))

    ax = fig.add_subplot(2, 2, 1, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*a), "Activity " + str(a))

    ax = fig.add_subplot(2, 2, 2, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*b), "Activity " + str(b))

    ax = fig.add_subplot(2, 2, 3, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*c), "Activity " + str(c))

    ax = fig.add_subplot(2, 2, 4, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*d), "Activity " + str(d))
    
    return ax



def plot_eight_activities(a, b, c, d, e, f, g, h):
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize = (16, 8))

    ax = fig.add_subplot(2, 4, 1, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*a), "Activity " + str(a))

    ax = fig.add_subplot(2, 4, 2, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*b), "Activity " + str(b))

    ax = fig.add_subplot(2, 4, 3, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*c), "Activity " + str(c))

    ax = fig.add_subplot(2, 4, 4, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*d), "Activity " + str(d))
    
    ax = fig.add_subplot(2, 4, 5, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*e), "Activity " + str(e))

    ax = fig.add_subplot(2, 4, 6, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*f), "Activity " + str(f))

    ax = fig.add_subplot(2, 4, 7, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*g), "Activity " + str(g))

    ax = fig.add_subplot(2, 4, 8, projection='3d')
    ax = plot_activity_on_ax(ax, *load_activity_signal(*h), "Activity " + str(h))
    
    return ax

