.PHONY:test
test:
	@./data_matrix_class.py -s '	' -o  atom-data.tsv | sort > atom-data-tmp.tsv
	@sort atom-data.tsv | diff - atom-data-tmp.tsv
	@rm -f atom-data-tmp.tsv
	@./data_matrix_class.py -s '	' -k H He Li -a atomicNumber symbol name meltingPoint -o atom-data.tsv | sort > atom-data-tmp.tsv
	@sort atom-data-mini.tsv | diff -w - atom-data-tmp.tsv
	@rm -f atom-data-tmp.tsv
	@echo "Congratulations. Tests passed"
