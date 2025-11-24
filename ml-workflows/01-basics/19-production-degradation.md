# Question

Why does an ML model's performance degrade in production?

# Answer

ML models degrade in production because the real-world data they encounter differs from the training data they learned from. The fundamental assumption in statistical learning—that training and test data are drawn from the same distribution—is violated in production environments where data distributions shift over time.

**Primary Causes of Model Degradation:**

**1. Data Drift (Covariate Shift)**
- **Definition**: The distribution of input features (X) changes over time
- **Example**: A fraud detection model trained on 2020 transaction patterns encounters new payment methods in 2023
- **Impact**: Model receives inputs outside its training distribution, leading to poor predictions
- **Relation to ML fundamentals**: Violates the assumption that new data comes from the same distribution as training data

**2. Concept Drift (Label Drift)**
- **Definition**: The relationship between features (X) and target (Y) changes over time
- **Example**: Customer preferences for product recommendations shift due to seasonal trends or cultural changes
- **Impact**: Even if inputs look similar, the learned mapping f(X) → Y becomes incorrect
- **Why it happens**: The true function f that relates X to Y is not static in real-world systems

**3. Upstream Data Issues**
- **Definition**: Changes in data collection, preprocessing, or feature engineering
- **Examples**: Sensor calibration changes, new data source added, feature engineering pipeline modified
- **Impact**: Creates distribution mismatch even if the underlying phenomenon hasn't changed
- **Relation to cross-validation**: Unlike train/test splits which use consistent data processing, production may have pipeline changes

**4. Missing or Out-of-Range Values**
- **Definition**: Production data contains values not seen during training
- **Examples**: New categorical values, features outside training ranges, increased missing data
- **Impact**: Model doesn't know how to handle these cases, leading to degraded predictions

**5. Feedback Loops**
- **Definition**: Model's own predictions influence future training data
- **Example**: A recommendation system changes user behavior, which then becomes the new training data
- **Impact**: Can amplify biases and create distribution shift over time

**Connection to Core ML Concepts:**

From statistical learning theory, we assume: `Y = f(X) + ε`, where f is a fixed function and ε is irreducible error. In production:
- **Data drift** means the distribution P(X) changes
- **Concept drift** means the function f itself changes
- **Both** violate the i.i.d. (independent and identically distributed) assumption underlying cross-validation

Cross-validation estimates generalization error by simulating held-out test data. But it assumes all data comes from the same distribution. Production breaks this assumption, causing the model's actual generalization error to exceed its cross-validation estimates.

**Why Generalization Fails:**

During training, we optimize the model to minimize error on data from distribution P_train. Cross-validation validates this on held-out data from the same P_train. But in production, data comes from P_production ≠ P_train, so the model's learned patterns may not transfer.

**Preventing Overfitting Doesn't Prevent Degradation:**

Techniques like regularization, cross-validation, and limiting model capacity help prevent overfitting to training data. But they don't prevent degradation from distribution shift—a well-generalized model trained on 2020 data will still fail on shifted 2023 data.

---

## Extracts from my notes

### 202101080742 Cross Validation (K-Fold).txt

```
Cross validation is a general technique that estimates how well a model will **generalize** to new data.  K-Fold cross validation is a method that attempts to get the most out of your data.  **The goal is to use all the data for learning while still being able to measure an accurate generalization error** [@russell2010artificial, p. 708].

How does it work?

1. First split the data into train and test sets.  Leave the test set alone until you have your final model.

1. Then take the training data, and partition it into $K$ (usually 5) folds.

1. Train $K$ models:

```code
for i in k:
    train a model on all folds except fold i
    evaluate performance on i
```

4. When complete, you have $K$ performance scores for your model.  These can be used to estimate generalization error, and it's standard deviation.

After evaluating the performance of a model, you can tweak the hyperparameters, and follow the same process again.  Only after you have chosen a final model do you evaluate on

**Note**:  These models are thrown away when you are done.  Usually you would then train your final model over **all** the training data.  Then do your final evaluation of the model on the test set, only using the test set once.


K-Fold Cross validation works particularly well when you have a small dataset because it minimizes the impact of a single split.  From François Chollet [@chollet2018deep, p. 99]:

> This method is helpful when the performance of your model shows significant variance based on your train-test split.
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

## Gaps filled by me (not from notes)

I do not have specific notes on production ML systems, model drift, data drift, concept drift, or MLOps practices. The entire answer explaining the causes of production model degradation (data drift, concept drift, upstream issues, feedback loops) was synthesized from ML production best practices and systems engineering knowledge. My notes on cross-validation and statistical learning provided the theoretical foundation for understanding why models generalize, which I connected to the production context by explaining how distribution shift violates the assumptions underlying these validation techniques.
