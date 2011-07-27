import getopt, os, sys
"""
This script processes an opencompute multimarkdown file and converts it into a multipage pdf

yael@fb.com

"""

repos=["",""]

def sync(path, url, repo_name):
    p = os.path.join(path, repo_name) + ".git"
    print("Synching %s -> %s" % (repo_name, p))
    if not os.path.exists(p):
          subprocess.call(['git','clone',url,p])

if __name__ == "__main__":
  try:
    opts, args = getopt.getopt(sys.argv[1:],"f:hg",["file","help","git"])
  except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(2)

  mmdcmd='mmd2tex '
  pdfcmd='xelatex -interaction=batchmode '

  for o, a in opts:
    if o in ("-f","--file"):
      fname=a
    elif o in ("-h","--help"):
      usage()
      sys.exit()

  # make sure images are present as symlinks in the image directory
  lnames = ['OCPlogo_horiz.png','OCPlogo_vert.png']
  for l in lnames:
      if os.access('../../spec/images/'+l,os.F_OK) is False:
          os.symlink('../../spec/images/'+l,'../images/l')

  # first convert mmd to latex
  print(mmdcmd+fname)
  os.system(mmdcmd+fname)

  # second, convert latex to pdf
  file, ext = os.path.splitext(fname)
  print(pdfcmd+file+'.tex')
  os.system(pdfcmd+file+'.tex')
