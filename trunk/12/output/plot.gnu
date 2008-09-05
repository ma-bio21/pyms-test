# plot.gnu
#
# Usage:
#     $ gnuplot plot.gnu
#

set term post eps
set output 'tic_sg_smoothed.eps'

set xrange [6.0:8.0]
set yrange [0:1e6]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic.dat' using 1:2 notitle w l,\
     'tic1.dat' using 1:2 notitle w l

