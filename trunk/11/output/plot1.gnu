# plot1.gnu
#
# Gnuplot script to plot 'tic.dat'
#
# Usage:
#     $ gnuplot plot.gnu
#
# The plot will be saved as 'tic.eps'
#

set term post eps
set output 'tic1.eps'

set xrange [6.3:7.0]
set yrange [0:1.5e6]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic.dat' using 1:2 notitle w l,\
     'tic1.dat' using 1:2 notitle w l



