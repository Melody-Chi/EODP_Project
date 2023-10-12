# League of Legends Matches Analysing
 2022 S1 COMP20008 Assignment2 sourse code, aim to predict players' kda performance while having game
# Introduction: 
 Mainly focusing on any potential relationships between kda and other variables
 as well as making visualisation.
# File structure and use of each file:
## data_wrangling.py
Processing the raw csv files from ./data/a2/games, removing any rows that
contains any null cells, removing kda outliers and merge them. Visualising
the kda distribution with and without removing outliers. Generating dataset
that contains the merged files with(global_d.csv) and without(global_d_ro.csv)
outliers to ./wrangled_data
### data_wrangling.py output:
 * plots/hist_kda_dis.png
 * plots/box_kda_dis.png
 * plots/hist_kda_ro_dis.png
 * plots/box_kda_ro_dis.png
 * wrangled_data/global_d.csv
 * wrangled_data/global_d_ro.csv
## pre_analysis.py
Analysing the processed data from ./wrangled_data, find the majority part
(level 13,14) in processed data(global_d), take the majority part of data
that removed outliers and divide it by roles, output it to ./wrangled_data
, ganerating mj_t.csv(majority with role Toplane_Jungle) and mj_o.csv
(majority with role Other). Visualising the correlation and nmi between each
variables, and output table files to ./analysis_data that collect the datas.
Visualising the links of correlation and the links of nmi between other 
variables and kda. Visualising the relationship between kda, kills, deaths and 
assists, group by minions_killed. Visualising the relationship between kda, 
damage_building, turret_kills and gold_earned.
### pre_analysis.py output:
 * plots/hist_level_dis.png
 * wrangled_data/mj_t.csv
 * wrangled_data/mj_o.csv
 * analysis_data/corr_d_tj.csv
 * plots/heat_corr_tj.png
 * analysis_data/corr_d_other.csv
 * plots/heat_corr_other.png
 * plots/kda_corr.png
 * analysis_data/nmi_d_tj.csv
 * plots/heat_nmi_tj.png
 * analysis_data/nmi_d_other.csv
 * plots/heat_nmi_other.png
 * plots/kda_nmi.png
 * plots/pair_kda_tj.png
 * plots/pair_kda_other.png
 * plots/pair_kda_dmg_tj.png
 * plots/pair_kda_dmg_other.png
## modeling.py
Modeling the majority data of mj_t.csv and mj_o.csv from ./wrangled_data, using
regression and knn methods, gnerating a few key informations of each model on the 
terminal. Visualising their result.
### modeling.py output:
 * plots/regression.png
 * plots/regression_res.png
 * plots/ds_kda_dis.png
 * plots/cm_t.png
 * plots/cm_o.png
## championVSserver.py
Get the champions with top 10 everage kda in each server, give the visualisation
### championVSserver.py output:
 * plots/NAtop10.png
 * plots/KRtop10.png
 * plots/EUtop10.png
## analysis_data
Collecting the analysised data.
## data
All raw data are stored in this folder.
## plots
Collecting all visualised graph.
## wrangled_data
Collecting all wrangled data.
# Source code usage:
* 1.data_wrangling.py 
* 2.pre_analysis.py 
* 3.modeling.py <br/>
should run one by one in order, 
because each file need to use some results that the generated in previouse files.
championVSserver.py is fine that this python file is independent with the other.
