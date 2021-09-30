# add pathway to folders 1 level higher (i.e., to mesmer and configs)
import os
import sys

sys.path.append("../")


import joblib
import numpy as np
from scipy.stats import percentileofscore

# load in configurations used in this script
import configs.config_major_emitters_cmip5ng_rcpall_default as cfg

# import MESMER tools
from mesmer.io import load_mesmer_output

print("Get config information sorted")

# directories
dir_magicc = cfg.dir_magicc
dir_median = cfg.dir_stats_median
dir_probhy = cfg.dir_stats_probhy

# create directories if do not exist yet
os.makedirs(dir_median, exist_ok=True)
os.makedirs(dir_probhy, exist_ok=True)

# rest of config
time = np.arange(cfg.time_emus["start"], cfg.time_emus["end"] + 1)
scens = cfg.scens_magicc_ref + cfg.scens_magicc_m + cfg.scens_magicc_pc
print("Scenarios considered here", scens)
esms = cfg.esms
print("ESMs", esms)

print("Derive time indices")
# put the indices where the computations should start
idx_time = {}

# scens_magicc_ref
idx_time["h-NDC"] = 0

# scens_magicc_m
idx_time["m_top5_Paris"] = np.where(time == 2016)[0][0]
idx_time["m_top5_IPCC"] = np.where(time == 1991)[0][0]

# scens_magicc_pc
for scen_pc in cfg.scens_magicc_pc:
    idx_time[scen_pc] = np.where(time == 2030)[0][0]

print("Load in preprocessed MAGICC output")
Tglob_gt = joblib.load(dir_magicc + "Tglob_gt_all_scens.pkl")
# Tglob_gt already cut to relevant time period for each scen
# computes ref statistics for all time periods
# minustop5 statistics for period in which top5 removed
# percaptop5 statistics for 2030

print("Start with MESMER part")
for esm in esms:

    print("Start with ESM", esm)

    print("Load local trends parameters")
    params_lt = load_mesmer_output("params_lt", cfg, esm_str=esm)

    print("Create local trend emulations")
    nr_gps = params_lt["intercept"]["tas"].shape[0]

    # TODO introduce ability to compute this into mesmer-openscmrunner coupler
    emus_lt = {}
    for scen in scens:
        nr_Tglob_gts, nr_ts = Tglob_gt[scen].shape
        emus_lt[scen] = np.zeros([nr_Tglob_gts, nr_ts, nr_gps])
        for nr_gp in np.arange(nr_gps):
            emus_lt[scen][:, :, nr_gp] = (
                params_lt["coef_gttas"]["tas"][nr_gp] * Tglob_gt[scen]
                + params_lt["intercept"]["tas"][nr_gp]
            )

    print("Load local variability emulations")
    emus_lv = load_mesmer_output("emus_lv", cfg, esm_str=esm)

    print("Derive medians")
    median = {}

    for scen in scens:
        median[scen] = emus_lt[scen]
        # by definition: the true median is emus_lt

    joblib.dump(median, dir_median + "median_" + esm + "_grid_point_level.pkl")

    print("Derive probabilitiy of extreme hot year")
    probhy = {}  # probability extreme hot year
    for scen in scens:
        probhy[scen] = np.zeros(median[scen].shape)

    for run_gt in np.arange(nr_Tglob_gts):
        for scen in scens:
            emus_lv_tmp = emus_lv["all"]["tas"][:, idx_time[scen] :]
            emus_l_tmp = emus_lt[scen][run_gt] + emus_lv_tmp
            if scen == "h-NDC" and scen == scens[0]:
                # check that h-NDC is the first scen
                # compute the magnitude of a 1 in 100 years hot year in pre-industrial time period
                # the first 51 years represent 1850 - 1900 (ie the pre-industrial ref period) here
                exhy_pi = np.percentile(
                    emus_l_tmp[:, :51, :].reshape(-1, nr_gps), 99, axis=0
                )
                # extreme hot year in pre-industrial time period
            # for each time step and each grid point compute the probhry as (100 - percentileofscore)
            # ie percofscore = percentile of an event of the same magnitude as the 99th percentile event in pi times
            # in current climate -> 100 - that percentile = probability of the event to occur in current climate
            for ts in np.arange(emus_l_tmp.shape[1]):
                for gp in np.arange(nr_gps):
                    probhy[scen][run_gt, ts, gp] = 100 - percentileofscore(
                        emus_l_tmp[:, ts, gp], exhy_pi[gp]
                    )

        if run_gt % 50 == 0:
            print(
                "Done with probability for extreme hot year for global trend trajectory",
                run_gt,
            )

        del exhy_pi  # to ensure not using wrong baseline scenario

    joblib.dump(probhy, dir_probhy + "probhy_" + esm + "_grid_point_level.pkl")
