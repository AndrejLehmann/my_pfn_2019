.PHONY:test
FILES=hypo.tsv nothypo.tsv locus.tsv ranges.tsv

test:
	./tsv.sh
	@for file in ${FILES}; do \
		echo "-- $$file"; \
		diff $$file $$file.solution; \
		if [ $$? -eq 0 ]; then \
		  echo "..... OK"; \
		else \
			exit 1;\
		fi;\
  	done
	@echo "Congratulations: Test passed!"

clean:
	${RM} ${FILES} nohead.tsv
