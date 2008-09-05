# plot.gnu
#
# Usage:
#     $ gnuplot plot.gnu
#

set term post eps
set output 'tic.eps'

set xrange [5.0:20.0]
set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic.dat' using 1:2 notitle w l

