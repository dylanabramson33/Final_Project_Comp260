#!/usr/bin/ env python

import pytraj as pt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class TrajectoryBuilder():
    def __init__(self,trajectory_file,topology,mask = '@*'):
        self.mask = mask
        self.trajectory_file = trajectory_file
        self.topology = topology
        self.trajectory = pt.Trajectory(trajectory_file, topology)[mask]

    def rmsd(self):
        return pt.rmsd(traj=self.trajectory, mask=self.mask)

    def kmeans(self,num_clusters):
        return pt.cluster.kmeans(self.trajectory,n_clusters=5)

traj = TrajectoryBuilder('Hexane_wat_strip.trj','Hexane_nowat.prmtop','@C,1-6')

cluster_indices = np.array(traj.kmeans(5).cluster_index)
np.save('data.npy',cluster_indices)

plt.hist(cluster_indices,bins=5)


print(cluster.cluster_index)
plt.show()
