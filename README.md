# README

## Apr 12: tomorrow plan
- [ ] Complete the `universal` function `get_suburbs_data`
- [ ] Increase the scope of research to 10 or even 15 suburbs
- [ ] Export all 15 files in the `csv` format
- [ ] **Give the `csv` files to Jasmine and Bjungjun for future processing**

*Ideally, the increased amount of data should make the data seem less random. And we can actually see a trend from it. I'll also be experimenting different methods to try to get a trend.*

**It's been a long day. Thank you and every one of you for your hard work!**

## From Apr 11, 2023: 'Add `min_work_ex-before_graph.rmd` and successfully run for two suburbs; Add list; De-clutter the code; Reset the `0_sat`'
- Please look at the `min_work_ex-before_graph.rmd` and the format of `csv_cache/l_2122_eastwood__houseprice.csv`
- The `min_work_ex-before_graph.rmd` should be able to run on any computer
    - It currently can process any location and export a `csv` file in `csv_cache/`
    - Tomorrow, I will add a more general function
    - 
```
# get_suburbs_data <- function(suburb_list) { -->
#   all_data <- list() -->
#   for (suburb_info in suburb_list) { -->
#     location <- suburb_info[[1]] -->
#     lat <- suburb_info[[2]] -->
#     lon <- suburb_info[[3]] -->
#     suburb_data <- get_l_suburb(location, lat, lon) -->
#     all_data[[location]] <- suburb_data -->
#   } -->
#   return(all_data) -->
# } -->
# suburb_list <- list( -->
#   list("2122/eastwood/", -33.7899, 151.0821), -->
#   list("2144/auburn/", -33.8490, 151.0329) -->
# ) -->
# suburb_data_list <- get_suburbs_data(suburb_list) -->
# # 1. Print the list -->
# print(suburb_data_list) -->
# # 2. Append the data (assuming you want to combine all dataframes into one) -->
# combined_data <- do.call(rbind, lapply(suburb_data_list, function(x) x)) -->
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
