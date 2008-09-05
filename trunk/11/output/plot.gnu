# plot.gnu
#
# Gnuplot script to plot 'tic.dat' and 'tic1.dat'
#
# Usage:
#     $ gnuplot plot.gnu
#

set term post eps
set output 'tic_mean_smoothed.eps'

set xrange [6.0:8.0]
set yrange [0:1.0e6]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic1.dat' using 1:2 notitle w l,\
     'tic.dat' using 1:2 notitle w l

set term post eps
set output 'tic_median_smoothed.eps'

set xrange [6.0:8.0]
set yrange [0:1.0e6]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic2.dat' using 1:2 notitle w l,\
     'tic.dat' using 1:2 notitle w l


