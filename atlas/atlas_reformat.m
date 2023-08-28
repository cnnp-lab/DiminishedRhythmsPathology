% Reformat ATLAS.mat to make variables easier to port into python.
% Also condenses info from ATLAS.mat, atlasinfo.mat, and retains.mat into
% same workspace for each parcellation.

close all; clearvars; clc

%% project repository - atlas folder
cd('~/Documents/scripts_postdoc/22June_continuous_normative/continuous_abnormalities/data/atlas')

% load atlas info
load('ATLAS.mat')
load('atlasinfo.mat')
load('retains.mat')

%% Reformat and save atlas info for each parcellation 

% names of different parcellations
scales = {'36','60','125','250'};

% number of pcarcellations
n_parc = length(scales);

% parcellation info
for i=1:n_parc
    roi_names = eval(['ATLAS.name' scales{i}]);
    roi_dists = eval(['dists' scales{i}]);
    roi_vol = eval(['vol' scales{i}]);
    roi_xyz = eval(['xyz' scales{i}]);
    roi_retain = eval(['scale' scales{i} 'retain']);
    roi_scale = scales{i};
    
    save(['atlas_scale' scales{i} '.mat'],'roi_*')
    clearvars roi_*
end


