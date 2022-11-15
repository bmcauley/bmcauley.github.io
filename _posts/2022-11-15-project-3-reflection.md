##  Project 3 Reflection

The purpose of this project was to implement automated reports, and storing them together on [a github site](https://suyogd9.github.io/ST558-Project-3/) _(and props to Suyog for the pretty theme, I had nothing to do with that lol)_ using a [github project repo](https://github.com/Suyogd9/ST558-Project-3). The goal of the analysis was to predict the number of shares of articles published by Mashable, using a variety of modeling methods and comparing their performance.

_**What would you do differently?**_

On the R side, not much, to be honest. I was pretty happy with how I implemented the models, really took my `ggplot2` usage to the next level, and the script for rendering the reports was rather robust; I got to allow for all value options for the function like I wanted to in the previous project. As for using git, I would definitely create branches more often instead of always committing to main. I did so for the automation process, but the rest I just stayed on main. I would always test my work before pushing, but I know it's not the best practice, especially if there's more than one person working on the project...

_**What was the most difficult part for you?**_

The automation, haha! Especially when trying to use the `render()` function _within_ the .Rmd file. Doesn't work for dynamic inputs, and I tried for several hours before realizing that. Hence, script. There were _a lot_ of StackOverflow and RStudio community tabs open before I had that revelation. I'm an overthinker, and for R, that usually makes me waste more time than actually needed since the simplest solution is almost always the correct one.

_**What are your big take-aways from this project?**_

- I never thought to use values of a variable as a basis for a document, and the world of possibiltiies in statistical programming has expanded even further in my mind.
- I will never underestimate R's capabilities ever again. It surpasses SAS in my eyes _(as a SAS employee, I can say that; we only use nowadays VA anyway, the glass cannon that it is...)_.
- I always thought of myself as a weak programmer _(C++ was never my friend in undergrad, and still isn't)_, but this project has solidified my confidence in my abilities, and I can't wait to keep improving and using the tools I now have for personal projects.
- _Random forests take up way too much time and computational resources to train, which made waiting on the reports to generate so slow..._ I thought boosted was supposed to be the slow one! If I need a tree, I'll stick to boosting it.
