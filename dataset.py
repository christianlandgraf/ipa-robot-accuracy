"""
MIT License

Copyright (c) 2021 Christian Landgraf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import  pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation


class RobotAccuracyDataset(object):
    """
    A simple starting point to use the dataset
    """
    
    def __init__(self):
        pass
    
    def read_csv_ur10(self, csv_file):
        """
        Read a given dataset csv file
        """
        df = pd.read_csv(csv_file, sep=';', decimal=',', header=0)
        return df
    
    
    def get_LT_TM_trafo(self, row):
        """
        Return a homogenous transformation matrix from Laser tracker to T-Mac
        """
        
        rot_LT_TM = Rotation.from_euler('XYZ',
                                        [row['measurement_rx'],
                                          row['measurement_ry'],
                                          row['measurement_rz']],
                                        degrees = True)    
        trafo_LT_TM = np.identity(4)
        trafo_LT_TM[:3, :3] = rot_LT_TM.as_matrix()
        trafo_LT_TM[:3, 3] = [row['measurement_x'], row['measurement_y'],  row['measurement_z']]
        return trafo_LT_TM
    
    def get_R_F_trafo(self, row):
        """
        Return a homogenous transformation matrix from robot base to flange
        """

        # [x, y, z, roll, pitch, yaw] format
        if 'Goal x' in row:
            rot_R_F = Rotation.from_euler('xyz',
                                          [row['Goal roll'], row['Goal pitch'], row['Goal yaw']],
                                          degrees = False)
            trafo_R_F = np.identity(4)
            trafo_R_F[:3, :3] = rot_R_F.as_matrix()
            trafo_R_F[:3, 3] = [row['Goal x']*1000, row['Goal y']*1000, row['Goal z']*1000]
        # [x, y, z, qx, qy, qz, qw] format (in case of calibration)
        elif 'flange_x' in row:
            rot_R_F = Rotation.from_quat([row['flange_qx'], row['flange_qy'], row['flange_qz'], row['flange_qw']])
            trafo_R_F = np.identity(4)
            trafo_R_F[:3, :3] = rot_R_F.as_matrix()
            trafo_R_F[:3, 3] = [row['flange_x']*1000, row['flange_y']*1000, row['flange_z']*1000]
        return trafo_R_F
    
            