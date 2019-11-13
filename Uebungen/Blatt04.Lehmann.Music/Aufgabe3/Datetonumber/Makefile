.PHONY:test
test:
	@./datetonumber.py randomdates.csv | diff - randomdates-numbered.csv
	@./check_err.py
	@echo "Congratulations: test passed!"
