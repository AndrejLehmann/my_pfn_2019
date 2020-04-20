.PHONY:test
test:${wildcard *.py}
	@./generate-test.rb py | sh -s

.PHONY:
clean:
	@${RM} countbasepython tmpfile
	@${RM} -r __pycache__
