"""Misc utility functions/classes"""
import os
import numpy as np


class working_directory:
    """ Context manager for temporarily changing the current working directory. """
    old_directory = None

    def __init__(self, directory, create=False):
        if directory:
            self.directory = os.path.expanduser(directory)
            if not os.path.exists(self.directory) and create:
                os.mkdir(self.directory)
        else:
            self.directory = None


    def __enter__(self):
        self.old_directory = os.getcwd()
        if self.directory:
            os.chdir(self.directory)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_directory)

def axis_rotation_matrix(angle=0, axis='x'):
    sin = np.sin(angle)
    cos = np.cos(angle)
    if axis == 'x':
        return np.array([
            [1,    0,       0],
            [0,    cos, -sin ],
            [0,    sin,  cos]])
    elif axis == 'y':
        return np.array([
            [ cos,   0,   sin],
            [   0,   1,     0],
            [-sin,   0,   cos]])

    elif axis == 'z':
        return np.array([
            [cos,  -sin,   0],
            [sin,   cos,   0],
            [0,       0,   1]])

