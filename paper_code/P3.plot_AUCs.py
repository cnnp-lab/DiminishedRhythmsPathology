#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:17:00 2023

@author: nct76
"""
# external modules
import matplotlib
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle
# internal modules

import proj_funcs.vis_funcs as vis_funcs


auc_comb_allP = pd.read_csv (
    os.path.join ( '../data/AUCs/', "AUCs.csv" ) )
#%% Figures 1 (d) and 2 (c)

auc_comb_allP['fluct_name'] = auc_comb_allP.fluct_name.str.strip()
drs_df_delta = auc_comb_allP[auc_comb_allP.band=='Delta'].reset_index()

fig, ax = plt.subplots ( 1, 1, figsize=(2.5, 3.5) )
fig.tight_layout ( rect=[0.14, 0.14, 0.87, 0.85], h_pad=3, w_pad=3 )
drs_df_delta['drs'] = drs_df_delta.AUC
vis_funcs.plot_AUC_per_cycle(drs_df_delta[drs_df_delta.fluct_name=='19h-1.3d'],x_var='fluct_name', ax = ax, size=5)
plt.ylim([0,1])
plt.savefig('../data/plots/figure1d.pdf')
#%%
fig, ax = plt.subplots ( 1, 1, figsize=(10, 7) )
fig.tight_layout ( rect=[0.14, 0.14, 0.87, 0.85], h_pad=3, w_pad=3 )
fluct_name = ['1h-3h', '3h-6h', '6h-9h', '9h-12h',
       '12h-19h']
for pos in ['right', 'top']:
    plt.gca().spines[pos].set_visible(False)

vis_funcs.plot_AUC_per_cycle(drs_df_delta.loc[(drs_df_delta.fluct_name.isin(fluct_name))],x_var='fluct_name', ax=ax, overlay_violin=True, size=5)
plt.ylim([0,1])
plt.savefig('../data/plots/figure2c.pdf')
