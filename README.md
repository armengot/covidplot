# covidplot
Single data plot of COVID19 cases (or deaths) for specific country.

# Usage:
Single script to download data from: [covid.ourworldindata.org](https://covid.ourworldindata.org/data/owid-covid-data.csv) and plot a specific country data.
```
$ ./covidplot.py Spain
```
It plots two graphics (cases and deaths). Ready to be saved as PNG.

# Examples

![Spain cases plot](https://github.com/armengot/covidplot/blob/main/spain_cases_sample.png)
![Spain deaths plot](https://github.com/armengot/covidplot/blob/main/spain_deaths_sample.png)

# HELP

## Don't forget
Remove local .csv files downloaded.

## What is the tag of my country?
The source data is downloaded from [covid.ourworldindata.org](https://covid.ourworldindata.org/data/owid-covid-data.csv) in a csv file.
After the first run of the script you can access and look for the specific tag, some countries need quotes.
```
$ ./covidplot.py "United States"
```

## Requirements
The script is written under a GNU/Linux system but if you are using Windows you will probably be able to (run)[https://realpython.com/run-python-scripts/#using-the-script-filename] it too.

# License

Marcelo Armengot (C) 2022
[GNU/GPL](https://www.gnu.org/licenses/gpl-3.0.html)