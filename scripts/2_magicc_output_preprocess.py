# add pathway to folders 1 level higher (i.e., to mesmer and configs)
import sys

sys.path.append("../")

import joblib
import numpy as np
import xarray as xr

# load in configurations used in this script
import configs.config_major_emitters_cmip5ng_rcpall_default as cfg

# load information from config
time_start = cfg.time_emus["start"]
time_end = cfg.time_emus["end"]
time = np.arange(time_start, time_end + 1)

ref_start = cfg.ref_magicc["start"]
ref_end = cfg.ref_magicc["end"]

ps = cfg.ps
dir_median = cfg.dir_stats_median

scens_ref = cfg.scens_magicc_ref
paths_ref = [cfg.dir_magicc_ref + f for f in cfg.files_magicc_ref]

scens_m = cfg.scens_magicc_m
paths_m = [cfg.dir_magicc_m + f for f in cfg.files_magicc_m]

scens_pc = cfg.scens_magicc_pc
paths_pc = [cfg.dir_magicc_pc + f for f in cfg.files_magicc_pc]

scens_m_se = cfg.scens_magicc_m_se
paths_m_se = [cfg.dir_magicc_m + f for f in cfg.files_magicc_m_se]

scens = scens_ref + scens_m + scens_pc
paths = paths_ref + paths_m + paths_pc

scens_KYGHG = scens + scens_m_se
paths_KYGHG = paths + paths_m_se

# Kyoto-GHG
print("Preprocess and save total Kyoto greenhouse gas emissions")
# units: GTCO2eq/year
KYGHG_em = {}
for i, scen in enumerate(scens_KYGHG):
    # load in the total anthropogenic CO2 emissions
    KYGHG_em[scen] = (
        xr.open_dataset(paths_KYGHG[i], decode_times=False)
        .totalKYOTOGHG_emis.sel(time=slice(time_start, time_end))
        .values[:, 0]
    )
    # for each MAGICC run are the same -> only need to keep 1
joblib.dump(KYGHG_em, cfg.dir_magicc + "KYOTOGHGem_all_scens.pkl")

# DeltaGMT
print("Preprocess and save probabilistic forced global warming trajectories")
Tglob_gt = {}
for i, scen in enumerate(scens):
    # load Tglob datasets
    Tglob_gt[scen] = xr.open_dataset(
        paths[i], decode_times=False
    ).global_mean_temperature.sel(time=slice(time_start, time_end))

    # change dim to standard: nr_runs x nr_ts
    Tglob_gt[scen] = Tglob_gt[scen].transpose()

    # rebaseline each run on its pre-industrial mean (ie mean 1850 - 1900 = 0)
    Tglob_gt[scen] = (
        Tglob_gt[scen] - Tglob_gt[scen].sel(time=slice(ref_start, ref_end)).mean(axis=1)
    ).values


# compute ref statistics for all time periods
# minustop5 statistics for period in which top5 removed
# percaptop5 statistics for 2030

# put the indices where the computations should start
idx_time = {}

# scens_magicc_ref
idx_time["h-NDC"] = 0

# scens_magicc_m
idx_time["m_top5_Paris"] = np.where(time == 2016)[0][0]
idx_time["m_top5_IPCC"] = np.where(time == 1991)[0][0]

# scens_magicc_pc
for scen_pc in scens_pc:
    idx_time[scen_pc] = np.where(time == 2030)[0][0]

print("Cut forced warming trends to time periods of interest for each scenario")
for scen in scens:
    Tglob_gt[scen] = Tglob_gt[scen][:, idx_time[scen] :]
joblib.dump(Tglob_gt, cfg.dir_magicc + "Tglob_gt_all_scens.pkl")


print("Start with forced global warming statistics computations")

print("Derived forced global warming percentiles")
perc_Tglob_gt = {}
for scen in scens:
    perc_Tglob_gt[scen] = {}
    (
        perc_Tglob_gt[scen][ps[0]],
        perc_Tglob_gt[scen][ps[1]],
        perc_Tglob_gt[scen][ps[2]],
        perc_Tglob_gt[scen][ps[3]],
        perc_Tglob_gt[scen][ps[4]],
    ) = np.percentile(Tglob_gt[scen], ps, axis=0)

joblib.dump(perc_Tglob_gt, dir_median + "perc_median_forced_global.pkl")

# ATTENTION: KYOTOGHGem_all_scens contains more scens than Tglob_all_scens
# because some individual emitter removed scens are required for the emission plot in Fig. 1
