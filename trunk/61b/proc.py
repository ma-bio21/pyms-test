"""proc.py
"""

import sys, os
sys.path.append("/x/PyMS")

from pyms.GCMS.IO.ANDI.Function import ANDI_reader
from pyms.GCMS.Function import build_intensity_matrix_i
from pyms.Noise.SavitzkyGolay import savitzky_golay
from pyms.Baseline.TopHat import tophat
from pyms.Peak.Class import Peak
from pyms.Peak.Function import peak_sum_area

from pyms.Deconvolution.BillerBiemann.Function import BillerBiemann, \
    rel_threshold, num_ions_threshold

from pyms.Experiment.Class import Experiment
from pyms.Experiment.IO import store_expr


# define path to data files
base_path = "/x/PyMS/data/"

# define experiments to process
expr_codes = [ "a0806_140", "a0806_141", "a0806_142" ]

# deconvolution and peak list filtering parameters
points = 9; scans = 2; n = 3; t = 2000; r = 2;

# loop over all experiments
for expr_code in expr_codes:

    print "Processing", expr_code

    # define the names of the peak file and the corresponding ANDI-MS file
    andi_file = os.path.join(base_path, expr_code + ".cdf")

    data = ANDI_reader(andi_file)

    im = build_intensity_matrix_i(data)

    # get the size of the intensity matrix
    n_scan, n_mz = im.get_size()

    # smooth data
    for ii in range(n_mz):
        ic = im.get_ic_at_index(ii)
        ic1 = savitzky_golay(ic)
        ic_smooth = savitzky_golay(ic1)
        ic_base = tophat(ic_smooth, struct="1.5m")
        im.set_ic_at_index(ii, ic_base)

    # do peak detection on pre-trimmed data

    # get the list of Peak objects
    pl = BillerBiemann(im, points, scans)

    # trim by relative intensity
    apl = rel_threshold(pl, r)

    # trim by threshold
    peak_list = num_ions_threshold(apl, n, t)

    print "Number of Peaks found:", len(peak_list)

    # ignore TMS ions and use same mass range for all experiments
    for peak in peak_list:
        peak.crop_mass(50,540)
        peak.null_mass(73)
        peak.null_mass(147)
        # find area
        area = peak_sum_area(im, peak)
        peak.set_area(area)

    # create an experiment
    expr = Experiment(expr_code, peak_list)

    # use same time range for all experiments
    expr.sele_rt_range(["6.5m", "21m"])

    store_expr("output/"+expr_code+".expr", expr)
