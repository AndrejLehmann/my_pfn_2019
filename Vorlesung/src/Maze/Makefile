.PHONY:all
all:neighbors maze_gray17_5.tex maze_bin.tex\
    maze_all maze_shortest11_13 \
    maze_shortest11_13.tex maze_shortest2_5.tex maze_shortest17_5.tex \
    maze_some17_5.tex \
    maze_gray_small_origin.tex  \
    maze_gray_small_dot.tex

neighbors:
	maze.py -n '(2,5)'

maze_gray17_5.tex:maze.py
	maze.py -g '(17,5)' --noheader > $@

maze_gray_small_origin.tex:maze.py
	maze.py -g --scale 0.21 --origin --noheader > $@

maze_gray_small_dot.tex:maze.py
	maze.py -g '(17,5)' --scale 0.24 --noheader > $@

maze_some17_5.tex:maze.py
	maze.py -g --scale 0.24 --somepath '(17,5)/0' --noheader > $@

maze_bin.tex:maze.py
	maze.py --noheader -b --origin --scale 0.21 > $@

maze_shortest11_13.tex:maze.py
	maze.py --noheader -g -s '(11,13)' > $@

maze_shortest2_5.tex:maze.py
	maze.py --noheader -g -s '(2,5)' > $@

maze_shortest17_5.tex:maze.py
	maze.py --noheader -g -s '(17,5)' --scale 0.24  > $@

maze_all:maze.py
	maze.py -a '(8,11)'

maze_shortest:maze.py
	maze.py -s

maze_shortest11_13:maze.py
	maze.py --noheader -s '(11,13)'

%.pdf:%.tex
	pdflatex $<

clean:
	${RM} maze_tmp*.pdf maze_tmp*.aux maze_tmp*.nav 
	${RM} maze_tmp*.snm maze_tmp*.out maze_tmp*.log maze_tmp*.toc
	${RM} maze_shortest11_13.tex maze_shortest2_5.tex
