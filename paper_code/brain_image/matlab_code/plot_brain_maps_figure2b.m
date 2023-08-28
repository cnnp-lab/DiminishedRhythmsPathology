addpath('../matlab_data/Simple-Brain-Plot-main/');

% %location to save the data. Note subject IDs will be appended to the end
% saveLoc='../figures/';
% 
% %create folder if it doesn't exist
% if ~isfolder(saveLoc)
%     
%     mkdir(saveLoc);
%     
% end

%load in the plot specifications
load('../matlab_data/plotSpecs.mat');

%load in the plot specifications for atlas description provided by the
%package
load('../matlab_data/Simple-Brain-Plot-main/examples/regionDescriptions.mat');

%read in the patient average power data
avg_power_table = readtable('../../../data/node_file_3h-6h_Delta_Cycle_power.csv');

% array for storing the modified names of the regionDescriptions.mat 
% without changing the order
lausanne120_aseg_newNames = {};
for i=1:128 % start changing the names of the subcortical areas
    roiName=regionDescriptions.lausanne120_aseg{i,1};

    if i<=14
    lausanne120_aseg_newNames{i} = roiName;
    continue
    end
    
    roiName=regionDescriptions.lausanne120_aseg{i,1};
    roiName_split=split(roiName,'-');
    if i<=71
    roiName_new=strcat('l.',roiName_split{3,1});
    else
    roiName_new=strcat('r.',roiName_split{3,1});
    end
    lausanne120_aseg_newNames{i} = roiName_new;
end

% create the cell array with the atlas names (provided by the package) to
% table
atlas_table = cell2table( lausanne120_aseg_newNames', "VariableNames", ["roi_names"]);


% merge the data with the atlas_table 
[data_merged, rows_left, rows_right] = outerjoin(atlas_table,avg_power_table,'Type','Left',"keys", "roi_names", 'MergeKeys',true);
% Sort them in order to maintain the order in left table
[~, sortinds] = sort(rows_left);
% Apply this sort order to the new table
data_merged_correctOrder = data_merged(sortinds,:);

%for every subject in our cohort plot the brain and save

%plot the average power for each cycle


% cm = [0.8431    0.1882    0.1529; ...
% 0.9569    0.4275    0.2627; ...
% 0.9922    0.6824    0.3804; ...
% 0.9961    0.8784    0.5451; ...
% 1.0000    1.0000    0.7490; ...
% 0.8510    0.9373    0.5451; ...
% 0.6510    0.8510    0.4157; ...
% 0.4000    0.7412    0.3882; ...
% 0.1020    0.5961    0.3137];

% cm = [1,0,0; 
%     1, 1, 1;
%     0, 0, 1];
% cm = interp1(cm, 1:0.01:size(cm,1));

% cm=cmaps.z_score_map;
% cm = colormap("parula");
 c = hot;
 c = flipud(c);
c = parula;
%c = flipud(c);
cm = colormap(c);
cm(1,:) = [.8,.8,.8];
% column that contains the average power values
avg_power = table2array(data_merged_correctOrder(:,6));

max_value = max(avg_power);
min_value = min(avg_power);

%if you want subcortical structures comment out line 79
%avg_power(1:14)=zeros(14,1);
avg_power(isnan(avg_power))=0;

plotBrain(regionDescriptions.lausanne120_aseg,avg_power,cm,'atlas','lausanne120',...
    'savePath', char(strcat('../../../data/plots/','figure2b_POW')),'limits', [0 max_value])

% make a plot with highlighting the SOZ only
is_soz = table2array(data_merged_correctOrder(:,5));
is_soz(isnan(is_soz))=0;

plotBrain(regionDescriptions.lausanne120_aseg,is_soz,cm,'atlas','lausanne120',...
    'savePath', char(strcat('../../../data/plots/','figure2b_SOZ')),'limits', [0 1])





