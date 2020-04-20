.PHONY:test

whisker:mk_boxwhisker.py
	./mk_boxwhisker.py > boxwhisker.tex
	./mk_boxwhisker.py --minimal > boxwhisker_minimal.tex

test:test-plot test-plot-pd

test-plot:
	@for arg in std scatter hist boxp ysub; do \
		echo $$arg;\
		./time_series.py --$$arg;\
	done
	@./time_series.py --year 2017

test-plot-pd:
	@for arg in std scatter hist hsmth boxp ysub heat lag acor; do \
		echo $$arg;\
		./temp_plot_pd.py --$$arg;\
	done
	@./temp_plot_pd.py --year 2010

.PHONY:clean
clean:
	rm -f temp_pd.pdf
	git checkout `find . -newer temp_violinplot.pdf -name '*.pdf'`
	@${RM} -r __pycache__
