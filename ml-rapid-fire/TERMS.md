# ML Interview Terms (Comprehensive)

**Source:** Bottom-up discovery from PDFs, markdown files, and 240+ zettelkasten notes

---

## 1. ML Fundamentals

### Core Concepts
- [ ] Bias-Variance Trade-off
- [ ] Classification vs Regression
- [ ] Discriminative vs Generative Models
- [ ] Empirical Risk
- [ ] Generalization / Generalization Error
- [ ] Hypothesis Space
- [ ] Model Complexity
- [ ] No Free Lunch Theorem
- [ ] Occam's Razor
- [ ] Overfitting / Underfitting
- [ ] Parameters vs Hyperparameters
- [ ] Parametric vs Non-parametric Models
- [ ] Supervised / Unsupervised / Semi-supervised / Self-supervised Learning
- [ ] Training vs Inference

### Model Training
- [ ] Batch Size
- [ ] Convergence / Convergence Criteria
- [ ] Cost Surface
- [ ] Epoch
- [ ] Iteration
- [ ] Online Learning
- [ ] Warm Start / Cold Start

---

## 2. Classical ML

### Linear Models
- [ ] Elastic Net
- [ ] Intercept / Bias Term
- [ ] Interaction Term
- [ ] L1 Regularization (Lasso)
- [ ] L2 Regularization (Ridge)
- [ ] Linear Discriminant Analysis (LDA)
- [ ] Linear Regression
- [ ] Logistic Regression (Binary, Multinomial, One-vs-Rest)
- [ ] Ordinary Least Squares (OLS)
- [ ] Polynomial Regression
- [ ] Regression Coefficients / Slope

### Regression Diagnostics
- [ ] Adjusted R-Squared
- [ ] Collinearity / Multicollinearity
- [ ] Constant Variance Assumption
- [ ] Fitted Values
- [ ] Heteroscedasticity / Homoscedasticity
- [ ] Independent Errors Assumption
- [ ] Linearity Assumption
- [ ] Normality Assumption
- [ ] R-Squared
- [ ] Residual Plots
- [ ] Residuals
- [ ] Variance Inflation Factor (VIF)

### Variable Selection
- [ ] Backward Elimination
- [ ] Best Subset Selection
- [ ] Forward Selection
- [ ] Stepwise Regression
- [ ] Variable Selection Problem

### Specialized Regression
- [ ] Hurdle Regression
- [ ] Negative Binomial Regression
- [ ] Poisson Regression
- [ ] Quasi-Poisson Regression
- [ ] Zero-Inflated Negative Binomial Regression
- [ ] Zero-Inflated Poisson Regression
- [ ] Zero-Truncated Poisson Regression

### Tree-Based Methods
- [ ] AdaBoost (Adaptive Boosting)
- [ ] Bagging (Bootstrap Aggregating)
- [ ] Boosting / Hypothesis Boosting
- [ ] CART (Classification and Regression Trees)
- [ ] Decision Trees
- [ ] Entropy
- [ ] Gini Impurity / Gini Index
- [ ] Gradient Boosting
- [ ] Information Gain
- [ ] Leaf Nodes
- [ ] LightGBM
- [ ] Node Splitting
- [ ] Random Forest
- [ ] Strong Learner
- [ ] Tree Depth
- [ ] Tree Pruning
- [ ] Weak Learner
- [ ] XGBoost

### Ensemble Methods
- [ ] Ensemble Learning
- [ ] Model Averaging
- [ ] Stacking
- [ ] Voting Classifier

### Support Vector Machines
- [ ] C Parameter
- [ ] Hard Margin
- [ ] Kernel Trick
- [ ] Linear Kernel
- [ ] Platt Scaling
- [ ] Polynomial Kernel
- [ ] RBF Kernel (Radial Basis Function)
- [ ] Slack Variable
- [ ] Soft Margin Classification
- [ ] Support Vector Classifier
- [ ] Support Vectors

