# DiminishedRhythmsPathology
Code to reproduce figures from a paper showing diminished biological rhythms in pathological tissue from patients with epilepsy. 

To reproduce figures from the paper, please first clone this repository and download the data from zenodo (https://doi.org/10.5281/zenodo.8289342).
Place the unzipped data directory in the DiminishedRhythmsPathology directory.
Then, run the each of the scripts in paper_code/ in order: P1.extract_cycles.py, P2.compute_AUCs.py, P3.plot_AUCs.py, P4.mixedeffects.py, and P5.get_file_brain_image.py.

- P1.extract_cycles.py will filter the bandpower timeseries to get the power of each biological rhythm, storing these in the data/cycles/ directory.
- P2.compute_AUCs.py will use these cycles and the SOZ location data (data/SOZ_info.pickle) to calculate AUCs for each biological rhythm / EEG band combination, storing these in data/AUCs. It will also plot figures 1a and 2a, sotring these in data/plots.
- P3.plot_AUCs.py will create figures 1d and 2c, storing them in data/plots.
- P4.mixedeffects.py will run a mixed effects model used to generate the effect sizes in figure 3b, it will also plot 3a and 3b, storing these in data/plots.
- P5.get_file_brain_image.py will generate the data tables needed to plot the power of rhythms across the brain.
- paper_code/brain_image/matlab_code/plot_brain_maps_figure1b will use the data table to create figure 1b.
- paper_code/brain_image/matlab_code/plot_brain_maps_figure2b will use the data table to create figure 2b.

Requirements:
Python (tested on 3.8.1)
Python Dependencies:
numpy (1.24.3)
scipy (1.10.1)
matplotlib (3.7.1)
pandas (2.0.3)
seaborn (0.13.1)
statsmodels (0.14.0)

MATLAB (R2023a)

