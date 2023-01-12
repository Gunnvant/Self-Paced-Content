### Coding Problems
- Around 4-5 problems in which a dataset will be given and students will need to answer questions by manipulating data and computing probability using binomial, poisson or normal distribution. Problems could also involve the use of 2 sample t-test, ANOVA, Chi Square test of factor association

**Q1. Use the `./data/bank_transactions.csv`. This has daily data on withdrawl activity at 5 ATMs. What are the chances that there will be more than 148 withdrawls in a day for Mount Road ATM? Round your result to 2 decimal places.**

**Solution**

```python
import pandas as pd
from scipy.stats import binom, poisson
import math
import scipy
df = pd.read_csv("./data/bank_transactions.csv")
round(1-poisson.cdf(147,144),2)

```

**Q2.Use the `./data/bank_transactions.csv`. This has daily data on withdrawl activity at 5 ATMs. It is believed that on an average 490000 Rs are withdrawn from the Mount Road ATM daily, is there substantial statistical evidence to the belief or have average daily withdrawls increased? Use a significance level of 5%.**

**Solution**

```python
def p_value(pop_mean,sample_mean,sample_stdev,sample_size):
    SE = sample_stdev/math.sqrt(sample_size)
    if pop_mean>sample_mean:
        pval = scipy.stats.norm(pop_mean,SE).cdf(sample_mean)
    else:
        pval = 1-scipy.stats.norm(pop_mean,SE).cdf(sample_mean)
    return pval


pop_mean = 490000
sample_mean = df[df['ATM Name']=='Mount Road ATM']['Total amount Withdrawn'].mean()
sample_stdev = df[df['ATM Name']=='Mount Road ATM']['Total amount Withdrawn'].std()
sample_size = df[df['ATM Name']=='Mount Road ATM']['Total amount Withdrawn'].shape[0]

p_value(pop_mean,sample_mean,sample_stdev,sample_size) ### Reject H0, withdrawls have increased
```

**Q3.Use the `./data/bank_transactions.csv`. This has daily data on withdrawl activity at 5 ATMs. Compare the average daily withdrawls on Mount Road ATM vs Big Street ATM for year 2015. Do you find them to be statistically. Use a significance level of 5%
different?**

**Solution**

```python
import scipy.stats as stats
def replace(x):
    return x.replace("-","/")
df['Transaction Date']=df['Transaction Date'].map(replace)

df['Year']=pd.to_datetime(df['Transaction Date'],format="%d/%m/%Y").dt.year
mnt_rd = df[df['ATM Name']=='Mount Road ATM'].query("Year==2015")['Total amount Withdrawn'].values
big_street = df[df['ATM Name']=='Big Street ATM'].query("Year==2015")['Total amount Withdrawn'].values
stats.ttest_ind(mnt_rd,
                big_street,equal_var=True) ## pvalue is low so reject
```

**Q4.Use the `./data/bank_transactions.csv`. This has daily data on withdrawl activity at 5 ATMs. For the Mount Road ATM, in a month what is the probability that there will be 10 days in which the withdrawl amoiunt will be more than 684350.0?**

**Solution**

```python
n = df[df['ATM Name']=='Mount Road ATM']['Total amount Withdrawn'].shape[0]
obs = df[(df['ATM Name']=='Mount Road ATM')&(df['Total amount Withdrawn']>684350)]['Total amount Withdrawn'].shape[0]
p = obs/n
binom.cdf(10,30,0.25)
```

### Concept Questions
- Around 5 problems that will test learner's ability to formulate a correct Null and Alternate Hypothesis, formulate the correct P-value, articulate the notion of type 1 and type 2 error.

**Q1. Imagine you were doing a hypothesis test to find out if there was a change in the click through rate on a company's website before and after a design modification on the home page of the website. Which hypothesis test will you use? Assume that before design change you have average click through rates for 10 days. You also have data after design change for another 10 days.**

- (a) ANOVA Test
- (b) Chi Square Test
- **(c) 2 Sample T test**
- (d) Paired sample T test

**Solution**

Since two samples are being compared and we want to test the change in average of a quantity (click through rates here), we can use 2 Sample T test.

**Q2. Imagine that you did a hypothesis test and the p-value that was computed turned out to be 2%. Given below is the null and alternate hypothesis pair**

- H0: The sample means from two groups are similar
- Ha: The sample means are different

Based on the p-value what will be your conclusion

- (a) There is sufficient evidence to say that the means are not same
- (b) The p-value is large and hence H0 can't be rejected
- **(c) Can't decide if the p-value is small**
- (d) None of these

**Solution**

Until there is excplicit or implicit information given about significance level, one can't decide if its small or not. The problem doesn't explicitly or implicitly states the significance level

**Q3. A new test for diagnosing malaria has been developed, the test turned out to be positive ( patient had malaria) for 7% of the patients who infact did not have malaria, if the test starts with an assumption that the patient doesn’t have malaria and then looks at the data to find the evidence to the contrary then which statement is correct for the 7% of the people:**

- **(a) A type I error has been made**
- (b) A type II error has been made
- (c) A type IV error has been made
- (d) No error has been committed

**Solution** A, The null hypothesis in this scenario will be H0: Patient doesn’t have malaria, The alternate hypothesis will be Ha: Patient has malaria, for some cases H0 is true but our test is able to reject H0, so a type I error has been committed 

**Q4. There are 100 balls in a bag, 40 are white and 60 are red. If each ball is drawn randomly (without replacement) from the bag and we define ‘X’ as a random variable denoting the number of red balls, then which statement is true:**
- A.	“X” is an binomial random variable
- **B.	“X” is not a binomial random variable**

**Answer** B, This is not a binomial random variable as the probability of success is not constant from one trail to another. In the first trail P(S) = 60/100, in the second trial it can be either 59/99 or 60/99.

**Q5. . It has been observed that 12% of the drivers stopped at Mekri Circle in Bangalore show traces of alcohol. A random sample of 20 drivers is taken, to find the probability that upto 10 drivers will have traces of alcohol in thier blood we can use:**

- A. Poisson Distribution
- B. Chi Square Distribution
- **C. Binomial Distribution**
- D. Normal Distribution

**Answer** C, This is a binomial random variable as:

- The number of trails are finite
- There are only two outcome
- P(S) remains constant from one trial to another
