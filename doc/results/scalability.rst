This is an example of the scalability using a small probabilistic ash model with 40 wind fields as example. These are the best timings obtained from a range of runs below. We use the best timings because that is closest to what the hardware is capable of delivering irrespective of network congestion or other disturbances.


#Cores      Time (s)   Speedup  Parallel Efficiency (%)
======      ========   =======  =======================
1           9505        1.00    100.0 
2           4742        2.00    100.0
5           1924        4.94     98.8
10          1060        8.97     89.7 
20          539        17.63     88.15
40          356        26.70     66.75


The observed scalability is good and consistent with what is expected from Python-FALL3D. As is usually the case with speedup for a fixed sized problem, the parallel efficiency drops as the number of cores is increased. This is due to communication overheads, the time it takes to initialise the run, overheads of cores sharing resources (bus, disk, cpu, memory, etc), difficulty in load balancing increasingly smaller chunks of work etc. 
Having said that, a parallel efficiency exceeding 60% is generally regarded as feasible. 



Raw timings
===========

These are observations from runs using the unix command `time` as in::
    
    time mpirun -np 40 -x FALL3DHOME -x PYTHONPATH -hostfile /etc/mpihosts python guntur_multiple_wind.py
    
1 core
------

real158m25.044s
user0m0.072s
sys0m0.176s
(9505.044s)


2 cores
-------

real	79m1.637s
user	0m0.060s
sys	0m0.104s
(4741.634s)


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
(1060.270s)


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
(538.665s)


30 cores
--------

real9m2.250s
user0m0.168s
sys0m0.056s
(542.25s)

Need one more timing!

40 cores
--------
real	5m56.225s
user	0m0.164s
sys	0m0.084s
(356.225s)

real	6m8.831s
user	0m0.176s
sys	0m0.064s

real	6m1.748s
user	0m0.164s
sys	0m0.084s

real	5m59.188s
user	0m0.164s
sys	0m0.060s
