# Alpha

This is a project to convert multimarkdown spec files into multi-page pdfs. This is currently designed around the script gitmmd2pdf.py

## gitmmd2pdf.py

This is a script which converts a multimarkdown file into a multi-page pdf to serve from opencompute.org

Within the <project>/spec directory:

    ../../alpha/gitmg2pdf.py -f <spec file>

## Requirements

You need [xelatex](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=xetex) installed on your system, with all the latex extras.

In this directory are the following modified files:

    mmd-memoir-packages.tex
    mmd-article-begin-doc.tex
    mmd-article-header.tex
   
## Fonts

The script needs the VistaSlabReg and VistaSlabAltReg TrueType fonts installed.

## Latex packages

The list of latex packages required are:

