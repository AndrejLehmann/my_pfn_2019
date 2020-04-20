#!/usr/bin/env python3

import argparse

def parse_arguments():
  p = argparse.ArgumentParser(description='output boxbplot in tikz')
  p.add_argument('-m','--minimal',action='store_true',default=False,
                  help='show minimal version of boxplot')
  p.add_argument('--header',action='store_true',default=False,
                  help='output with header')
  return p.parse_args()

args = parse_arguments()

if args.header:
  print(r'''\documentclass[english]{beamer}
\usepackage{tikz}
\usetikzlibrary{snakes}
\begin{document}
\begin{frame}[fragile,allowframebreaks]{}
\begin{center}''')

print(r'''% Author: Sivaram Neelakantan
% from http://www.texample.net/tikz/examples/box-and-whisker-plot/
\begin{tikzpicture}[thick]
    \filldraw[fill=black!5] (2,0) rectangle (5,1);% draw the box
    \draw (7,0.39) -- (7,0.61);% draw vertical tab
    \draw (1,0.39) -- (1,0.61);% draw vertical tab
    \node[below] at (8,0.7) {$o$}; % mild outlier on the right
    \node[below] at (-1.4,0.7) {$o$}; % extreme outlier on the left
    % Axis
    \draw (-2.5,1.2) -- (8.5,1.2);
    % Note that the snaked line is drawn to 11.1 to force
    % TikZ to draw the final tick.
    \draw[snake=ticks,segment length=1cm] (-2.5,1.2) -- (8.5,1.2);
''')
if args.minimal:
  print(r'''\draw[red] (3,0) -- (3,1);% draw the median
    \draw (5,0.5) -- (7,0.5);% draw right whisker
    \draw (2,0.5) -- (1,0.5);% draw left whisker''')
else:
  print(r'''\draw[red] (3,0) -- (3,1) node[yshift=-3pt] {median};
    \draw (5,0.5) -- (7,0.5) node[pos=0.5,above] {\footnotesize whisker};
    \draw (2,0.5) -- (1,0.5) node[pos=0.5,above] {\footnotesize whisker};
    \node[below] at (2,0.24) %
             {\begin{tabular}{c}
                    {\small lower}\\[-3pt]
                    {\small quartile}\\[-3pt]
                    \(Q_{1}\)
               \end{tabular}};% label the hinge
    \node[below] at (5,0.27) %
             {\begin{tabular}{c}
                    {\small upper}\\[-3pt]
                    {\small quartile}\\[-3pt]
                    \(Q_{3}\)
               \end{tabular}};% label the hinge
    \node[below] at (8,0.5) {\footnotesize outlier};
    \node[below] at (-1.4,0.5) {\footnotesize outlier};
    % label the hinge
    \filldraw[ball color=red!80,shading=ball] (4,0.5) circle
        (0.06cm) node[above]{$\bar{x}$};% the mean
    \draw[thin,<->] (2.01, -0.3) -- (4.97, -0.3)
        node (IQR) [pos=0.5,yshift=-5pt] %
             {\begin{tabular}{c}
                    {\scriptsize inter quartile}\\[-4pt]
                    {\scriptsize range \textit{IQR}}\\[-4pt]
                    \(\scriptstyle =Q_{3}-Q_{1}\)
               \end{tabular}};% label the hinge
    \node (IQ1) [below of=IQR,yshift=-24pt]{
         \(\scriptstyle \begin{array}{l@{~}c@{~}l}
           Q_{1}&=&\text{median of values smaller than {\color{red}median}}\\
           Q_{3}&=&\text{median of values larger than {\color{red}median}}\\
           \multicolumn{3}{l}{\text{left whisker:}<Q_{1};
                              \text{right whisker:}>Q_{3}\text{, both except outliers}}\\
           \multicolumn{3}{l}{\text{outlier:} <Q_{1}-(1.5\cdot\mathit{IQR})\mbox{ or }
                           >Q_{3}+(1.5\cdot\mathit{IQR})}\\[9pt]
  \multicolumn{3}{c}{\text{adapted from }
    \text{http://www.texample.net/tikz/examples/box-and-whisker-plot/}}
          \end{array}\)};
               % mark the IQR fences
    %\draw[<->] (2, -0.8) -- (0,-0.8)
        %node[pos=0.5,below]{$\textsc{1.5*IQR}$}; % left inner fence
    %\draw[<->] (2,-1.4) -- (-2, -1.4)
        %node[pos=0.5,below]{$\textsc{3*IQR}$};% left outer fence
    %\draw[<->] (5, -0.8) -- (8,-0.8)
        %node[midway,below]{$\textsc{1.5*IQR}$}; % right inner fence
    %\draw[<->] (5,-1.4) -- (10, -1.4)
        %node[pos=0.5,below]{$\textsc{3*IQR}$};% right outer fence
    %
    % Title
    %\draw (3,2) node[above,yshift=-10pt,xshift=0.7cm]{Box and Whisker Plot};''')


print(r'\end{tikzpicture}')
if args.header:
  print(r'''\end{center}
\end{frame}
\end{document}''')
