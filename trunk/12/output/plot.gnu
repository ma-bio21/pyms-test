# plot.gnu
#
# Gnuplot script to plot 'tic2.dat'
#
# Usage:
#     $ gnuplot plot.gnu
#
# The plot will be saved as 'tic_tophat.eps'
#

set term post eps
set output 'tic_tophat.eps'

set xrange [5.0:20.0]
set yrange [0:2e6]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic.dat' using 1:2 notitle w l,\
     'tic2.dat' using 1:2 notitle w l

