import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string

path = '' # Path to directory with csv files with localizations
track_path = '' # Path to directory with csv files with tracks

filename = '488nm_15prcnt_20ms_30000f'
data_15_20ms = pd.read_csv(f'{path}{filename}.csv')
data_15_20ms = data_15_20ms[data_15_20ms.Channel == 0]

filename = '488nm_15prcnt_50ms_12000f'
data_15_50ms = pd.read_csv(f'{path}{filename}.csv')
data_15_50ms = data_15_50ms[data_15_50ms.Channel == 0]

filename = '488nm_15prcnt_10ms_50000f'
data_15_10ms = pd.read_csv(f'{path}{filename}.csv')
data_15_10ms = data_15_10ms[data_15_10ms.Channel == 0]

filename = '488nm_15prcnt_20ms_30000f_tracks'
tracks_15_20ms = pd.read_csv(f'{track_path}{filename}.csv')
tracks_15_20ms = tracks_15_20ms[tracks_15_20ms['Channel Index'] == 0]

filename = '488nm_15prcnt_50ms_12000f_tracks'
tracks_15_50ms = pd.read_csv(f'{track_path}{filename}.csv')
tracks_15_50ms = tracks_15_50ms[tracks_15_50ms['Channel Index'] == 0]

filename = '488nm_15prcnt_10ms_50000f_tracks'
tracks_15_10ms = pd.read_csv(f'{track_path}{filename}.csv')
tracks_15_10ms = tracks_15_10ms[tracks_15_10ms['Channel Index'] == 0]


data_15_20ms_sorted = data_15_20ms[(data_15_20ms.Frame >= 1) & data_15_20ms['p-value'] >= 0.95]
data_15_20ms_sorted['Mean precision'] = data_15_20ms_sorted.apply(lambda row: np.mean([row['X precision (nm)'], row['Y precision (nm)']]), axis = 1)
tracks_15_20ms_sorted = tracks_15_20ms[tracks_15_20ms.Frame >= 1]
tracks_15_20ms_sorted['Time'] = tracks_15_20ms_sorted.apply(lambda row: row.Steps * 0.02, axis = 1)

plot_15_20ms = data_15_20ms_sorted.groupby('Frame').size()
hist_15_20ms = tracks_15_20ms_sorted[['Track ID', 'Time']].groupby('Track ID').mean()
label_15_20ms = '50 frames per second'


data_15_50ms_sorted = data_15_50ms[(data_15_50ms.Frame >= 1) & data_15_50ms['p-value'] >= 0.95]
data_15_50ms_sorted['Mean precision'] = data_15_50ms_sorted.apply(lambda row: np.mean([row['X precision (nm)'], row['Y precision (nm)']]), axis = 1)
tracks_15_50ms_sorted = tracks_15_50ms[tracks_15_50ms.Frame >= 1]
tracks_15_50ms_sorted['Time'] = tracks_15_50ms_sorted.apply(lambda row: row.Steps * 0.05, axis = 1)

plot_15_50ms = data_15_50ms_sorted.groupby('Frame').size()
hist_15_50ms = tracks_15_50ms_sorted[['Track ID', 'Time']].groupby('Track ID').mean()
label_15_50ms = '20 frames per second'


data_15_10ms_sorted = data_15_10ms[(data_15_10ms.Frame >= 1) & data_15_10ms['p-value'] >= 0.95]
data_15_10ms_sorted['Mean precision'] = data_15_10ms_sorted.apply(lambda row: np.mean([row['X precision (nm)'], row['Y precision (nm)']]), axis = 1)
tracks_15_10ms_sorted = tracks_15_10ms[tracks_15_10ms.Frame >= 1]
tracks_15_10ms_sorted['Time'] = tracks_15_10ms_sorted.apply(lambda row: row.Steps * 0.01, axis = 1)

plot_15_10ms = data_15_10ms_sorted.groupby('Frame').size()
hist_15_10ms = tracks_15_10ms_sorted[['Track ID', 'Time']].groupby('Track ID').mean()
label_15_10ms = '100 frames per second'

mosaic = """
          BBB
          CDE
          """

fig = plt.figure(layout = 'constrained', figsize = (16, 8))
axes = fig.subplot_mosaic(mosaic)


# Counts per frame

# ax1 = axes['A']
# ax1.plot(plot_15_10ms/plot_15_10ms.max(), color = 'darkblue', label = label_15_10ms)
# ax1.plot(plot_15_20ms/plot_15_20ms.max(), color = 'darkred', label = label_15_20ms)
# ax1.plot(plot_15_50ms/plot_15_50ms.max(), color = 'darkgreen', label = label_15_50ms)






# ax1.set_ylabel('Localizations, normed', fontsize = 20)
# ax1.set_xlabel('Frames', fontsize = 20)
# ax1.set_xlim(0)
# ax1.set_yticklabels(labels = ax1.get_yticklabels(), fontsize = 14)
# ax1.set_xticklabels(labels = ax1.get_xticklabels(), fontsize = 14)
# ax1.legend(loc = 'best', frameon = False, fontsize = 16)

# Counts per s