### Instance-Based Methods
- [ ] Imputation (k-NN)
- [ ] k-Nearest Neighbors (k-NN)
- [ ] k-NN Neighborhood Size
- [ ] Radius-Based Nearest Neighbor

### Clustering
- [ ] Agglomerative Clustering
- [ ] DBSCAN
- [ ] Gaussian Mixture Models (GMM)
- [ ] GrabCut
- [ ] Hierarchical Clustering
- [ ] k-Means Clustering
- [ ] Meanshift Clustering
- [ ] Silhouette Coefficients

### Dimensionality Reduction
- [ ] Curse of Dimensionality
- [ ] Kernel PCA
- [ ] PCA (Principal Component Analysis)
- [ ] Principal Components
- [ ] t-SNE
- [ ] UMAP

### Probabilistic Models
- [ ] Bayesian Inference
- [ ] Bayesian Methods
- [ ] EM Algorithm (Expectation-Maximization)
- [ ] Gaussian Naive Bayes
- [ ] Hidden Markov Models (HMM)
- [ ] Likelihood Function
- [ ] Maximum Likelihood Estimation (MLE)
- [ ] Multinomial Naive Bayes
- [ ] Naive Bayes
- [ ] Perceptron / Perceptron Learning
- [ ] Posterior Probability
- [ ] Prior Probability

---

## 3. Deep Learning

### Architectures
- [ ] Autoencoder
- [ ] Bidirectional RNNs
- [ ] Convolutional Neural Networks (CNNs)
- [ ] Dense Layers / Fully Connected Layers
- [ ] Encoder-Decoder Architecture
- [ ] Feedforward Neural Networks
- [ ] GANs (Generative Adversarial Networks)
- [ ] Gated Recurrent Unit (GRU)
- [ ] Hidden Layer
- [ ] Inception Modules / Layers
- [ ] Input Layer
- [ ] LSTM (Long Short-Term Memory)
- [ ] Network in Network
- [ ] Neural Network Layers
- [ ] Neuron
- [ ] Output Layer
- [ ] Recurrent Neural Networks (RNNs)
- [ ] Residual Connections / Skip Connections
- [ ] Sequence-to-Sequence Models (Seq2Seq)
- [ ] Siamese Networks
- [ ] Transformers
- [ ] Variational Autoencoder (VAE)
- [ ] Wide vs Deep Networks

### CNN Specifics
- [ ] 1x1 Convolution Layer
- [ ] AlexNet
- [ ] Convolutional Kernels / Filters
- [ ] Convolutional Layer
- [ ] Feature Maps
- [ ] Global Average Pooling
- [ ] GoogLeNet
- [ ] L2 Pooling
- [ ] LeNet-5
- [ ] Local Receptive Fields
- [ ] Max Pooling
- [ ] Padding (Zero, Valid, Same)
- [ ] Pooling Layer
- [ ] Receptive Field
- [ ] ResNet
- [ ] Stride
- [ ] Translation Invariance
- [ ] VGG
- [ ] ZFNet

### Activation Functions
- [ ] ELU
- [ ] Leaky ReLU
- [ ] Linear Activation
- [ ] Noisy ReLU
- [ ] ReLU (Rectified Linear Unit)
- [ ] Saturation / Saturated Neuron
- [ ] Sigmoid
- [ ] Softmax
- [ ] Softplus
- [ ] Tanh
- [ ] Threshold Activation
- [ ] Unit-Step Activation

### Optimization
- [ ] Adam (Adaptive Moment Estimation)
- [ ] Adadelta
- [ ] Adagrad
- [ ] Backpropagation
- [ ] Chain Rule
- [ ] Convergence
- [ ] Dying ReLU / Dead Neuron
- [ ] Exploding Gradients
- [ ] Gradient
- [ ] Gradient Clipping
- [ ] Gradient Descent (Batch)
- [ ] Learning Rate
- [ ] Learning Rate Schedule / Decay
- [ ] Local Minima
- [ ] Mini-Batch Gradient Descent
- [ ] Momentum / Momentum Optimizer
- [ ] Nesterov Accelerated Gradient (NAG)
- [ ] Newton's Method
- [ ] Plateau
- [ ] RMSprop
- [ ] Saddle Points
- [ ] Stochastic Gradient Descent (SGD)
- [ ] Vanishing Gradients

### Regularization (DL)
- [ ] Batch Normalization
- [ ] Co-adaptation
- [ ] Data Augmentation
- [ ] Dropout
- [ ] Early Stopping
- [ ] Internal Covariate Shift
- [ ] Label Smoothing
- [ ] Layer Normalization
- [ ] Max-Norm Regularization
- [ ] Norm Penalties
- [ ] Parameter Norm
- [ ] Parameter Sharing / Weight Tying
- [ ] Weight Decay
- [ ] Weight Initialization (Xavier, He, Gaussian)

### Training Concepts
- [ ] Backward Pass
- [ ] Checkpoint
- [ ] Error Term / Delta
- [ ] Fine-Tuning
- [ ] Forward Pass / Forward Propagation
- [ ] Gradient Checking
- [ ] Gradient Update
- [ ] Teacher Forcing
- [ ] Transfer Learning
- [ ] Weight Update

---

## 4. NLP & Transformers

### Text Processing
- [ ] Bag of Words Model
- [ ] Embedding Layer
- [ ] GloVe
- [ ] Pre-trained Embeddings
- [ ] Stemming
- [ ] Stop Words
- [ ] Text Vectorization
- [ ] TF-IDF
- [ ] Tokenization
- [ ] Vocabulary
- [ ] Word Counts
- [ ] Word Embeddings
- [ ] Word2Vec

### Sequence Models
- [ ] Beam Search
- [ ] Greedy Decoding
- [ ] Language Model
- [ ] Machine Translation Model
- [ ] Sequence Modeling

### Attention Mechanisms
- [ ] Attention Distribution
- [ ] Attention Mechanism
- [ ] Attention Scores
- [ ] Bahdanau Attention
- [ ] Context Vector
- [ ] Luong Attention
- [ ] Multi-Head Attention
- [ ] Query, Key, Value
- [ ] Self-Attention

### Transformers & LLMs
- [ ] BERT
- [ ] ELMo
- [ ] GPT
- [ ] Positional Embeddings / Positional Encoding
- [ ] RoBERTa
- [ ] XLNet

### NLP Tasks
- [ ] Aspect-Based Sentiment Analysis
- [ ] Named Entity Recognition
- [ ] Sentiment Analysis
- [ ] Text Classification

---

## 5. Reinforcement Learning

### Core Concepts
- [ ] Action Space
- [ ] Agent
- [ ] Bellman Equation / Bellman Optimality Equation
- [ ] Discount Factor (Gamma)
- [ ] Dynamics (Environment)
- [ ] Environment
- [ ] Episode
- [ ] Exploration vs Exploitation
- [ ] Markov Decision Process (MDP)
- [ ] Policy / Policy Function
- [ ] Reinforcement Learning
- [ ] Reward Function / Reward Signal
- [ ] State Space
- [ ] Terminal State
- [ ] Transition Probability

### Value Functions
- [ ] Action-Value Function (Q-Function)
- [ ] State-Value Function
- [ ] Value Function

### Algorithms
- [ ] Deep Q-Learning (DQN)
- [ ] Double Q-Learning
- [ ] Dynamic Programming (RL)
- [ ] Expected SARSA
- [ ] Monte Carlo Methods
- [ ] Monte Carlo Tree Search (MCTS)
- [ ] N-step Methods
- [ ] Off-Policy Learning
- [ ] On-Policy Learning
- [ ] Policy Evaluation
- [ ] Policy Improvement
- [ ] Policy Iteration
- [ ] Q-Learning
- [ ] REINFORCE (Vanilla Policy Gradients)
- [ ] SARSA
- [ ] Temporal Difference (TD) Learning
- [ ] Value Iteration

