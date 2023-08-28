"""
@Mariellapanag

Created on March 2023
@author: mariella

Code for computing abnormality data as well as band power

"""

# external modules
import numpy as np
import os
import pandas as pd

# internal modules
import proj_funcs.generic_funcs as generic_funcs
import proj_funcs.atlas_chan_rois_funcs as atlas_chan_rois_funcs

# choose parcellation
# parcellation index (0-3)
parc = 1
parc_scales = ['36','60','125','250']   # possible atlas parcellations

# use most common set of channels or all channels
chan_prefix = '' # most common set of channels
# chan_prefix = 'all_chan_' # all of recording with different sets of channels

# list of patients

# Choose variables to analyse
variables_analyse = "rel_log_roi_bp"

# folder for fixed frequencies analysis
var_folder = "rel_log_roi_bp_FIXED_freqs"

# frequency bands to look
fb_interest = ["Delta"]


in_dir = '../data/'

# Load atlas
atlas_path = os.path.join ( "../atlas", "atlas_scale{}.mat".format ( parc_scales[parc] ) )
# load atlas (mat file) - contains all atlas parcellations ['36', '60', '125', '250']
atlas_dict = atlas_chan_rois_funcs.load_atlas ( atlas_path )

atlas_df = pd.DataFrame({"roi_names": atlas_dict["roi_names"], "roi_x": atlas_dict["roi_xyz"][:,0],
                         "roi_y": atlas_dict["roi_xyz"][:,1], "roi_z": atlas_dict["roi_xyz"][:,2]})

patient = 14




## Load the dictionary
n_roi = None
# for each frequency band


# the measures and drs data
filename = os.path.join ( in_dir,'AUCs', '{}_ROI_AUC_scale60_SOZ_{}.mat'.format(patient, 'Delta') )

input_vars_dict = {}
generic_funcs.mat_load ( filename, input_vars_dict,
                         'cycles_power', 'auc_variable', "val",
                         "fluct_name", 'is_soz',
                         'roi_names', 'n_cycles', "n_roi" )

is_soz = input_vars_dict['is_soz'].squeeze ()
n_roi = input_vars_dict['n_roi'].squeeze ()

cycles_power = input_vars_dict['cycles_power']
auc_variable = input_vars_dict['auc_variable']

roi_names = np.array (
    [a.replace ( " ", "" ) for a in input_vars_dict['roi_names'].squeeze ()] )  # # replace all the blank space within string names
if input_vars_dict['fluct_name'].shape[0] != 1:
    fluct_name = np.array ( [a.replace ( " ", "" ) for a in input_vars_dict['fluct_name'].squeeze ()] )
else:
    fluct_name = input_vars_dict['fluct_name']


for cc in [3,7]:

    # get average power of 1 cycle
    cycles_power_1cycle = cycles_power[:, cc]

    node_file = pd.DataFrame ( {"roi_names": roi_names,
                                "values": cycles_power_1cycle, "colour": is_soz} )
    # add the x,y,z coordinates
    node_file_df = pd.merge ( node_file, atlas_df, how="left", on="roi_names" )
    # remove rows with NaN values
    node_file_df = node_file_df.dropna ().reset_index ( drop=True )

    # reorder the columns based on the BrainNet instructions
    node_file_df = node_file_df[["roi_x", "roi_y", "roi_z", "colour", "values", "roi_names"]]
    # node_file_df.to_csv ( os.path.join ( out_dir,
    #                                      "node_file_{}_{}_Cycle_power.node".format ( fluct_name[cc], var ) ),
    #                       encoding="ascii", header=False, index=False, sep=" " )

    node_file_df.to_csv ( os.path.join ( in_dir,
                                          "node_file_{}_{}_Cycle_power.csv".format ( fluct_name[cc], 'Delta' ) ),
                          header=True, index=False)
