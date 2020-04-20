.PHONY:test
test:
	@./predictionqual.py --gold_standard goldstandard.tsv prediction[0-9]*.tsv | diff - quality-out.tsv
	@echo "Congratulations. Tests passed"
