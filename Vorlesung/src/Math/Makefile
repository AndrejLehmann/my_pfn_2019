CC?=gcc
LD=${CC}
CFLAGS=-Wall -Werror -O3 -m64
LDFLAGS=-m64 -lm

all:test

test:approx_integral.py multisets.py
	@./approx_integral.py -m 100000 | diff - integral-out.txt
	@./multisets.py -r 3 -q 4
	@./multisets.py -r 3 -q 5
	@./multisets.py -r 3 -q 4 --str
	@./multisets.py -r 20

%.x:%.o
	${LD} ${LDFLAGS} -o $@ $<

.PHONY:clean
clean:
	${RM} -r __pycache__
