"""
Configuration file for cmip5-ng, tas, hist + all rcps

"""


# ---------------------------------------------------------------------------------

# directories:
basedir = "/your/path/"
basedir_cmip = "/your/cmip/path/"

# cmip-ng
gen = 5  # generations
dir_cmipng = basedir_cmip + "cmip" + str(gen) + "-ng/"

# observations
dir_obs = basedir + "mesmer/data/observations/"

# auxiliary data
dir_aux = basedir + "mesmer/data/auxiliary/"

# MESMER
dir_mesmer_params = basedir + "attrib_emu_T/mesmer/calibrated_parameters/"
dir_mesmer_emus = basedir + "attrib_emu_T/mesmer/emulations/"

# MAGICC
dir_magicc = basedir + "attrib_emu_T/magicc/"
dir_magicc_ref = dir_magicc + "historical-NDC/"
dir_magicc_m = dir_magicc + "minus_top5/"
dir_magicc_pc = dir_magicc + "percap_top5/"

# sample emulations
dir_sample_emulations = basedir + "attrib_emu_T/sample_emulations/"

# emulation statistics
dir_stats = basedir + "attrib_emu_T/statistics/"
dir_stats_median = dir_stats + "median/"
dir_stats_probhy = dir_stats + "probability_hot_year/"


# plots
dir_plots = basedir + "attrib_emu_T/plots/"

# configs that can be set for every run:

# time
time_emus = {}
time_emus["start"] = 1850  # first year included
time_emus["end"] = 2030  # last year included

# statistics
ps = [5, 17, 50, 83, 95]  # percentiles

# emitters
emitters_abs = ["RUS", "IND", "EU", "US", "CHN"]
emitters_pc = ["IND", "EU", "CHN", "RUS", "US"]
title_e_pc = ["India", "EU-27", "China", "Russia", "US"]

# MAGICC
ref_magicc = {}
ref_magicc["type"] = "individ"
ref_magicc["start"] = 1850
ref_magicc["end"] = 1900

scens_magicc_ref = ["h-NDC"]
scens_magicc_m = ["m_top5_Paris", "m_top5_IPCC"]
scens_magicc_pc = [
    "pc_IND_Paris",
    "pc_EU_Paris",
    "pc_CHN_Paris",
    "pc_RUS_Paris",
    "pc_US_Paris",
    "pc_IND_IPCC",
    "pc_EU_IPCC",
    "pc_CHN_IPCC",
    "pc_RUS_IPCC",
    "pc_US_IPCC",
]
scens_magicc_m_se = [
    "m_IND_Paris",
    "m_EU_Paris",
    "m_CHN_Paris",
    "m_RUS_Paris",
    "m_US_Paris",
    "m_IND_IPCC",
    "m_EU_IPCC",
    "m_CHN_IPCC",
    "m_RUS_IPCC",
    "m_US_IPCC",
]

files_magicc_ref = ["SLRA_NDC_reference_2030.nc"]
files_magicc_m = ["SLRA_NDC_TOP5_2016.nc", "SLRA_NDC_TOP5_1991.nc"]
files_magicc_pc = [
    "SLRA_NDC_IND_PerCapCO2_2016.nc",
    "SLRA_NDC_EU27BX_PerCapCO2_2016.nc",
    "SLRA_NDC_CHN_PerCapCO2_2016.nc",
    "SLRA_NDC_RUS_PerCapCO2_2016.nc",
    "SLRA_NDC_USA_PerCapCO2_2016.nc",
    "SLRA_NDC_IND_PerCapCO2_1991.nc",
    "SLRA_NDC_EU27BX_PerCapCO2_1991.nc",
    "SLRA_NDC_CHN_PerCapCO2_1991.nc",
    "SLRA_NDC_RUS_PerCapCO2_1991.nc",
    "SLRA_NDC_USA_PerCapCO2_1991.nc",
]
files_magicc_m_se = [
    "SLRA_NDC_IND_2016.nc",
    "SLRA_NDC_EU27BX_2016.nc",
    "SLRA_NDC_CHN_2016.nc",
    "SLRA_NDC_RUS_2016.nc",
    "SLRA_NDC_USA_2016.nc",
    "SLRA_NDC_IND_1991.nc",
    "SLRA_NDC_EU27BX_1991.nc",
    "SLRA_NDC_CHN_1991.nc",
    "SLRA_NDC_RUS_1991.nc",
    "SLRA_NDC_USA_1991.nc",
]
# must match order of scens_magicc_x!


