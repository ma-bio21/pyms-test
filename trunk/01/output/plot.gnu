# plot.gnu
#
# Gnuplot script to plot 'tic.dat'
#
# Usage:
#     $ gnuplot plot.gnu
#
# The plot will be saved as 'tic.eps'
#

set term post eps
set output 'tic.eps'

set xrange [5.0:20.0]
set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic.dat' using 1:2 notitle w l



