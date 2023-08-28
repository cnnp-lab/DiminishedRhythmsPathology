#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:03:07 2023

@author: nct76
"""
import proj_funcs.generic_funcs as generic_funcs
import os
import numpy as np
# %%
###### UPDATE this to where the data folder is stored ###############
in_dir = '../data/'

# list of patients

all_patients = [str(i) for i in range(0,39)]

n_patients = len ( all_patients )

extract_fluct_method = "bandpass"


# Choose variables to analyse
variables_analyse = "rel_log_roi_bp"
srate = 24 * 60 * 2


# ## For every subject save data and make plots
for i in np.arange ( 0,n_patients):  # range(n_patients):
    my_patient = all_patients[i]

    # load
    # Input path of data transformed
    fname = os.path.join ( in_dir,'bandpower_series',
                           "{}_rel_log_roi_bp_scale60.mat".format ( my_patient) )
    rel_log_bp_dict = {}
    generic_funcs.mat_load ( fname, rel_log_bp_dict,variables_analyse, "freq_band", "roi_names", "t_days",
                             "n_roi", "n_win")
    generic_funcs.mat_save ( fname, rel_log_bp_dict,variables_analyse, "freq_band", "roi_names", "t_days",
                             "n_roi", "n_win")