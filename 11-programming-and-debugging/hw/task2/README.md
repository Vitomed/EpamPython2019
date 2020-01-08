# strace и профилирование


1)cProfiler

```
				cProfile.run("main(p,s)")
```

ncalls – это количество совершенных вызовов;

tottime – это все время, потраченное в данной функции;

percall – ссылается на коэффициент tottime, деленный на ncalls;

cumtime – совокупное время, потраченное как в данной функции, так и наследуемых функциях.

Второй столбец percall – это коэффициент cumtime деленный на примитивные вызовы;

filename:lineno(function) предоставляет соответствующие данные о каждой функции.
```
	ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	1228    1.127    0.001    1.127    0.001 {built-in method _hashlib.openssl_sha256}
	1229    0.217    0.000    0.217    0.000 {method 'read' of '_io.BufferedReader' objects}
	   1    0.000    0.000    1.581    1.581 {built-in method builtins.exec}
	   1    0.028    0.028    1.581    1.581 profiler.py:13(walker_path)
	   1    0.000    0.000    1.581    1.581 profiler.py:28(main)
	1228    0.034    0.000    1.430    0.001 profiler.py:7(get_hash_file)
	1594    0.005    0.000    0.005    0.000 {built-in method posix.fspath}
```

2) strace

```
				strace -c  python3 profiler.py
```

```
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 78.68    0.248705          95      2619           read
  4.48    0.014165           9      1527         2 open
  4.43    0.013998           5      2842           fstat64
  3.77    0.011924           5      2551         6 _llseek
  2.88    0.009093           6      1528           close
  2.09    0.006593          17       392           getdents64
  1.92    0.006065           5      1244      1232 ioctl
  0.54    0.001703           4       384        58 stat64
```

## Вывод:
```
*Системный вызов, который был вызван чаще всего - 
		{built-in method posix.fspath}(Return the file system representation of the path)

*Самый горячий участок кода - функция walker_path

*Системный вызов, который потребил больше всего времени - read чтение файла
```






