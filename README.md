[![Format](https://github.com/dani-jimlar/djl_ind_project_1/actions/workflows/format.yml/badge.svg)](https://github.com/dani-jimlar/djl_ind_project_1/actions/workflows/format.yml)
[![Lint](https://github.com/dani-jimlar/djl_ind_project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/dani-jimlar/djl_ind_project_1/actions/workflows/lint.yml)
[![Install](https://github.com/dani-jimlar/djl_ind_project_1/actions/workflows/install.yml/badge.svg)](https://github.com/dani-jimlar/djl_ind_project_1/actions/workflows/install.yml)
[![Test](https://github.com/dani-jimlar/djl_ind_project_1/actions/workflows/test.yml/badge.svg)](https://github.com/dani-jimlar/djl_ind_project_1/actions/workflows/test.yml)



# 2023.706 Data Enigineering. Project 1

## Demo video
- https://youtu.be/1nETtCDdkvU

## Repo structure
- git actions/workflow 
 	- format.yml
  - install.yml
  - lint.yml
  - test.yml
- source (contains a scrpit and jupyter notebook that use functions from the lib.py file to perform data anayisis)
  - bar_plot2.png
  - imp_edos_2.csv
  - lib.py
  - my_notebook.ipnyb
  - script.py
  - test_lib.py
  - test_script.py
 - Makefile
 - requirements.txt
## Code description for lib file
In this project several functions are used to descirbe the data from a csv file and were defined in the lib.py file.
One function prints the descriptive statistcs using pandas describe():
- mean 
- median
- standard deviation
- min value
- max value
- first qt
- second qt
- third qt


Two functions are used for data visualizations:
Both functions make a barplot from a two selected variables using seaborn and matplotlib, one function saves it as a png image and the other just shows the image.


