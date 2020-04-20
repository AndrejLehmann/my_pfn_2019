.PHONY:test

test:
	@./restriction.py Ath.fna AccI Afl83II | grep -v '^parsed' | diff - result.txt
	@./restriction_class.py Ath.fna AccI Afl83II | diff - result.txt

.PHONY:clean
clean:
	@${RM} -r __pycache__
