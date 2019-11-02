.PHONY:test

FILES=references.txt aligned_only.sam references_count.tsv \
			reads_n_alignments.tsv reads_n_alignments_distri.tsv

test:
	./sam.sh
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
	${RM} ${FILES}