# ESMs
# esms = ['ACCESS1-0','ACCESS1-3','bcc-csm1-1-m','bcc-csm1-1'] # ch4 screen 1
# esms = ['BNU-ESM','CanESM2','CCSM4','CESM1-BGC'] # ch4 screen 2
# esms = ['CESM1-CAM5','CMCC-CESM','CMCC-CM','CMCC-CMS'] # ch4 screen 3
# esms = ['CNRM-CM5','CSIRO-Mk3-6-0','EC-EARTH','FGOALS-g2'] # ch4 screen 4
# esms = ['FIO-ESM','GFDL-CM3','GFDL-ESM2G','GFDL-ESM2M'] # ch4 screen 5
# esms = ['GISS-E2-H-CC','GISS-E2-H','GISS-E2-R-CC','GISS-E2-R'] # iacdipl-6 screen 1
# esms = ['HadGEM2-AO','HadGEM2-CC','HadGEM2-ES','inmcm4'] # iacdipl-6 screen 2
# esms = ['IPSL-CM5A-LR','IPSL-CM5A-MR','IPSL-CM5B-LR','MIROC5'] # iacdipl-6 screen 3
# esms = ['MIROC-ESM-CHEM','MIROC-ESM','MPI-ESM-LR','MPI-ESM-MR'] # iacdipl-6 screen 4
# esms = ['MRI-CGCM3','MRI-ESM1','NorESM1-ME','NorESM1-M'] # iacdipl-6 screen 5
esms = [
    "ACCESS1-0",
    "ACCESS1-3",
    "bcc-csm1-1-m",
    "bcc-csm1-1",
    "BNU-ESM",
    "CanESM2",
    "CCSM4",
    "CESM1-BGC",
    "CESM1-CAM5",
    "CMCC-CESM",
    "CMCC-CM",
    "CMCC-CMS",
    "CNRM-CM5",
    "CSIRO-Mk3-6-0",
    "EC-EARTH",
    "FGOALS-g2",
    "FIO-ESM",
    "GFDL-CM3",
    "GFDL-ESM2G",
    "GFDL-ESM2M",
    "GISS-E2-H-CC",
    "GISS-E2-H",
    "GISS-E2-R-CC",
    "GISS-E2-R",
    "HadGEM2-AO",
    "HadGEM2-CC",
    "HadGEM2-ES",
    "inmcm4",
    "IPSL-CM5A-LR",
    "IPSL-CM5A-MR",
    "IPSL-CM5B-LR",
    "MIROC5",
    "MIROC-ESM-CHEM",
    "MIROC-ESM",
    "MPI-ESM-LR",
    "MPI-ESM-MR",
    "MRI-CGCM3",
    "MRI-ESM1",
    "NorESM1-ME",
    "NorESM1-M",
]  # all

targs = ["tas"]  # emulated variables

reg_type = "countries"

ref = {}
ref["type"] = "individ"  # alternatives: 'first','all'
ref["start"] = "1870"  # first included year
ref["end"] = "1900"  # last included year

threshold_land = 1 / 3

wgt_scen_tr_eq = True  # if True weigh each scenario equally (ie less weight to individ runs of scens with more ic members)

