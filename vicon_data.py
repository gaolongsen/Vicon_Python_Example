from pyvicon_datastream import tools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
# Author: Longsen Gao
# Email: longsengao@gmail.com
# Tutorial for this file in Youtube: https://youtu.be/oUW-DhOWX7s

VICON_TRACKER_IP = "192.168.50.230"
OBJECT_NAME = "solar"

panel_pos_track = []


def changex(temp, position):
    return format(int(temp / 10) * 0.1, '.0f')


def vicon_data(VICON_TRACKER_IP, OBJECT_NAME):
    mytracker = tools.ObjectTracker(VICON_TRACKER_IP)
    posori = mytracker.get_position(OBJECT_NAME)

    while not posori:
        print("Wait for data")
        posori = mytracker.get_position(OBJECT_NAME)

    init_pos = np.asarray(posori[0])
    init_ori = np.asarray(posori[1])
    return init_pos, init_ori


dof_labels = ["x", "y", "z", r'$\alpha$', r'$\beta$', r'$\gamma$']
tf_labels = [r'$F_x$', r'$F_y$', r'$F_z$', r'$\tau_x$', r'$\tau_y$', r'$\tau_z$']

panel_pos_track = []
count = 0

while 1:
    panel_pos, panel_ori = vicon_data(VICON_TRACKER_IP, OBJECT_NAME)
    print("Position:",panel_pos)
    print("Rotation:",panel_ori)
    panel_pos_track.append(np.copy(panel_pos))
    count += 1
    if count > 100:
        break


panel_pos_track = np.squeeze(panel_pos_track)
# panel_pos_track = np.copy(panel_pos_track)
plt.plot(panel_pos_track[:, 0], label="X")
plt.plot(panel_pos_track[:, 1], label="Y")
plt.plot(panel_pos_track[:, 2], label="Z")

plt.show(block=True)
plt.ylim((-300, -250))
