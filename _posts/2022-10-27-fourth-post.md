## Assignment Blog #4 - Variable Selection

**_Write up a brief discussion of how you would plan to determine variables to use in a regression model._**

When determining which variables from a data set to use in a regression model, I first consider the following:
- Redundancy - Does more than one variable explain the same (or similar) phenomenon in the response?
- Collinearity - Do any predictor variables have a significant association with or influence on any others? 
- Transformation - Do any of the predictor variables have a non-linear relationship with the response?

To answer these questions, I would perform an EDA! To (partially) regurgitate from my previous post, my process would be:
1. Get the dimensions of the data to guestimate the size of the model needed to "best" make a prediction. While we always want to keep models as simple as possible, larger datasets may require larger models and similar for smaller ones! 
2. Print the first 5-10 rows to see what variables are present, and intuitively knock out any that aren't likely to be deemed significant in predicting the response.
3. Construct a faceted scatter plot for the response vs the predictors to identify the shape and strength of the relationships between them (if any). If they're non-linear, then the predictors may need to be transformed. If there is a weak or no correlation, then those predictors can also probably be left out.
4. Plot a correlation matrix for a value-based representation of the relationships between the response and the predictors, and also between the predictors. If there are multicollinearity issues, certain predictors may be removed based on their VIF values.
5. Run a few different variable selection functions to see which variables the algorithms deem important (or not), and compare this to what I chose manually. I would also look at the information critera (AIC, BIC, Cp) to refine my selection.

**_What variable selection techniques do you prefer and why?_**

I prefer stepwise selection with/and cross validation. You can't get any simpler then these in terms of implementation, computational resources, interpretability, and generalization. In other words, I like that they are easy to call; really quick and efficient in returning results; with some basic hypothesis testing knowledge, easy to determine which variables were deemed significant and to what degree (or not); and because they don't make a lot of assumptions, they are "friendlier" to predictors that are not linearly related to the response, but still provide sufficient enough information to be included (as opposed to methods like LASSO, which would penalize them for it because they don't have a linear relationship). Cross-validation adds the benefit of testing whether the predictors chosen are _consistently_ useful across _k_ random samples of the data.
