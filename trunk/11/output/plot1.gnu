# plot1.gnu
#
# Gnuplot script to plot 'tic.dat' and 'tic1.dat'
#
# Usage:
#     $ gnuplot plot1.gnu
#
# The plot will be saved as 'tic_mean_smoothed.eps'
#

set term post eps
set output 'tic_mean_smoothed.eps'

set xrange [6.3:7.0]
set yrange [0:1.5e6]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic.dat' using 1:2 notitle w l,\
     'tic1.dat' using 1:2 notitle w l