### Exploration Strategies
- [ ] Contextual Bandits
- [ ] Cross-Entropy Method (CEM)
- [ ] Epsilon-Greedy Policy
- [ ] Greedy Action Selection
- [ ] K-Armed Bandit Problem
- [ ] Sample-Average Method
- [ ] Upper Confidence Bound (UCB)

### RL Categories
- [ ] Model-Based vs Model-Free RL
- [ ] Policy-Based vs Value-Based RL

---

## 6. Model Evaluation

### Classification Metrics
- [ ] Accuracy
- [ ] Area Under Curve (AUC)
- [ ] Brier Score
- [ ] Confusion Matrix
- [ ] F1 Score
- [ ] False Positive Rate
- [ ] Fowlkes-Mallows
- [ ] Matthews Correlation Coefficient
- [ ] Precision
- [ ] Recall / Sensitivity
- [ ] ROC Curve
- [ ] True Positive Rate
- [ ] Youden's J Statistic

### Regression Metrics
- [ ] Explained Sum of Squares (ESS)
- [ ] Mean Absolute Error (MAE)
- [ ] Mean Squared Error (MSE)
- [ ] Residual Sum of Squares (RSS)
- [ ] Sum of Squares due to Regression (SSR)
- [ ] Total Sum of Squares (TSS)

### Loss Functions
- [ ] Binary Cross-Entropy
- [ ] Categorical Cross-Entropy
- [ ] Cost Function
- [ ] Cross-Entropy
- [ ] Hamming Loss
- [ ] Hinge Loss
- [ ] Log-Likelihood Cost
- [ ] Loss Function
- [ ] Quadratic Cost
- [ ] Triplet Loss
- [ ] Zero-One Loss

### Model Selection
- [ ] AIC (Akaike Information Criterion)
- [ ] BIC (Bayesian Information Criterion)
- [ ] Bootstrap
- [ ] Cross-Validation (K-Fold, Leave-One-Out)
- [ ] Grid Search
- [ ] Hold-Out Validation
- [ ] Hyperparameter Tuning
- [ ] Learning Curve
- [ ] Mallow's Cp
- [ ] Model Selection
- [ ] Out-of-Bag Error
- [ ] Prediction Risk
- [ ] Randomized Search
- [ ] Stratified Sampling
- [ ] Test / Training / Validation Sets
- [ ] Validation Curve

### Error Analysis
- [ ] Bayes Error
- [ ] Bias
- [ ] Error Types (Type I, Type II)
- [ ] Generalization Error
- [ ] Test Error
- [ ] Training Error
- [ ] Variance

---

## 7. Probability & Statistics

### Probability Basics
- [ ] Bayes' Theorem
- [ ] Combination
- [ ] Conditional Probability
- [ ] Events
- [ ] I.I.D. (Independent and Identically Distributed)
- [ ] Independence
- [ ] Notions of Probability
- [ ] Odds / Odds Ratio
- [ ] Outcome
- [ ] Sample Space

### Random Variables
- [ ] Continuous Random Variable
- [ ] Discrete Random Variable
- [ ] Expected Value / Expectation
- [ ] Moments (First, Second)
- [ ] Random Variable
- [ ] Variance

### Distributions
- [ ] Bernoulli Distribution
- [ ] Binomial Distribution
- [ ] Chi-Square Distribution
- [ ] Cumulative Distribution Function (CDF)
- [ ] Data-Generating Distribution
- [ ] Exponential Distribution
- [ ] F-Distribution
- [ ] Geometric Distribution
- [ ] Negative Binomial Distribution
- [ ] Normal Distribution (Gaussian)
- [ ] Overdispersion / Underdispersion
- [ ] Pareto Distribution
- [ ] Poisson Distribution
- [ ] Probability Density Function (PDF)
- [ ] Probability Mass Function (PMF)
- [ ] Standard Normal Distribution
- [ ] Uniform Distribution