nr_emus_v = 6000  # trade-off between stable quantiles for individ ESMs and a not too large probab ensemble
scen_seed_offset_v = 0  # 0 meaning same emulations drawn for each scen, if put a number will have different ones for each scen
max_iter_cv = 15  # max. nr of iterations in cross validation

# predictors (for global module)
preds = {}
preds["tas"] = {}  # predictors for the target variable tas
preds["hfds"] = {}
preds["tas"]["gt"] = ["saod"]
preds["hfds"]["gt"] = []
preds["tas"]["gv"] = []
preds["tas"]["g_all"] = preds["tas"]["gt"] + preds["tas"]["gv"]

# methods (for all modules)
methods = {}
methods["tas"] = {}  # methods for the target variable tas
methods["hfds"] = {}
methods["tas"]["gt"] = "LOWESS_OLSVOLC"  # global trend emulation method
methods["hfds"]["gt"] = "LOWESS"
methods["tas"]["gv"] = "AR"  # global variability emulation method
methods["tas"]["lt"] = "OLS"  # local trends emulation method
method_lt_each_gp_sep = True  # method local trends applied to each gp separately
methods["tas"]["lv"] = "OLS_AR1_sci"  # local variability emulation method

# ---------------------------------------------------------------------------------

# configs that should remain untouched:

# full list of esms (to have unique seed for each esm no matter how)
all_esms = [
    "ACCESS1-0",
    "ACCESS1-3",
    "bcc-csm1-1-m",
    "bcc-csm1-1",
    "BNU-ESM",
    "CanESM2",
    "CCSM4",
    "CESM1-BGC",
    "CESM1-CAM5",
    "CMCC-CESM",
    "CMCC-CM",
    "CMCC-CMS",
    "CNRM-CM5",
    "CSIRO-Mk3-6-0",
    "EC-EARTH",
    "FGOALS-g2",
    "FIO-ESM",
    "GFDL-CM3",
    "GFDL-ESM2G",
    "GFDL-ESM2M",
    "GISS-E2-H-CC",
    "GISS-E2-H",
    "GISS-E2-R-CC",
    "GISS-E2-R",
    "HadGEM2-AO",
    "HadGEM2-CC",
    "HadGEM2-ES",
    "inmcm4",
    "IPSL-CM5A-LR",
    "IPSL-CM5A-MR",
    "IPSL-CM5B-LR",
    "MIROC5",
    "MIROC-ESM-CHEM",
    "MIROC-ESM",
    "MPI-ESM-LR",
    "MPI-ESM-MR",
    "MRI-CGCM3",
    "MRI-ESM1",
    "NorESM1-ME",
    "NorESM1-M",
]

# full list of scenarios that could be considered
scenarios = [
    "h-rcp26",
    "h-rcp45",
    "h-rcp60",
    "h-rcp85",
]

if scen_seed_offset_v == 0:
    scenarios_emus_v = ["all"]
else:
    scenarios_emus_v = scenarios

nr_emus = {}
nr_ts_emus_v = {}
seed = {}
i = 0
for esm in all_esms:
    seed[esm] = {}
    j = 0
    for scen in scenarios_emus_v:
        seed[esm][scen] = {}
        seed[esm][scen]["gv"] = i + j * scen_seed_offset_v
        seed[esm][scen]["lv"] = i + j * scen_seed_offset_v + 1000000
        j += 1
    i += 1


# ---------------------------------------------------------------------------------

# information about loaded data:

# cmip-ng
# Data downloaded from ESGF (https://esgf-node.llnl.gov/projects/esgf-llnl/) and pre-processed according to Brunner et al. 2020 (https://doi.org/10.5281/zenodo.3734128)
# assumes folder structure / file name as in cmip-ng archives at ETHZ -> see mesmer.io.load_cmipng.file_finder_cmipng() for details
# - global mean stratospheric AOD, monthly, 1850-"2020" (0 after 2012), downloaded from KNMI climate explorer in August 2020, no pre-processing