ax2 = axes['B']
ax2.plot([0.01 * x for x in plot_15_10ms.index.values], plot_15_10ms/plot_15_10ms.max(), color = 'darkblue', label = label_15_10ms)
ax2.plot([0.02 * x for x in plot_15_20ms.index.values], plot_15_20ms/plot_15_20ms.max(), color = 'darkred', label = label_15_20ms)
ax2.plot([0.05 * x for x in plot_15_50ms.index.values], plot_15_50ms/plot_15_50ms.max(), color = 'darkgreen', label = label_15_50ms)





ax2.set_ylabel('Localizations, normed', fontsize = 20)
ax2.set_xlabel('Time, s', fontsize = 20)
ax2.set_xlim(0)
ax2.set_yticklabels(labels = ax2.get_yticklabels(), fontsize = 14)
ax2.set_xticklabels(labels = ax2.get_xticklabels(), fontsize = 14)

ax2.legend(loc = 'best', frameon = False, fontsize = 16)

# precision

ax3 = axes['C']
ax3.hist(data_15_10ms_sorted['Mean precision'], density = True, histtype = 'step', bins = 50, color = 'darkblue', label = label_15_10ms, range = (0, 80))
ax3.hist(data_15_20ms_sorted['Mean precision'], density = True, histtype = 'step', bins = 50, color = 'darkred', label = label_15_20ms, range = (0, 80))
ax3.hist(data_15_50ms_sorted['Mean precision'], density = True, histtype = 'step', bins = 50, color = 'darkgreen', label = label_15_50ms, range = (0, 80))

ax3.axvline(data_15_10ms_sorted['Mean precision'].median(), color = 'darkblue', linestyle="dashed")
ax3.axvline(data_15_20ms_sorted['Mean precision'].median(), color = 'darkred', linestyle="dashed")
ax3.axvline(data_15_50ms_sorted['Mean precision'].median(), color = 'darkgreen', linestyle="dashed")

ax3.set_ylabel('Frequency', fontsize = 20)
ax3.set_xlabel('Precision, nm', fontsize = 20)
ax3.set_xlim(0)
ax3.set_yticks([])
ax3.set_yticklabels(labels = [], fontsize = 14)
ax3.set_xticklabels(labels = ax3.get_xticklabels(), fontsize = 14)
ax3.legend(loc = 'best', frameon = False, fontsize = 14)

# photons

ax4 = axes['D']
ax4.hist(data_15_10ms_sorted.Photons, density = True, histtype = 'step', bins = 50, color = 'darkblue', label = label_15_10ms, range = (0, 6000))
ax4.hist(data_15_20ms_sorted.Photons, density = True, histtype = 'step', bins = 50, color = 'darkred', label = label_15_20ms, range = (0, 6000))
ax4.hist(data_15_50ms_sorted.Photons, density = True, histtype = 'step', bins = 50, color = 'darkgreen', label = label_15_50ms, range = (0, 6000))

ax4.axvline(data_15_10ms_sorted.Photons.median(), color = 'darkblue', linestyle="dashed")
ax4.axvline(data_15_20ms_sorted.Photons.median(), color = 'darkred', linestyle="dashed")
ax4.axvline(data_15_50ms_sorted.Photons.median(), color = 'darkgreen', linestyle="dashed")

ax4.set_ylabel('Frequency', fontsize = 20)
ax4.set_xlabel('Photon count', fontsize = 20)
ax4.set_xlim(0)
ax4.set_yticks([])
ax4.set_yticklabels(labels = [], fontsize = 14)
ax4.set_xticklabels(labels = ax4.get_xticklabels(), fontsize = 14)
ax4.legend(loc = 'best', frameon = False, fontsize = 14)

# blink time

ax5 = axes['E']
ax5.hist(hist_15_10ms.Time, density = True, cumulative = -1, histtype = 'step', bins = 20, color = 'darkblue', label = label_15_10ms, range = (0, 1.0))
ax5.hist(hist_15_20ms.Time, density = True, cumulative = -1, histtype = 'step', bins = 20, color = 'darkred', label = label_15_20ms, range = (0, 1.0))
ax5.hist(hist_15_50ms.Time, density = True, cumulative = -1, histtype = 'step', bins = 20, color = 'darkgreen', label = label_15_50ms, range = (0, 1.0))
ax5.axhline(0.5, color = 'blue', linestyle = 'dashed', linewidth = 1)




ax5.set_ylabel('Fractions of\n track lengths ≥ T', fontsize = 20)
ax5.set_xlabel('T, s', fontsize = 20)
ax5.set_xlim(0)
ax5.set_yticklabels(labels = [], fontsize = 14)
ax5.set_yticks([])
ax5.set_xticklabels(labels = ax5.get_xticklabels(), fontsize = 14)
ax5.legend(loc = 'best', frameon = False, fontsize = 14)

for n, (key, ax) in enumerate(axes.items()):
      ax.text(-0.0, 1.1,
              string.ascii_lowercase[n],
              transform=ax.transAxes,
              size=40)

plt.savefig(f'{path}488nm_15%_sup.png',
            dpi = 400,
            bbox_inches='tight',
            transparent=False,
            facecolor='white')
