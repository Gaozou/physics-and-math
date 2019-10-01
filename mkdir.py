import sys
import os
from pathlib import Path
import shutil

TEMPLATE_PATH = Path(r"C:\Users\yugo9\Documents\Scripts\TeX Scripts\数物メモ\template.tex")
PREAMBLE_PATH = Path(r"C:\Users\yugo9\Documents\Scripts\TeX Scripts\数物メモ\preamble.tex")

def main():
	if len(sys.argv)<2:
		print("Error: specify the directory you are making.")
		exit()
	
	dirpath = Path(sys.argv[1])
	
	# check validity of arg
	if dirpath.exists():
		print("Error: the directory already exists.")
		exit()
	else:
		os.makedirs(dirpath)

	filename = dirpath.name + '.tex'
	filepath = dirpath / filename

	shutil.copy(str(TEMPLATE_PATH), str(filepath) )
	shutil.copy(str(PREAMBLE_PATH), str(dirpath / "preamble.tex"))


if __name__ == "__main__":
	main()