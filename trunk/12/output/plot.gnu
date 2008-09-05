# plot.gnu
#
# Usage:
#     $ gnuplot plot.gnu
#

set term post eps
set output 'tic_bc_tophat.eps'

set xrange [5.0:20.0]
set yrange [0:2e6]

set xlabel 'retentione time [min]'
set ylabel 'Intensity'

plot 'tic_bc.dat' using 1:2 notitle w l,\
     'tic.dat' using 1:2 notitle w l

