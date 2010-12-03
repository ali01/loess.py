# vim: ft=make
.PHONY: report._graphics
report.aux report.aux.make report.d report.pdf: /usr/local/texlive/2009/texmf-dist/tex/latex/base/article.cls
report.aux report.aux.make report.d report.pdf: /usr/local/texlive/2009/texmf-dist/tex/latex/graphics/epsfig.sty
report.aux report.aux.make report.d report.pdf: /usr/local/texlive/2009/texmf-dist/tex/latex/graphics/graphics.sty
report.aux report.aux.make report.d report.pdf: /usr/local/texlive/2009/texmf-dist/tex/latex/graphics/graphicx.sty
report.aux report.aux.make report.d report.pdf: /usr/local/texlive/2009/texmf-dist/tex/latex/graphics/keyval.sty
report.aux report.aux.make report.d report.pdf: /usr/local/texlive/2009/texmf-dist/tex/latex/graphics/trig.sty
report.aux report.aux.make report.d report.pdf: /usr/local/texlive/2009/texmf-dist/tex/latex/ltxmisc/endnotes.sty
report.aux report.aux.make report.d report.pdf: /usr/local/texlive/2009/texmf-dist/tex/latex/psnfss/times.sty
report.aux report.aux.make report.d report.pdf: report.tex
report.aux report.aux.make report.d report.pdf: usenix.sty
.SECONDEXPANSION:
report.bbl report.aux report.aux.make: ./references.bib
