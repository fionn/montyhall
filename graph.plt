#!/usr/bin/gnuplot

set term png font "Helvetica"
set output "montyhall.png"

set xlabel "Games"
set ylabel "Percentage won"

set yrange[0:100]

plot "winloose1.dat" using 1:2 w l lt 3 notitle, "winloose2.dat" w l lt 5 notitle, "winloose3.dat" w l lt 8 notitle, 66.666 w l lt 0 notitle, "winloose1.dat" using 1:3 w l lt 3 notitle, "winloose2.dat" using 1:3 w l lt 5 notitle, "winloose3.dat" using 1:3 w l lt 8 notitle, 66.666 w l lt 0 notitle, 33.333 w l lt 0 notitle

