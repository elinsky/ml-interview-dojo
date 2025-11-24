# Question

Why is it empirical?

# Answer

It's called "empirical" because the risk is calculated from observed data (the training dataset) rather than from the true underlying probability distribution, which is unknown and inaccessible.

"Empirical" means based on observation, measurement, and experience rather than theory alone. In empirical risk minimization:

- We don't have access to the true data distribution or the population
- We only have a finite sample (our training data) drawn from that distribution
- We compute risk/loss by averaging over this observed sample
- This sample-based calculation is an **estimate** of the true risk

The process mirrors statistical estimation in general: we use an **estimator** (a function of our sample data) to approximate an unknown population parameter. The empirical risk is our best estimate of the true risk given only the data we've collected. Measurement inherently reduces uncertainty based on observations, and in ML, those observations are our training examples.

This is why larger datasets generally improve model performance - they provide better empirical estimates of the true risk. It's also why techniques like cross-validation and the bootstrap are useful: they help us understand how well our empirical measurements (based on finite samples) approximate the true underlying quantities we care about.

---

## Extracts from my notes

### 201806080942 Concept of measurement - Measurement is a quantified reduction in uncertainty based on your observations.txt

```
Concept of Measurement

- Measurement is a quantified reduction in uncertainty based on your observations
- When you measure, you can never get complete certainty
```

### 201806080958 Uncertainty is a feature of the observer, not the thing being measured.txt

```
Bayesian measurement implies uncertainty is a feature of the observer, not the thing being measured [@hubbard2014measure, p. 34]:

P1) The observer has some level of uncertainty they would like to reduce.

P2) Observations by the observer reduces uncertainty

C1) Therefore, the uncertainty of the object is a characteristic of the observer, not the object.
```

### 202106160905 Estimator.txt

```
An estimator is basically a function that takes sample data as an input, and outputs an estimate for the population parameter.

Sometimes the estimator is the same as the method used to calculate the population parameter, as in with the mean.

From Jones and Tukey [@jones1987collected, p. 633]:

> An estimator is a function of the observations, a specific way of putting them together. It may be specified by an arithmetic formula, like $\bar y = \sum{x_i/n}$, or by words alone, as in directions for finding a sample median by ordering and counting. We distinguish between the estimator and its value, an estimate, obtained from a specific set of data. The variance estimator, $s^2 = \sum{(x_i - \bar x)^2 / (n - 1)}$, yields the estimate 7 from the three observations 2, 3, 7. We say that $s^2$ is an estimator for $\sigma^2$, and we call $\sigma^2$ the estimand. In the numerical example, 7 estimates $\sigma^2$.
```

### 202106191014 Statistical Learning.txt

```
From _An Introduction to Statistical Learning_ [@james2013introduction, p. 16]:

> More generally, supposed that we observe a quantitative response $Y$ and $p$ different predictors, $X_1, X_2, \dots, X_p$. We assume that there is some relationship between $Y$ and $X = (X_1, X_2, \dots, X_p), which can be written in the very general form
>
> $$Y = f(X) + \epsilon$$
>
> Here $f$ is some fixed but unknown function of $X_1, \dots , X_p$, and $\epsilon$ is a random error term, which is independent of $X$ and has mean zero. In this formulation, $f$ represents the systematic information that $X$ provides about $Y$.

Note $f$ is the best that we can do _given only_ $X$. If we were to have more predictor variables in $X$ that provided additional information, we would be able to produce a better $f$ and reduce $\epsilon$. In this sense, the irreducible error $\epsilon$ cannot be reduced given $X$. But if you augment $X$, it _can_ be reduced.

From _An Introduction to Statistical Learning_ [@james2013introduction, p. 17:

> In essence, statistical learning refers to a set of approaches for estimating $f$.
```

### 201908031541 Three criteria are necessary for selecting random samples.txt

```
Three criteria are necessary for selecting random samples: [@watt2002research, p. 62-81]

1. Equal likelihood principle must be met. Every unit must have an equal probability of being chosen.
2. The observer shouldn't be able to predict who will be chosen.
3. It must be possible to choose a sample of every possible combination of people.
```

### 202101080707 The Bootstrap.txt

```
The bootstrap is a resampling technique that allows you to estimate the standard error of a sample statistic [@wilcox2010fundamentals, ch. 6].  As an example, say you sample 100 people and calculate the median height.  You could use bootstrapping to measure the standard error of that median (e.g. how much variation does that median exhibit? or how much uncertainty is there in this measurement of the median?).  The bootstrap works particularly well on non-normal distributions.  It is a robust method.  It is also a very general method.  As an example, you could use it to estimate the standard error of a regression coefficient.
```

### 201908031553 The two major types of error in sampling are sample bias and sample error.txt

```
There are two major types of error in sampling: [@watt2002research, p. 62-81]

1. Sample error is due to randomness. You can reduce sample error by increasing your sample size.
2. Sample bias. Sample bias has two sub-components: Selection bias and response bias.  You introduce selection bias by not having a truly random sample.  Response bias is introduced when people opt-out of your survey.
```

### 202012281937 Statistical Approach to Computational Linguistics.txt

```
The 1980s say the rise of a second approach to computational linguistics [[202012281857 Computational Linguistics]]: the statistical approach (compared to the logical approach [[202012281935 Logical Approach to Computational Linguistics]]).  In the statistical approach, language isn't precise in its meaning.  Rather, the attributes of words, phrases, sentences, and texts follow a distribution.  The statistical approach focuses on analyzing large corpuses, and how words are used in different contexts.
```

### 202101091757 Technical Trends Driving Deep Learning's Success.txt

```
Deep Learning took off after 2012.  Many credit the AlexNet paper [@NIPS2012_c399862d] as kicking off the most recent AI revolution.  In general there are three trends that have driven the recent success of deep learning [@chollet2018deep, p. 20] [@lecun1998gradient, p. 40]:

1. Hardware
2. Datasets and Benchmarks
3. Algorithmic Advances

# Datasets and Benchmarks

There are two primary drivers of increased quantity and availability of data: progress in storage hardware, and the internet.

From François Chollet [@chollet2018deep, p. 21]:

> When it comes to data, in addition to the exponential progress in storage hardware over the past 20 years (following Moore's law), the game changer has been the rise of the internet, making it feasible to collect and distribute very large datasets for machine learning.

Ian Goodfellow credits increasing dataset sizes as ``the most important new development`` that is driving recent success in deep learning [@goodfellow2016deep, p18].  He credits this trend to the digitization of society, which spawned the age of 'big data.'

Additionally, as datasets get larger, models can get larger.  Larger models tend to perform better than smaller ones.  So as datasets get larger, neural networks become more effective [@goodfellow2016deep, p21].
```

