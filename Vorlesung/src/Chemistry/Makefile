.PHONY:clean
test:
	@data_matrix_main.py -s '	' -o  atom-data.tsv | sort > atom-data-tmp.tsv
	@sort atom-data.tsv | diff - atom-data-tmp.tsv
	@${RM} atom-data-tmp.tsv
	@data_matrix_main.py -s '	' -k H He Li -a atomicNumber symbol name meltingPoint -o atom-data.tsv | sort > atom-data-tmp.tsv
	@sort atom-data-mini.tsv | diff -w - atom-data-tmp.tsv
	@${RM} atom-data-tmp.tsv

.PHONY:clean
clean:
	@${RM} -r __pycache__	
