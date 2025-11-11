from numpy import *
from matplotlib.pyplot import *

x = arange([1, 2, 3, 4, 5, 6])
plot( x ,x , x ,x  )
xlabel( r'$x$' )
ylabel( r'$f(x)$' )
title( r'$f_1(x)=\,\ f_2(x)=\,\ f_3(x)=$' )
grid( True )
show( )
