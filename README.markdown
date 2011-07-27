# Open Compute Projects

Welcome to our beta Git repository. In it you will find specs in multimarkdown for our Intel and AMD V2 motherboards. Mechanical CAD files will be forthcoming. We also have a small project, called alpha, for converting multimarkdown specs into multi-page pdfs. It is non-functional until the instructions for installing all the latex tools are documented.

One thing to note: the OCP logos for html and PDF generation are in /alpha/images. You will need to manually symlink the images in there to a particular project's images folder. the gitmmd2pdf.py script will do this for you, but this script won't generate nice output or compile unless you have all the latex tools installed.