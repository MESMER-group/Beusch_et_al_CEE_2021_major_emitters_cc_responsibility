# add pathway to folders 1 level higher (i.e., to configs)
import sys

sys.path.append("../")


import joblib
import numpy as np

# load in configurations used in this script
import configs.config_major_emitters_cmip5ng_rcpall_default as cfg

# import MESMER tools
from mesmer.io import load_cmipng, load_regs_ls_wgt_lon_lat
from mesmer.utils import convert_dict_to_arr, extract_land

print("Get config information sorted")

# directories
dir_magicc = cfg.dir_magicc
dir_median = cfg.dir_stats_median
dir_probhy = cfg.dir_stats_probhy

# rest of config
scens = cfg.scens_magicc_ref + cfg.scens_magicc_m + cfg.scens_magicc_pc
print("Scenarios considered here", scens)
esms = cfg.esms
print("ESMs", esms)
ps = cfg.ps
print("Percentiles", ps)

print("Load in MAGICC output")
Tglob_gt = joblib.load(dir_magicc + "Tglob_gt_all_scens.pkl")
# needed just for dimensions of initialized arrays

print("Grid point level statistics")

print(
    "Load in information from a single ESM to obtain region and land mask information"
)
# TODO: improve MESMER library to no longer depend on ESM run for region / land mask infos

# load in tas with global coverage
tas_g = {}
for esm in ["CanESM2"]:
    print(esm)
    tas_g_dict = {}
    for scen in ["h-rcp85"]:
        tas_g_dict[scen], _, lon, lat, _ = load_cmipng("tas", esm, scen, cfg)
    tas_g[esm] = convert_dict_to_arr(tas_g_dict)

# load in the constant files
reg_dict, ls, wgt_g, lon, lat = load_regs_ls_wgt_lon_lat(cfg.reg_type, lon, lat)

# extract land
tas, reg_dict, ls = extract_land(
    tas_g, reg_dict, wgt_g, ls, threshold_land=cfg.threshold_land
)

print("Bring all ESM-specific medians and probabilities of hot year into single arrays")
# load in the local medians (600 per ESM)
nr_esms = len(esms)
nr_gps = len(ls["gp_l"])

# initialize the arrays which will contain all local medians and probabilities for a extreme hot year
median_all = {}
probhy_all = {}
for scen in scens:
    nr_meds_per_esm, nr_ts = Tglob_gt[scen].shape
    median_all[scen] = np.zeros([nr_esms * nr_meds_per_esm, nr_ts, nr_gps])
    probhy_all[scen] = np.zeros(median_all[scen].shape)

# loop through all ESMs and fill the arrays
i = 0
for esm in esms:
    print(esm)
    median_esm = joblib.load(dir_median + "median_" + esm + "_grid_point_level.pkl")
    probhy_esm = joblib.load(dir_probhy + "probhy_" + esm + "_grid_point_level.pkl")

    for scen in scens:
        median_all[scen][i : i + nr_meds_per_esm] = median_esm[scen]
        probhy_all[scen][i : i + nr_meds_per_esm] = probhy_esm[scen]
    i += nr_meds_per_esm

print("Compute percentiles for medians and probabilities of extreme hot years")
perc_median = {}
perc_probhy = {}

for scen in scens:
    print("start with scenario", scen)
    perc_median[scen] = {}
    (
        perc_median[scen][ps[0]],
        perc_median[scen][ps[1]],
        perc_median[scen][ps[2]],
        perc_median[scen][ps[3]],
        perc_median[scen][ps[4]],
    ) = np.percentile(median_all[scen], ps, axis=0)

    perc_probhy[scen] = {}
    (
        perc_probhy[scen][ps[0]],
        perc_probhy[scen][ps[1]],
        perc_probhy[scen][ps[2]],
        perc_probhy[scen][ps[3]],
        perc_probhy[scen][ps[4]],
    ) = np.percentile(probhy_all[scen], ps, axis=0)

# save the obtained percentiles!!
joblib.dump(perc_median, dir_median + "perc_median_grid_point_level.pkl")
joblib.dump(perc_probhy, dir_probhy + "perc_probhy_grid_point_level.pkl")