### Descriptive Statistics
- [ ] Anscombe's Quartet
- [ ] Correlation
- [ ] Covariance
- [ ] Interquartile Range
- [ ] Kurtosis
- [ ] Mean / Median / Mode
- [ ] Pearson's Correlation
- [ ] Percentile / Quartile
- [ ] Simpson's Paradox
- [ ] Skewness
- [ ] Standard Deviation
- [ ] Standard Error of the Mean
- [ ] Variance

### Statistical Inference
- [ ] Central Limit Theorem
- [ ] Chi-Squared Test
- [ ] Confidence Intervals
- [ ] Consistency
- [ ] Degrees of Freedom
- [ ] Estimator
- [ ] F-Statistic
- [ ] Heteroskedasticity
- [ ] Homogeneity
- [ ] Hypothesis Testing
- [ ] Instrumental Variables
- [ ] Maximum Likelihood Estimation (MLE)
- [ ] P-Value
- [ ] Significance Level
- [ ] T-Statistic
- [ ] Weak Stationarity

---

## 8. Linear Algebra

### Vectors & Matrices
- [ ] Affine Transformation
- [ ] Dot Product / Inner Product
- [ ] Element-wise Product (Hadamard)
- [ ] Matrix
- [ ] Matrix Multiplication
- [ ] Norm (L1, L2)
- [ ] Transpose
- [ ] Vector

### Decomposition
- [ ] Eigenvalues / Eigenvectors
- [ ] Matrix Decomposition
- [ ] PCA (Principal Component Analysis)
- [ ] Singular Value Decomposition (SVD)

### Tensors
- [ ] Broadcasting
- [ ] Tensors
- [ ] Vectorization

---

## 9. Calculus & Optimization

### Differentiation
- [ ] Chain Rule
- [ ] Derivative
- [ ] Gradient (Nabla)
- [ ] Hessian
- [ ] Jacobian
- [ ] Partial Derivatives
- [ ] Product Rule
- [ ] Quotient Rule

### Optimization Theory
- [ ] Convex Optimization
- [ ] Global Optimum
- [ ] Lagrange Multipliers
- [ ] Local Optimum
- [ ] Non-Convex Optimization

### Numerical Methods
- [ ] Automatic Differentiation
- [ ] Cubic Splines
- [ ] Finite Differences
- [ ] Gradient Checking
- [ ] Interpolation
- [ ] Newton-Raphson
- [ ] Numerical Differentiation
- [ ] Symbolic Differentiation

---

## 10. Data Engineering

### Feature Engineering
- [ ] Categorical Feature
- [ ] Design Matrix
- [ ] Encoding (One-Hot, Label, Ordinal)
- [ ] Feature Extraction
- [ ] Feature Importance
- [ ] Feature Selection
- [ ] SHAP Values
- [ ] Variance Thresholding

### Scaling & Normalization
- [ ] Min-Max Scaling
- [ ] Normalization
- [ ] Standardization (Z-Score)
- [ ] Whitening

### Missing Data
- [ ] Imputation
- [ ] Interpolation
- [ ] Missing At Random (MAR)
- [ ] Missing Completely At Random (MCAR)
- [ ] Missing Not At Random (MNAR)

### Imbalanced Data
- [ ] Downsampling
- [ ] Handling Outliers
- [ ] Imbalanced Classes
- [ ] Outlier Detection
- [ ] SMOTE
- [ ] Tomek Link
- [ ] Upsampling

### Data Preprocessing
- [ ] Data Augmentation
- [ ] Data Pipeline
- [ ] ETL
- [ ] Preprocessing
- [ ] Train-Test Split

