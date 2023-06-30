# Theoretical interview questions



## Table of contents

* [Supervised machine learning](#supervised-machinelearning)
* [Linear regression](#linear-regression)
* [Validation](#validation)
* [Classification](#classification)
* [Regularization](#regularization)
* [Feature selection](#feature-selection)
* [Decision trees](#decision-trees)
* [Random forest](#random-forest)
* [Parameter tuning](#parameter-tuning)
* [Clustering](#clustering)
* [Time series](#time-series)

<br/>

## Supervised machine learning

**What is supervised machine learning? (Easy)**

Supervised learning is a type of machine learning in which our algorithms are trained using well-labeled training data, and machines predict the output based on that data. Labeled data indicates that the input data has already been tagged with the appropriate output. Basically, it is the task of learning a function that maps the input set and returns an output. Some of its examples are: Linear Regression, Logistic Regression, KNN, etc.


<br/>

## Linear regression

**What is regression? Which models can you use to solve a regression problem? (Easy)**

Regression is a part of supervised ML. Regression models investigate the relationship between a dependent (target) and independent variable (s) (predictor).
Here are some common regression models

- *Linear Regression* establishes a linear relationship between target and predictor (s). It predicts a numeric value and has a shape of a straight line.
- *Polynomial Regression* has a regression equation with the power of independent variable more than 1. It is a curve that fits into the data points.
- *Ridge Regression* helps when predictors are highly correlated (multicollinearity problem). It penalizes the squares of regression coefficients but doesn’t allow the coefficients to reach zeros (uses L2 regularization).
- *Lasso Regression* penalizes the absolute values of regression coefficients and allows some of the coefficients to reach absolute zero (thereby allowing feature selection).

<br/>

**What is linear regression? When do we use it? (Easy)**

Linear regression is a model that assumes a linear relationship between the input variables (X) and the single output variable (y).

With a simple equation:

```
y = B0 + B1*x1 + ... + Bn * xN
```

B is regression coefficients, x values are the independent (explanatory) variables  and y is dependent variable.

The case of one explanatory variable is called simple linear regression. For more than one explanatory variable, the process is called multiple linear regression.

Simple linear regression:

```
y = B0 + B1*x1
```

Multiple linear regression:

```
y = B0 + B1*x1 + ... + Bn * xN
```

<br/>

**What are the main assumptions of linear regression? (Medium)**

There are several assumptions of linear regression. If any of them is violated, model predictions and interpretation may be worthless or misleading.

1. Features are not correlated (no **collinearity**) since it can be difficult to separate out the individual effects of collinear features on the target variable.
2. Errors are independently and identically normally distributed (y<sub>i</sub> = B0 + B1*x1<sub>i</sub> + ... + error<sub>i</sub>):
   1. No correlation between errors (consecutive errors in the case of time series data).
   2. Constant variance of errors - **homoscedasticity**. For example, in case of time series, seasonal patterns can increase errors in seasons with higher activity.
   3. Errors are normally distributed, otherwise some features will have more influence on the target variable than to others. If the error distribution is significantly non-normal, confidence intervals may be too wide or too narrow.

<br/>

**What’s the normal distribution? Why do we care about it? (Easy)**

The normal distribution is a continuous probability distribution whose probability density function takes the following formula:

![formula](https://mathworld.wolfram.com/images/equations/NormalDistribution/NumberedEquation1.gif)

where μ is the mean and σ is the standard deviation of the distribution.

The normal distribution derives its importance from the **Central Limit Theorem**, which states that if we draw a large enough number of samples, their means will follow a normal distribution regardless of the initial distribution of the sample, i.e **the distribution of the means of the samples is normal**. It is important that each sample is independent from the other.

This is powerful because it helps us study processes whose population distribution is unknown to us.


<br/>

**How do we check if a variable follows the normal distribution? (Difficult)**

1. Plot a histogram out of the sampled data. If you can fit the bell-shaped "normal" curve to the histogram, then the hypothesis that the underlying random variable follows the normal distribution can not be rejected.
2. Check Skewness and Kurtosis of the sampled data. Skewness = 0 and kurtosis = 3 are typical for a normal distribution, so the farther away they are from these values, the more non-normal the distribution.
3. Use Kolmogorov-Smirnov or/and Shapiro-Wilk tests for normality. They take into account both Skewness and Kurtosis simultaneously.
4. Check for Quantile-Quantile plot. It is a scatterplot created by plotting two sets of quantiles against one another. Normal Q-Q plot place the data points in a roughly straight line.

<br/>


**What methods for solving linear regression do you know? (Expert)**

To solve linear regression, you need to find the coefficients <img src="https://render.githubusercontent.com/render/math?math=\beta"> which minimize the sum of squared errors.

Matrix Algebra method: Let's say you have `X`, a matrix of features, and `y`, a vector with the values you want to predict. After going through the matrix algebra and minimization problem, you get this solution: <img src="https://render.githubusercontent.com/render/math?math=\beta = (X^{T}X)^{-1}X^{T}y">. 

But solving this requires you to find an inverse, which can be time-consuming, if not impossible. Luckily, there are methods like Singular Value Decomposition (SVD) or QR Decomposition that can reliably calculate this part <img src="https://render.githubusercontent.com/render/math?math=(X^{T}X)^{-1}X^{T}"> (called the pseudo-inverse) without actually needing to find an inverse. The popular python ML library `sklearn` uses SVD to solve least squares.

Alternative method: Gradient Descent. See explanation below.

<br/>

**Which metrics for evaluating regression models do you know? (Easy)**

1. Mean Squared Error(MSE)
2. Root Mean Squared Error(RMSE)
3. Mean Absolute Error(MAE)
4. R² or Coefficient of Determination
5. Adjusted R²

<br/>

**What are MSE and RMSE? (Easy)**

MSE stands for <strong>M</strong>ean <strong>S</strong>quare <strong>E</strong>rror while RMSE stands for <strong>R</strong>oot <strong>M</strong>ean <strong>S</strong>quare <strong>E</strong>rror. They are metrics with which we can evaluate models.

<br/>

**What is the bias-variance trade-off? (Easy)**

**Bias** is the error introduced by approximating the true underlying function, which can be quite complex, by a simpler model. **Variance** is a model sensitivity to changes in the training dataset.

**Bias-variance trade-off** is a relationship between the expected test error and the variance and the bias - both contribute to the level of the test error and ideally should be as small as possible:

```
ExpectedTestError = Variance + Bias² + IrreducibleError
```

But as a model complexity increases, the bias decreases and the variance increases which leads to *overfitting*. And vice versa, model simplification helps to decrease the variance but it increases the bias which leads to *underfitting*.

<br/>


## Validation

**What is overfitting? (Easy)**

When your model perform very well on your training set but can't generalize the test set, because it adjusted a lot to the training set.

<br/>

**How to validate your models? (Medium)**

One of the most common approaches is splitting data into train, validation and test parts.
Models are trained on train data, hyperparameters are selected based on the validation data, the final measurement is done on test dataset.

Another approach is cross-validation: split dataset into K folds and each time train models on training folds and measure the performance on the validation folds.
Also you could combine these approaches: make a test/holdout dataset and do cross-validation on the rest of the data. The final quality is measured on test dataset.

<br/>

**Why do we need to split our data into three parts: train, validation, and test? (Medium)**

The training set is used to fit the model, i.e. to train the model with the data. The validation set is then used to provide an unbiased evaluation of a model while fine-tuning hyperparameters. This improves the generalization of the model. Finally, a test data set which the model has never "seen" before should be used for the final evaluation of the model. This allows for an unbiased evaluation of the model. The evaluation should never be performed on the same data that is used for training. Otherwise the model performance would not be representative.

<br/>

**Can you explain how cross-validation works? (Medium)**

Cross-validation is the process to separate your total training set into two subsets: training and validation set, and evaluate your model to choose the hyperparameters. But you do this process iteratively, selecting different training and validation set, in order to reduce the bias that you would have by selecting only one validation set.

<br/>

**What is K-fold cross-validation? (Medium)**

K fold cross validation is a method of cross validation where we select a hyperparameter k. The dataset is now divided into k parts. Now, we take the 1st part as validation set and remaining k-1 as training set. Then we take the 2nd part as validation set and remaining k-1 parts as training set. Like this, each part is used as validation set once and the remaining k-1 parts are taken together and used as training set.
It should not be used in a time series data.

<br/>

**How do we choose K in K-fold cross-validation? What’s your favorite K? (Medium)**

There are two things to consider while deciding K: the number of models we get and the size of validation set. We do not want the number of models to be too less, like 2 or 3. At least 4 models give a less biased decision on the metrics. On the other hand, we would want the dataset to be at least 20-25% of the entire data. So that at least a ratio of 3:1 between training and validation set is maintained. <br/>
I tend to use 4 for small datasets and 5 for large ones as K.

<br/>


## Classification

**What is classification? Which models would you use to solve a classification problem? (Easy)**

Classification problems are problems in which our prediction space is discrete, i.e. there is a finite number of values the output variable can be. Some models which can be used to solve classification problems are: logistic regression, classification tree, random forests, multi-layer perceptron.

<br/>

**What is logistic regression? When do we need to use it? (Easy)**

Logistic regression is a Machine Learning algorithm that is used for binary classification. You should use logistic regression when your Y variable takes only two values, e.g. True and False, "spam" and "not spam", "churn" and "not churn" and so on. The variable is said to be a "binary" or "dichotomous".

<br/>

**Is logistic regression a linear model? Why? (Medium)**

Yes, Logistic Regression is considered a generalized linear model because the outcome always depends on the sum of the inputs and parameters. Or in other words, the output cannot depend on the product (or quotient, etc.) of its parameters.

<br/>

**What is sigmoid? What does it do? (Medium)**

A sigmoid function is a type of activation function, and more specifically defined as a squashing function. Squashing functions limit the output to a range between 0 and 1, making these functions useful in the prediction of probabilities.

Sigmod(x) = 1/(1+e^{-x})

<br/>

**How do we evaluate classification models? (Easy)**

Depending on the classification problem, we can use the following evaluation metrics:

1. Accuracy
2. Precision
3. Recall
4. F1 Score
5. Logistic loss (also known as Cross-entropy loss)

<br/>

**What is accuracy? (Easy)**

Accuracy is a metric for evaluating classification models. It is calculated by dividing the number of correct predictions by the number of total predictions.

<br/>

**Is accuracy always a good metric? (Easy)**

Accuracy is not a good performance metric when there is imbalance in the dataset. For example, in binary classification with 95% of A class and 5% of B class, a constant prediction of A class would have an accuracy of 95%. In case of imbalance dataset, we need to choose Precision, recall, or F1 Score depending on the problem we are trying to solve.

<br/>

**What is the confusion table? What are the cells in this table? (Medium)**

Confusion table (or confusion matrix) shows how many True positives (TP), True Negative (TN), False Positive (FP) and False Negative (FN) model has made.

||                |     Actual   |        Actual |
|:---:|   :---:        |     :---:    |:---:          |
||                | Positive (1) | Negative (0)  |
|Predicted|   Positive (1) | TP           | FP            |
|Predicted|   Negative (0) | FN           | TN            |

* True Positives (TP): When the actual class of the observation is 1 (True) and the prediction is 1 (True)
* True Negative (TN): When the actual class of the observation is 0 (False) and the prediction is 0 (False)
* False Positive (FP): When the actual class of the observation is 0 (False) and the prediction is 1 (True)
* False Negative (FN): When the actual class of the observation is 1 (True) and the prediction is 0 (False)

Most of the performance metrics for classification models are based on the values of the confusion matrix.

<br/>

**What are precision, recall, and F1-score? (Easy)**

[Link](https://en.wikipedia.org/wiki/Precision_and_recall)

<br/>

**Precision-recall trade-off (Hard)**

Tradeoff means increasing one parameter would lead to decreasing of other. Precision-recall tradeoff occur due to increasing one of the parameter(precision or recall) while keeping the model same. 

In an ideal scenario where there is a perfectly separable data, both precision and recall can get maximum value of 1.0. But in most of the practical situations, there is noise in the dataset and the dataset is not perfectly separable. There might be some points of positive class closer to the negative class and vice versa. In such cases, shifting the decision boundary can either increase the precision or recall but not both. Increasing one parameter leads to decreasing of the other. 

<br/>

**What is the ROC curve? (Medium)**

[Link](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)

<br/>

**How to interpret the AU ROC score? (Easy)**

AUC score is the value of *Area Under the ROC Curve*. 

If we assume ROC curve consists of dots, <img src="https://render.githubusercontent.com/render/math?math=(x_1, y_1), (x_2, y_2), \cdots, (x_m,y_m)">, then

<img src="https://render.githubusercontent.com/render/math?math=AUC = \frac{1}{2} \sum_{i=1}^{m-1}(x_{i%2B1}-x_i)\cdot (y_i%2By_{i%2B1})">

An excellent model has AUC near to the 1 which means it has good measure of separability. A poor model has AUC near to the 0 which means it has worst measure of separability. When AUC score is 0.5, it means model has no class separation capacity whatsoever. 

<br/>


**What do we do with categorical variables, while building ml models? (Medium)**

Categorical variables must be encoded before they can be used as features to train a machine learning model. There are various encoding techniques, including:
- One-hot encoding
- Label encoding
- Ordinal encoding
- Target encoding

<br/>

**Why do we need one-hot encoding? (Medium)**

If we simply encode categorical variables with a Label encoder, they become ordinal which can lead to undesirable consequences. In this case, linear models will treat category with id 4 as twice better than a category with id 2. One-hot encoding allows us to represent a categorical variable in a numerical vector space which ensures that vectors of each category have equal distances between each other. This approach is not suited for all situations, because by using it with categorical variables of high cardinality (e.g. customer id) we will encounter problems that come into play because of the curse of dimensionality.

<br/>


## Regularization

**What happens to our linear regression model if we have three columns in our data: x, y, z  —  and z is a sum of x and y? (Easy)**

We would not be able to perform the regression. Because z is linearly dependent on x and y so when performing the regression <img src="https://render.githubusercontent.com/render/math?math={X}^{T}{X}"> would be a singular (not invertible) matrix.
<br/>

**Which regularization techniques do you know? (Hard)**

There are mainly two types of regularization,
1. L1 Regularization (Lasso regularization) - Adds the sum of absolute values of the coefficients to the cost function. <img src="https://render.githubusercontent.com/render/math?math=\lambda\sum_{i=1}^{n} \left | w_i \right |">
2. L2 Regularization (Ridge regularization) - Adds the sum of squares of coefficients to the cost function. <img src="https://render.githubusercontent.com/render/math?math=\lambda\sum_{i=1}^{n} {w_{i}}^{2}">

* Where <img src="https://render.githubusercontent.com/render/math?math=\lambda"> determines the amount of regularization.

<br/>

**What kind of regularization techniques are applicable to linear models? (Hard)**

Ridge regression and Lasso. Both can be combined as elastic net.

<br/>

**How does L2 regularization look like in a linear model? (Hard)**

L2 regularization adds a penalty term to our cost function which is equal to the sum of squares of models coefficients multiplied by a lambda hyperparameter. This technique makes sure that the coefficients are close to zero and is widely used in cases when we have a lot of features that might correlate with each other.

<br/>

**How do we select the right regularization parameters? (Hard)**

Regularization parameters can be chosen using a grid search, for example https://scikit-learn.org/stable/modules/linear_model.html has one formula for the implementing for regularization, alpha in the formula mentioned can be found by doing a RandomSearch or a GridSearch on a set of values and selecting the alpha which gives the least cross validation or validation error.


<br/>

**What’s the effect of L2 regularization on the weights of a linear model? (Medium)**

L2 regularization penalizes larger weights more severely (due to the squared penalty term), which encourages weight values to decay toward zero.

<br/>

**How L1 regularization looks like in a linear model? (Hard)**

L1 regularization adds a penalty term to our cost function which is equal to the sum of modules of models coefficients multiplied by a lambda hyperparameter. For example, cost function with L1 regularization will look like: <img src="https://render.githubusercontent.com/render/math?math=\sum_{i=0}^{N}%20(y_i%20-%20\sum_{j=0}^{M}%20x_{ij}%20*%20w_j)%2B\lambda\sum_{j=0}^{M}%20\left%20|%20w_j%20\right%20|">

<br/>

**What’s the difference between L2 and L1 regularization? (Hard)**

- Penalty terms: L1 regularization uses the sum of the absolute values of the weights, while L2 regularization uses the sum of the weights squared.
- Feature selection: L1 performs feature selection by reducing the coefficients of some predictors to 0, while L2 does not.
- Computational efficiency: L2 has an analytical solution, while L1 does not.
- Multicollinearity: L2 addresses multicollinearity by constraining the coefficient norm.

<br/>

**Can we have both L1 and L2 regularization components in a linear model? (Hard)**

Yes, elastic net regularization combines L1 and L2 regularization. 

<br/>

**How do we interpret weights in linear models? (Medium)**

Without normalizing weights or variables, if you increase the corresponding predictor by one unit, the coefficient represents on average how much the output changes. By the way, this interpretation still works for logistic regression - if you increase the corresponding predictor by one unit, the weight represents the change in the log of the odds.

If the variables are normalized, we can interpret weights in linear models like the importance of this variable in the predicted result.

<br/>

**If a weight for one variable is higher than for another  —  can we say that this variable is more important? (Medium)**

Yes - if your predictor variables are normalized.

Without normalization, the weight represents the change in the output per unit change in the predictor. If you have a predictor with a huge range and scale that is used to predict an output with a very small range - for example, using each nation's GDP to predict maternal mortality rates - your coefficient should be very small. That does not necessarily mean that this predictor variable is not important compared to the others.

<br/>

**When do we need to perform feature normalization for linear models? When it’s okay not to do it? (Hard)**

Feature normalization is necessary for L1 and L2 regularizations. The idea of both methods is to penalize all the features relatively equally. This can't be done effectively if every feature is scaled differently. 

Linear regression without regularization techniques can be used without feature normalization. Also, regularization can help to make the analytical solution more stable, — it adds the regularization matrix to the feature matrix before inverting it. 

<br/>


## Feature selection

**What is feature selection? Why do we need it? (Easy)**

Feature Selection is a method used to select the relevant features for the model to train on. We need feature selection to remove the irrelevant features which leads the model to under-perform.  

<br/>

**Is feature selection important for linear models? (Easy)**

Yes, It is. It can make model performance better through selecting the most importance features and remove irrelevant features in order to make a prediction and it can also avoid overfitting, underfitting and bias-variance tradeoff. 

<br/>


**Can we use L1 regularization for feature selection? (Hard)**

Yes, because the nature of L1 regularization will lead to sparse coefficients of features. Feature selection can be done by keeping only features with non-zero coefficients.

<br/>

**Can we use L2 regularization for feature selection? (Hard)**

No, Because L2 regularization does not make the weights zero but only makes them very very small. L2 regularization can be used to solve multicollinearity since it stabilizes the model.

<br/>


## Decision trees

**What are the decision trees? (Easy)**

This is a type of supervised learning algorithm that is mostly used for classification problems, but can also be used for regression. Surprisingly, it works for both categorical and continuous dependent variables. 

In this algorithm, we split the population into two or more homogeneous sets. This is done based on most significant attributes/ independent variables to make as distinct groups as possible.

A decision tree is a flowchart-like tree structure, where each internal node (non-leaf node) denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node (or terminal node) holds a value for the target variable.

Various techniques : like Gini, Entropy

<br/>

**How do we train decision trees? (Easy)**

1. Start at the root node.
2. For each variable X, find the set S_1 that minimizes the sum of the node impurities in the two child nodes and choose the split {X*,S*} that gives the minimum over all X and S.
3. If a stopping criterion is reached, exit. Otherwise, apply step 2 to each child node in turn.

<br/>

**What are the main parameters of the decision tree model? (Easy)**

* maximum tree depth
* minimum samples per leaf node
* impurity criterion

<br/>

**How do we handle categorical variables in decision trees? (Easy)**

Some decision tree algorithms can handle categorical variables out of the box, others cannot. However, we can transform categorical variables with a one-hot encoder.

<br/>

**What are the benefits of a single decision tree compared to more complex models? (Easy)**

* easy to implement
* fast training
* fast inference
* good explainability

<br/>


## Random forest

**What is random forest? (Easy)**

Random Forest is a machine learning method for regression and classification which is composed of many decision trees. Random Forest belongs to a larger class of ML algorithms called ensemble methods (in other words, it involves the combination of several models to solve a single prediction problem).

<br/>

**Why do we need randomization in random forest? (Easy)**

Random forest in an extension of the **bagging** algorithm which takes *random data samples from the training dataset* (with replacement), trains several models and averages predictions. In addition to that, each time a split in a tree is considered, random forest takes a *random sample of m features from full set of n features* (with replacement) and uses this subset of features as candidates for the split (for example, `m = sqrt(n)`).

Training decision trees on random data samples from the training dataset *reduces variance*. Sampling features for each split in a decision tree *decorrelates trees*.

<br/>

**What are the main hyper-parameters of the random forest model? (Medium)**

- `max_depth`: Longest Path between root node and the leaf
- `min_sample_split`: The minimum number of observations needed to split a given node
- `max_leaf_nodes`: Conditions the splitting of the tree and hence, limits the growth of the trees
- `min_samples_leaf`: minimum number of samples in the leaf node
- `n_estimators`: Number of trees
- `max_sample`: Fraction of original dataset given to any individual tree in the given model
- `max_features`: Limits the maximum number of features provided to trees in random forest model

<br/>

**How do we know how many trees we need in random forest? (Easy)**

The number of trees in random forest is worked by n_estimators, and a random forest reduces overfitting by increasing the number of trees. There is no fixed thumb rule to decide the number of trees in a random forest, it is rather fine tuned with the data, typically starting off by taking the square of the number of features (n) present in the data followed by tuning until we get the optimal results.

<br/>

## Parameter tuning

**Which hyper-parameter tuning strategies (in general) do you know? (Medium)**

There are several strategies for hyper-tuning but I would argue that the three most popular nowadays are the following:
* <b>Grid Search</b> is an exhaustive approach such that for each hyper-parameter, the user needs to <i>manually</i> give a list of values for the algorithm to try. After these values are selected, grid search then evaluates the algorithm using each and every combination of hyper-parameters and returns the combination that gives the optimal result (i.e. lowest MAE). Because grid search evaluates the given algorithm using all combinations, it's easy to see that this can be quite computationally expensive and can lead to sub-optimal results specifically since the user needs to specify specific values for these hyper-parameters, which is prone for error and requires domain knowledge.

* <b>Random Search</b> is similar to grid search but differs in the sense that rather than specifying which values to try for each hyper-parameter, an upper and lower bound of values for each hyper-parameter is given instead. With uniform probability, random values within these bounds are then chosen and similarly, the best combination is returned to the user. Although this seems less intuitive, no domain knowledge is necessary and theoretically much more of the parameter space can be explored.

<br/>

**What’s the difference between grid search parameter tuning strategy and random search? When to use one or another? (Medium)**

For specifics, refer to the above answer.

<br/>


## Clustering

**What is unsupervised learning? (Easy)**

Unsupervised learning aims to detect patterns in data where no labels are given.

<br/>

**What is clustering? When do we need it? (Easy)**

Clustering algorithms group objects such that similar feature points are put into the same groups (clusters) and dissimilar feature points are put into different clusters.

<br/>


**How to select K for K-means? (Easy)**

* Domain knowledge, i.e. an expert knows the value of k
* Elbow method: compute the clusters for different values of k, for each k, calculate the total within-cluster sum of square, plot the sum according to the number of clusters and use the band as the number of clusters.
* Average silhouette method: compute the clusters for different values of k, for each k, calculate the average silhouette of observations, plot the silhouette according to the number of clusters and select the maximum as the number of clusters.

<br/>

## Time series

**What is a time series? (Easy)**

A time series is a set of observations ordered in time usually collected at regular intervals.

<br/>

**How is time series different from the usual regression problem? (Medium)**

The principle behind causal forecasting is that the value that has to be predicted is dependant on the input features (causal factors). In time series forecasting, the to be predicted value is expected to follow a certain pattern over time.

<br/>

**Which models do you know for solving time series problems? (Easy)**

* Simple Exponential Smoothing: approximate the time series with an exponential function
* Trend-Corrected Exponential Smoothing (Holt‘s Method): exponential smoothing that also models the trend
* Trend- and Seasonality-Corrected Exponential Smoothing (Holt-Winter‘s Method): exponential smoothing that also models trend and seasonality
* Autoregressive models: similar to multiple linear regression, except that the dependent variable y_t depends on its own previous values rather than other independent variables.

<br/>


