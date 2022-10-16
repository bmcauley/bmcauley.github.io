## Assignment Blog #3 - EDA

**_What is your overall goal when doing an EDA?_**

When doing EDA, my overall goal is to determine the underlying structure of the data I am working with and identifying potential patterns between variables. Using visual means, I let the data tell me its story so I can know how to interpret the problem its existence is trying to solve; decide to what extent it needs to be cleaned and/or manipulated (_because no collected data is ever ready for analysis as-is, anyone who says otherwise is either a liar or isn't doing analytics right_); and identify all of the potential "problem children" (outliers, autocorrelations, skewness, etc.).

**_What methods do you think are important?_**

Generally, I always make use of the following methods for EDA and believe they are fundamental to the start of _any_ data project:
- Printing the first 5-10 rows - Simple, and provides a quick look at the layout of the data, the variable types, and how the values are represented
- Five-number summary - Another simple method to see what might be "typical" in a variable
- Boxplots - A visual representation of the five-number summary, with the added benefit that outliers can be seen (if any)
- Histograms/bar plots - For distributions and patterns of variables; absolutely no reason _not_ to include it
- Contingency tables - If categorical variables are present, there might be some interesting associations to be uncovered between values of these variables. Just having a count is also helpful
- Scatter plots - Identifies the strength, direction, and shape of relationships between variables, also pretty non-negotiable to include
- Correlation matrices - Provides the values for strength in correlation, which I really like! I will admit, however, it does fall short since it assumes linear relationships, so it's not always the most useful. I'm biased, I really like measuring correlation.

**_What things do you try to look for?_**

The things I try to look for in EDA are:
- Variable data types - Usually determines what kind of visuals would be appropriate to use and whether conercion would be needed (i.e. if a column of ages has a string type; doesn't make sense!)
- Missing data - The volume of missing information in a variable and whether that variable is even important enough to retain rather than fill in
- The aforementioned "problem children" - Can throw a wrench in modeling if they are not addressed properly, either by removal or variable transformation (whichever is considered appropriate for each case)
- Irrelevent variables - Not all columns are created equal, and some will provide zero insight in analysis, so no point in wasting computational resources to keep them in the data set
