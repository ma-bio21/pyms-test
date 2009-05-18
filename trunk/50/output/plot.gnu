# plot.gnu
#
# Gnuplot script to plot 'tic.dat' and 'tic1.dat'
#
# Usage:
#     $ gnuplot plot.gnu
#

set term post eps
set output 'ic51_mean_smoothed.eps'

set xrange [7.0:12.0]
set yrange [0:1.0e4]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'ic51_mean5.dat' using 1:2 notitle w l,\
     'ic51.dat' using 1:2 notitle w l

set term post eps
set output 'ic51_median_smoothed.eps'

set xrange [7.0:8.0]
set yrange [0:0.8e3]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'ic51_median5.dat' using 1:2 notitle w l,\
     'ic51.dat' using 1:2 notitle w l


