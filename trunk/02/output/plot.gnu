# plot.gnu
#
# Gnuplot script to plot 'ms.dat'
#
# Usage:
#     $ gnuplot plot.gnu
#
# The plot will be saved as 'ms.eps'
#

set term post eps
set output 'ms.eps'

set xrange [0:500]
set xlabel 'm/z'
set ylabel 'Intensity'

plot 'ms.dat' with impulses notitle

