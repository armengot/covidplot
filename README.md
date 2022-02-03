# covidplot
Single data plot of COVID19 cases (or deaths) for specific country.

# Usage:
Single script to download data from: https://covid.ourworldindata.org/data and plot a specific country data.
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
After the first run of the script you can access an look for the specific tag, some countries need quotes.
```
$ ./covidplot.py "United States"
```
# License

Marcelo Armengot (C) 2022
[GNU/GPL](https://www.gnu.org/licenses/gpl-3.0.html)