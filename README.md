# README **written by Brandon Lu**
- [README **written by Brandon Lu**](#readme-written-by-brandon-lu)
  - [Final report](#final-report)
  - [TODO](#todo)
      - [Long Lat](#long-lat)
      - [EXEC SUMMARY RN: (**Yvonne**)](#exec-summary-rn-yvonne)
      - [Re-categorization (Jasmine)](#re-categorization-jasmine)
      - [Data website:](#data-website)
      - [Limitaion:](#limitaion)
  - [Repo structure](#repo-structure)
  - [What's next?](#whats-next)
    - [Best case](#best-case)
        - [This will be left to ALL GROUP MEMBERS; I think it's best for all of us to think about what we can do with all this data](#this-will-be-left-to-all-group-members-i-think-its-best-for-all-of-us-to-think-about-what-we-can-do-with-all-this-data)
    - [Worst case](#worst-case)
  - [Apr 12: log](#apr-12-log)
  - [Apr 12: tomorrow plan](#apr-12-tomorrow-plan)
  - [From Apr 11, 2023: 'Add `min_work_ex-before_graph.rmd` and successfully run for two suburbs; Add list; De-clutter the code; Reset the `0_sat`'](#from-apr-11-2023-add-min_work_ex-before_graphrmd-and-successfully-run-for-two-suburbs-add-list-de-clutter-the-code-reset-the-0_sat)
  - [From Apr 10, 2023 **Brandon Lu** (Sorry for the American date format)](#from-apr-10-2023-brandon-lu-sorry-for-the-american-date-format)
    - [This contains](#this-contains)
    - [You might want to look at](#you-might-want-to-look-at)
    - [My progress](#my-progress)
    - [Implication of my work](#implication-of-my-work)
  - [Useful resources for learning GitHub](#useful-resources-for-learning-github)
  - [Useful resources for learning markdown](#useful-resources-for-learning-markdown)
  - [Apr 10, 2023:](#apr-10-2023)
    - [9:30 pm](#930-pm)
    - [Relative path](#relative-path)
    - [10:00 pm](#1000-pm)
    - [11:00 pm](#1100-pm)
    - [12:00 am](#1200-am)
  - [Questions](#questions)


## Final report
1. get the `suburb.txt`

## TODO
- [X] Conclusion
- [X] Starting writing transferrables
  - [X] Why we want to do this
  - [X] Conclusion `finalized`
  - [X] Too many suburbs
    - [X] Not that many
  - [X] Suburbs with little data
- [X] Jasmine's
- [X] Brandon's proposal
- [X] Universal function for Jasmine's
- [X] Future plan

- 2046 for all suburbs
- Auburn 675
- Eastwood 191

#### Long Lat
- Jasmine: individual houses `geo-code` `geo-sphere`
- Brandon: train station `manually` or `python`
- Gihansa: major train stations!!! ONLY!!! **NULL RESULT!!!**
- **Propose? Suppose that it doesn't make a difference?**
- To reach a more solid solution: 
  - incorporate `central` `town hall` `Wynyard`: big train stations make a diff
  - Blacktown, dsalfjdsalsadlf, tweak to reach a more robust conclusion
- Gihansa: reclassify??


#### EXEC SUMMARY RN: (**Yvonne**)

Based on our data analysis using 2046 data points from five different suburbs, we can conclude that the distance from a train station has a small but relatively insignificant effect on townhouse prices.Based on our data analysis using 2046 data points from five different suburbs, we can conclude that the distance from a train station has a small but relatively insignificant effect on townhouse prices.
(33 words)

#### Re-categorization (Jasmine)
date time -> qual

#### Data website:
- train station: https://en.wikipedia.org/wiki/List_of_Sydney_Trains_railway_stations 
- data from: https://www.auhouseprices.com/sold/list/NSW/
- inspiration: https://embracingtherandom.com/r/web-scraping/rent-scraping/

#### Limitaion:
- from other suburbs (Jasmine)

## Repo structure
```
.
├── Jasmine_files // Archived
├── README.md

├── csv_cache 
// Exported data: exported from `min_working_example-before_graph_analysis_Apr12.rmd`
// to be imported into `min_working_example-graph_adapted_from_Jasmine-Apr12_Apr12.Rmd`

├── df_files // Archived dependencies for `Jasmine_files`

├── get_suburbs.py 
// Input: a list of suburb; 
// Output: a list of suburb along with the postcode and geometric coordination

├── get_suburbs_by_areas.py // Archived
├── get_suburbs_by_areas_data

├── get_suburbs_data // Output data for `get_suburbs_data.py`

├── get_train_station_names.py 
├── get_train_station_names_data
// Get all the train stations from the wikipedia link:
// url = "https://en.wikipedia.org/wiki/List_of_Sydney_Trains_railway_stations"

├── l_files // Archived

├── min_working_example-before_graph_analysis_Apr12.html
├── min_working_example-before_graph_analysis_Apr12.rmd
├── min_working_example-graph_adapted_from_Jasmine-Apr12_Apr12.Rmd
├── min_working_example-graph_adapted_from_Jasmine-Apr12_Apr12.html

└── suburbs.txt // Input for `min_working_example-before_graph_analysis_Apr12.rmd`
```

## What's next?
### Best case
- [x] Validate the automatic `py` scraping program
- [x] Generate all files available in the `csv` format
##### This will be left to ALL GROUP MEMBERS; I think it's best for all of us to think about what we can do with all this data
- [x] Write new prgrams for all these files and figure out how we can have at least an insight
### Worst case
- [x] Can @Jasmine send your `last resort file` to me so that I can upload it to all people to see?

## Apr 12: log

- 12 pm: the universal function now works as expected: `min_working_example-before_graph_analysis_Apr12.rmd`
    - Function: export_all_suburbs()
    - Input: suburbs.txt
    - Note that: if you have `# "2142/granville/", -33.8326, 151.0120` in the `txt` file, the program is automatically configured to skip that line/entry
    - Also note that: it seems that if you don't delete the `csv` files in the `csv_cache` folder, the program will also skip that suburbs. So delete it if you want a fresh export
    - Output: in `csv_cache`
    - Note: for the outputs, **look at the first column!!! It has changed!!!**

- Contribution and Implication:
    - **You now can add as many suburbs as you want very efficiently in the `suburbs.txt` file, and avoid repeately exporting `csv` file to save time**
    - You now can drastically reduce the random error by incorporating mass data into your research     - You now has a much more encapsulated functions as in the `min_working_example-before_graph_analysis_Apr12.rmd` file so that you can edit the functions in that file with ease 

- [x] Note that after `setting the working directory`, you need to include the `relative path` only: DO NOT INCLUDE the `/` at the front!!! **E.g., "csv_cache/l_2122_eastwood_houseprice.csv"** is valide while "csv_cache/l_2122_eastwood_houseprice.csv" is NOT!

## Apr 12: tomorrow plan
- [x] Complete the `universal` function `get_suburbs_data`
- [x] Increase the scope of research to 10 or even 15 suburbs
- [x] Export all 15 files in the `csv` format
- [x] **Give the `csv` files to Jasmine and Bjungjun for future processing**

*Ideally, the increased amount of data should make the data seem less random. And we can actually see a trend from it. I'll also be experimenting different methods to try to get a trend.*

**It's been a long day. Thank you and every one of you for your hard work!**

## From Apr 11, 2023: 'Add `min_work_ex-before_graph.rmd` and successfully run for two suburbs; Add list; De-clutter the code; Reset the `0_sat`'
- Please look at the `min_work_ex-before_graph.rmd` and the format of `csv_cache/l_2122_eastwood__houseprice.csv`
- The `min_work_ex-before_graph.rmd` should be able to run on any computer
    - It currently can process any location and export a `csv` file in `csv_cache/`
    - Tomorrow, I will add a more general function
    - 
```
get_suburbs_data <- function(suburb_list) { -->
  all_data <- list() -->
  for (suburb_info in suburb_list) { -->
    location <- suburb_info[[1]] -->
    lat <- suburb_info[[2]] -->
    lon <- suburb_info[[3]] -->
    suburb_data <- get_l_suburb(location, lat, lon) -->
    all_data[[location]] <- suburb_data -->
  } -->
  return(all_data) -->
} -->
suburb_list <- list( -->
  list("2122/eastwood/", -33.7899, 151.0821), -->
  list("2144/auburn/", -33.8490, 151.0329) -->
) -->
suburb_data_list <- get_suburbs_data(suburb_list) -->
1. Print the list -->
print(suburb_data_list) -->
2. Append the data (assuming you want to combine all dataframes into one) -->
combined_data <- do.call(rbind, lapply(suburb_data_list, function(x) x)) -->
```
## From Apr 10, 2023 **Brandon Lu** (Sorry for the American date format) 

### This contains
- Code from Jasmine to directly import the csv files
- The now modified code (By brandon lu)
(Go to #Generic function taking a list of suburbs and geolocation data DONE)

### You might want to look at
- Jasmine files `Jasmine_self_test_sat_night.Rmd`
    - Her files are dependent on the `l_files` folder
    - Note that I've changed the absolute path to `relative` path, so once you've downloaded it, you should be able to run with without any modification

- `Project2_1901_v0.Rmd`
    - This is my modified version, look at #Generic function taking a list of suburbs and geolocation data 
    - It automatically generates the `csv_cache` folder if it doesn't exist and it's dependent on It

### My progress
You can see my progress report in the `Brandon_Lu_stat_rep.md` file:
- Create the `Generic function taking a list of suburbs and geolocation data:` section
- Modify the absolute path
- Debug the `geo_coder` `address` not character problem (sorry for the American spelling)
- Reorganize all the files that the two coding memembers have sent me; I've put them all in this very GitHub repository
- Discussed with Jasmine about some changes that can be made to make the result clearer (Saturday evening)

### Implication of my work
- **empower us to mass analyze data and expand the scope of research**
- achive modulization and encapsulation to make debugging and coding easier
- establish the GitHub repository to make code sharing easier
- streamline the development process
- ensure preliminary compatibility with other group member's code

## Useful resources for learning GitHub
- full tutorial and guide: [Quick Start](https://docs.github.com/en/get-started/quickstart)
- GUI (Graphical User Interface) application, if you find CLI (command-line input) challenging: [GitHub Desktop](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjK7JW53Z_-AhWIsVYBHTqDCQQQFnoECAcQAQ&url=https%3A%2F%2Fdesktop.github.com%2F&usg=AOvVaw3Q4aArCExy0qKbKQYeMfD4)
- YouTube Videos about *git*, *GitHub*, and *version control*

## Useful resources for learning markdown
This file is written in `markdonw` as a `md` format. It's the foundation on which the `rmd` format is built. 

[Markdown tutorial](https://www.markdowntutorial.com/lesson/1/)

## Apr 10, 2023:

### 9:30 pm

### Relative path

Please refer to this [guide](https://stackoverflow.com/questions/36834767/how-to-use-rstudio-relative-paths).

```
setwd("..")
getwd()

l_parramatta_dist <- read.csv("l_files/l_parramatta_houseprice.csv")
```

The directory can be shown as below:
```
~/Uni-Code/4_DATA1901_RStudio/Project2  ‹my-branch*› 
╰─➤  tree
.
├── Brandon_Lu_stat_rep.md
├── Jasmine_self_test_sat_night.Rmd
├── Jasmine_self_test_sat_night.html
├── Project2_1901_v0.Rmd
├── SelfTest_from_tutorial_Project2.html
├── SelfTest_from_tutorial_Project2.rmd
├── df_files
│   ├── df_eastwood_houseprice.csv
│   ├── df_granville_houseprice.csv
│   ├── df_marrickville_houseprice.csv
│   ├── df_merrylands_houseprice.csv
│   ├── df_parramatta_houseprice.csv
│   └── df_strathfield_houseprice.csv
├── l_files
│   ├── l_auburn_houseprice.csv
│   ├── l_eastwood_houseprice.csv
│   ├── l_granville_houseprice.csv
│   ├── l_merrylands_houseprice.csv
│   └── l_parramatta_houseprice.csv
├── test_code.rmd
├── test_read_csv_before.html
└── test_read_csv_before.rmd

3 directories, 20 files
```

### 10:00 pm

- Trying to figure out what everything means
- Comment the code when necessary

### 11:00 pm

- Organize code and propose some changes
- Combine all code into a `mega-function`

### 12:00 am

- Checking the compatibility with Jasmine's code

## Questions

- [] Why `df_` and `l_`?
