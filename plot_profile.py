import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string

path_roi = '' # Path to directory with rois for plot profiles
roi1_avg = pd.read_csv(f'{path_roi}Values_avg_roi1.csv')
roi1_avg['Norm'] = roi1_avg.apply(lambda row: np.divide(row['Gray_Value'] - roi1_avg['Gray_Value'].min(), roi1_avg['Gray_Value'].max() - roi1_avg['Gray_Value'].min()), axis = 1)

roi1_std = pd.read_csv(f'{path_roi}Values_std_roi1.csv')
roi1_std['Norm'] = roi1_std.apply(lambda row: np.divide(row['Gray_Value'] - roi1_std['Gray_Value'].min(), roi1_std['Gray_Value'].max() - roi1_std['Gray_Value'].min()), axis = 1)

roi1_sup = pd.read_csv(f'{path_roi}Values_sup_roi1.csv')
roi1_sup['Norm'] = roi1_sup.apply(lambda row: np.divide(row['Gray_Value'] - roi1_sup['Gray_Value'].min(), roi1_sup['Gray_Value'].max() - roi1_sup['Gray_Value'].min()), axis = 1)
roi1_sup


fig = plt.figure(figsize = (5, 5))

plt.plot(roi1_std['Distance_(microns)'], roi1_std['Norm'],  color="black", linestyle="dashed", label="Wide-field")
plt.plot(roi1_sup['Distance_(mkm)'], roi1_sup['Norm'],  color="darkred", label="BALM")

plt.xlim(0, 1.75)
plt.ylim(0, 1.3)
plt.ylabel('Intensity, norm', fontsize = 15)
plt.xlabel('Distance, \u03BCm', fontsize = 15)
plt.legend(loc = 'best', frameon = False, fontsize = 15)
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize = 13)
plt.xticks([0, 0.5, 1, 1.5], fontsize = 13)
plt.savefig(f'{path}488nm_15%_roi1_std.png',
            dpi = 400,
            bbox_inches='tight',
            transparent=False,
            facecolor='white')
