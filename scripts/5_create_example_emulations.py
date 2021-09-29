# add pathway to folders 1 level higher (i.e., to configs)
import sys

sys.path.append("../")

import joblib
import numpy as np

# load in configurations used in this script
import configs.config_major_emitters_cmip5ng_rcpall_default as cfg

# import MESMER tools
from mesmer.io import load_mesmer_output

# cfgs info
dir_magicc = cfg.dir_magicc
dir_samples = cfg.dir_sample_emulations
esms = cfg.esms

# load in all Tglob
Tglob_gt = joblib.load(dir_magicc + "Tglob_gt_all_scens.pkl")
nr_gt_trajs, nr_ts = Tglob_gt["h-NDC"].shape

# load in example emus_lv
emus_lv = load_mesmer_output("emus_lv", cfg, esm_str=esms[0])
nr_gps = emus_lv["all"]["tas"].shape[-1]

# create and save sample emulations for Figure S1
i = 0
emus = np.zeros([nr_gt_trajs, nr_ts, nr_gps])

for esm in esms:
    print("start with ESM", esm)
    # load in params lt
    params_lt = load_mesmer_output("params_lt", cfg, esm_str=esm)
    # load in emus_lv
    emus_lv = load_mesmer_output("emus_lv", cfg, esm_str=esm)
    # derive emus: combine params_lt with Tglob_gt and emus_lv
    # ATTENTION: assumes 6000 Tglob_gt, 40 ESMs involved, 6000 emus_lv each
    # (otherwise step sizes would need to be adapted)
    for nr_gp in np.arange(nr_gps):
        emus[i::40, :, nr_gp] = (
            params_lt["coef_gttas"]["tas"][nr_gp] * Tglob_gt["h-NDC"][i::40]
            + params_lt["intercept"]["tas"][nr_gp]
            + emus_lv["all"]["tas"][i::400, :, nr_gp]
        )

    i += 1

joblib.dump(emus, dir_samples + "sample_emus.pkl")
