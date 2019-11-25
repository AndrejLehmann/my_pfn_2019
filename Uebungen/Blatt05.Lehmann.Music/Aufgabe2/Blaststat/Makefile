.PHONY:test
test:
	@./blaststat.py blaststat.txt | diff - blaststat_output.txt
	@./check_err.py
	@echo "Congratulations: test passed!"
