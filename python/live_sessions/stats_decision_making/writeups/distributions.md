## Binomial Distribution

Used when the rv is discreet and has the following properties:

1. The possible trails are countable
2. In each trial there are only two possible outcomes
3. One trial is independent of the other

**Probability Mass Function**

$$P(X=x) = {n \choose x}p^x(1-p)^{n-x} $$

**CDF**
$$P(X<=k)=\sum_{i=0}^{|k|}{n \choose i}p^i(1-p)^{n-1}$$

## Drill problems

1. Suppose 60 percent of all the people prefer coke to pepsi. We select 18 people for further study.

- How many of them will be expected to prefer coke?
- What is the probability 10 of those surveyed will prefer coke?
- What is the probability that atleast 6 will prefer coke?
- What is the probability 15 will prefer coke?

2. A manufacturer of window frames knows from long experience that 5 percent of the production will have some type of minor defect that will require an adjustment. What is the probability that in a sample of 20 window frames:

- None will need adjustment?
- At least one will need adjustment?
- More than two will need adjustment?

## Poisson Distribution

Used when the random variable is positive discreet and:

1. The rv describes a rate like term

**PMF**

$$P(X=i)=\frac{\lambda^ie^{-\lambda}}{i!}$$

**CDF**

$$P(X<=k)=e^{-\lambda}\sum_{j=0}^{|k|}\frac{\lambda^j}{j!}$$

## Drill Problems

1. Textbook authors and publishers work very hard to minimize the number of errors in a text. However, some errors are unavoidable. Mr. J. A. Carmen, statistics editor, reports that the mean number of errors per chapter is O.B. What is the probability that there are less than 2 errors in a particular chapter?

2. Phone calls arrive at the rate of 48 per hour at the reservation desk for Regional Airways.
- Compute the probability of receiving three calls in a 5-minute interval of time.
- Compute the probability of receiving exactly 10 calls in 15 minutes.
- Suppose no calls are currently on hold. If the agent takes 5 minutes to complete the
current call, how many callers do you expect to be waiting by that time? What is the
probability that none will be waiting?
- If no calls are currently being processed, what is the probability that the agent can take 3 minutes for personal time without being interrupted by a call?

3. Airline passengers arrive randomly and independently at the passenger-screening facility at a major international airport. The mean arrival rate is 10 passengers per minute.
- Compute the probability of no arrivals in a one-minute period.
- Compute the probability that three or fewer passengers arrive in a one-minute period.
- Compute the probability of no arrivals in a 15-second period.
- Compute the probability of at least one arrival in a 15-second period.