.PHONY:test
test:data test-tsv test-country_list test-histogram test-boxplot
	@echo "Congratulations. Tests passed."

.PHONY:data
data:
	@bzip2 -d -c CO2ausstoss.html.bz2 > CO2ausstoss.html

.PHONY:test-tsv
test-tsv:data
	@./co2_stat_mn.py --tsv CO2ausstoss.html | diff - CO2ausstoss.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test-country_list
test-country_list:data
	@./create_plot.sh developing CO2ausstoss.tsv
	@./create_plot.sh middle_european CO2ausstoss.tsv
	@./create_plot.sh worst CO2ausstoss.tsv
	@./create_plot.sh big CO2ausstoss.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test-histogram
test-histogram:data
	@./create_plot.sh histogram CO2ausstoss.tsv
	@echo "Congratulations. $@ passed."

.PHONY:test-boxplot
test-boxplot:data
	@./create_plot.sh boxplot_region CO2ausstoss.tsv
	@./create_plot.sh boxplot_continent CO2ausstoss.tsv
	@echo "Congratulations. $@ passed."

.PHONY:clean
clean:
	@${RM} -r __pycache__
	@find . -newer CO2ausstoss.html -type f -name '*.pdf' -maxdepth 1 | xargs rm -f
