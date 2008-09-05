# plot.gnu
#
# Usage:
#     $ gnuplot plot.gnu
#

set term post eps
set output 'ms.eps'

set xrange [0:500]
set xlabel 'm/z'
set ylabel 'Intensity'

plot 'ms.dat' with impulses notitle

