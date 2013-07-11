This is an example of the scalability using a small probabilistic ash model with 40 wind fields as example. These are the best timings obtained from a range of runs below. We use the best timings because that is closest to what the hardware is capable of delivering irrespective of network congestion or other disturbances.


#Cores      Time (s)   Speedup  Parallel Efficiency
======      ========   =======  ===================
1
2           4742
5           1924
10          1060
20          539
40          356


The observed scalability is good and consistent with what is expected from Python-FALL3D.



Raw timings
===========

These are observations from runs using the unix command `time` as in::
    
    time mpirun -np 40 -x FALL3DHOME -x PYTHONPATH -hostfile /etc/mpihosts python guntur_multiple_wind.py
    
1 core
------

2 cores
-------

real	79m1.637s
user	0m0.060s
sys	0m0.104s
(4741.634)


5 cores
-------
real	32m4.291s
user	0m0.056s
sys	0m0.056s
(1924.291)

10 cores
--------
real	17m41.547s
user	0m0.064s
sys	0m0.040s

real	17m40.270s
user	0m0.068s
sys	0m0.052s
(1060.270 s)


20 cores
--------
real	9m0.656s
user	0m0.060s
sys	0m0.064s

real	8m58.755s
user	0m0.116s
sys	0m0.032s

real	8m58.665s
user	0m0.100s
sys	0m0.024s
(538.665)

40 cores
--------
real	5m56.225s
user	0m0.164s
sys	0m0.084s
(356.225)

real	6m8.831s
user	0m0.176s
sys	0m0.064s

real	6m1.748s
user	0m0.164s
sys	0m0.084s

real	5m59.188s
user	0m0.164s
sys	0m0.060s
