##  Project 2 Reflection

The purpose of this project was to [create a vignette](https://mmkahn.github.io/Project2/) using a [github project repo](https://github.com/MMKahn/Project2). The goal was to provide instruction about contacting an API of our choice (out of the ones offered) using functions and returning data for analysis. Upon reading the project description for this assignment, my first impression was that it was going to be very difficult. I'd never worked with APIs before, they looked confusing! And without JSON parsing, the information returned looks complicated!

It turned out to be rather simple, it felt more like a long homework assignment (which is a good thing!). What was being asked of us was broken down very intuitively, and easy to translate to code chunks. Ironically, when I feel a project is going to be "easy", it ends up being very frustrating, and vice versa, in this case. This project felt like it had a very stress-free conclusion upon us finishing, and that's always a nice feeling. I learned a lot, but I didn't feel like throwing my laptop out the window. :)

_**Explain what you did in the project and any interesting findings**_

My contributions to the project included:

- Setting up the script to generate the README.md, and testing it worked
- Writing the narrative throughout every section (minus the EDA section)
- Implementation of the functions used to pull data from the API, and the associated usage examples

It was interesting to find that API filtering was already built into generating different endpoints, so I used that to my advantage in determining how the user should input their queries. It was also surprising to me that the API will still successfully run a query (so long as the logic is valid), even if what the user is looking for doesn't inherently exist in the database. (i.e. if you ask for 5 observations for a filter in which only 3 exist, you still get the 3 and not an error; or if _none_ exist, you just get an empty dataframe.)

_**What would you do differenly in approaching a similar project in the future?**_

In approaching a similiar project in the future, I would expand the function to enable multiple filters for a query and allow the user to specify whether they even _want_ to query based on search criteria or get randomly generated data. Essentially, merging the two functions we ended up with into one. I would also do some data validation since there were a lot of observations that didn't have coordinates or counties, and it would've made the returned results more meaningful if there weren't so many `NA`s, in my opinion. To fix that issue, I would either filter those out or figure out how to dynamically fill them in appropriately using standarized geographic data.
