.PHONY:test
test:checkall.sh ${wildcard *.py}
	./checkall.sh py
	./gbMultiseq.py Library.gb | diff - Library.fasta

.PHONY:clean
clean:
	${RM} -r __pycache__