---

## 11. Information Theory

- [ ] Bits / Nats
- [ ] Cross-Entropy
- [ ] Entropy
- [ ] Information Gain
- [ ] KL Divergence (Kullback-Leibler)
- [ ] Mutual Information
- [ ] Perplexity

---

## 12. Quantitative Finance

### Returns & Risk
- [ ] Alpha
- [ ] Beta
- [ ] CAPM
- [ ] Continuously Compounded Returns
- [ ] Drawdown
- [ ] Expected Shortfall
- [ ] Factor Models
- [ ] Log Returns
- [ ] Momentum
- [ ] Portfolio Optimization
- [ ] Risk Premium
- [ ] Sharpe Ratio
- [ ] Simple Returns
- [ ] Value at Risk (VaR)
- [ ] Volatility

### Options & Derivatives
- [ ] Arbitrage
- [ ] Black-Scholes Model
- [ ] Delta Hedging
- [ ] Greeks (Delta, Gamma, Vega, Theta)
- [ ] Option Pricing
- [ ] Put-Call Parity
- [ ] Risk-Neutral Measure
- [ ] Term Structure
- [ ] Volatility Smile

### Time Series
- [ ] ARIMA
- [ ] Autocorrelation
- [ ] Backtesting
- [ ] Cointegration
- [ ] Forecasting
- [ ] GARCH
- [ ] Mean Reversion
- [ ] Seasonality
- [ ] Stationarity
- [ ] Time Series Analysis
- [ ] Trend
- [ ] Walk-Forward Analysis

### Stochastic Processes
- [ ] Brownian Motion
- [ ] Geometric Brownian Motion
- [ ] Ito's Lemma
- [ ] Markov Chains
- [ ] Martingales
- [ ] Monte Carlo Simulation
- [ ] Stochastic Processes

---

## 13. Computer Vision

### Tasks
- [ ] Edge Detection
- [ ] Image Classification
- [ ] Image Segmentation
- [ ] Object Detection

### Techniques
- [ ] Corner Detection
- [ ] Data Augmentation (Images)
- [ ] Feature Extraction
- [ ] Image Preprocessing
- [ ] Rotation Invariance
- [ ] Scale Invariance
- [ ] Shift Invariance

### Model Interpretability
- [ ] Attention Visualization
- [ ] Class Activation Maps (CAM)
- [ ] Grad-CAM
- [ ] Saliency Maps

---

## 14. Advanced Topics

### Anomaly Detection
- [ ] Isolation Forest
- [ ] Outlier Detection

### Specialized Learning
- [ ] Contrastive Learning
- [ ] Curriculum Learning
- [ ] Few-Shot Learning
- [ ] Meta-Learning
- [ ] Metric Learning
- [ ] Multi-Task Learning
- [ ] One-Shot Learning
- [ ] Zero-Shot Learning

### Representation Learning
- [ ] Dense Representation
- [ ] Distributed Representation
- [ ] Latent Space / Latent Variable
- [ ] Manifold
- [ ] Representation Learning
- [ ] Sparse Representation

### Model Interpretability
- [ ] Black Box Models
- [ ] Explainable AI (XAI)
- [ ] Feature Importance
- [ ] Interpretable Models
- [ ] LIME
- [ ] Model Introspection
- [ ] SHAP Values
- [ ] White Box Models

---

## 15. Systems & Implementation

### Computation
- [ ] Computational Graph
- [ ] Distributed Training
- [ ] GPU Acceleration
- [ ] Memory Optimization
- [ ] Parallelization

### ML Ops
- [ ] Benchmarking
- [ ] Model Saving / Loading
- [ ] Profiling
- [ ] Production Degradation
- [ ] Production Performance

### Data Systems
- [ ] Batch Processing
- [ ] Out-of-Core Processing
- [ ] Sparsity
- [ ] Stream Processing

---

**Total: ~500+ unique terms**
