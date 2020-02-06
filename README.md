# cmpe273-lab1

To run this:
1) Clone the repo.
2) Run the python files.

Note::

With the input files given, async is slower as it's own overhead. For smaller files async is actually slower. The times are listed below.

```
time python3 ext_merge_sort.py 

real	0m0.035s
user	0m0.019s
sys	0m0.010s

time python3 async_ext_merge_sort.py 

real	0m0.099s
user	0m0.064s
sys	0m0.020s
```

To simulate large files, sleep(0.1) has been introduced to prove that async is faster. With this the times are as follows

```
time python3 ext_merge_sort.py 

real	0m1.067s
user	0m0.020s
sys	0m0.009s

time python3 async_ext_merge_sort.py 

real	0m0.183s
user	0m0.061s
sys	0m0.017s
```
