# ML Interview Dojo

Personal repository for preparing for machine learning interviews.

## Source Material

ML questions are from [Machine Learning Interviews Book](https://huyenchip.com/ml-interviews-book/) by Chip Huyen.
Math & Quant questions are curated for market-making and quant-adjacent roles.

## Progress Scorecard

### Overall Mastery

```
[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/347)
```

### Card Status

| Status | Count | Percentage |
|--------|-------|------------|
| 🏆 Mastered | 0 | 0.0% |
| 💪 Learning | 0 | 0.0% |
| ⭐ New | 347 | 100.0% |
| **Total** | **347** | **100%** |


## Quick Start

```bash
# Start a review session
python3 srs.py review

# View your stats
python3 srs.py stats

# Update this README
python3 scripts/generate_readme.py
```

## How the SRS Works

This uses a **queue-based spaced repetition system** (not date-based like Anki):

- **No due dates**: Cards are prioritized in a smart queue based on performance
- **No pile-up**: Come back after months and continue right where you left off
- **Adaptive**: Struggles with a card? It gets higher priority automatically
- **Mastery tracking**: Cards graduate from New → Learning → Mastered

**Mastery Criteria**: 3+ consecutive reviews with score ≥4, spaced at least 1 hour apart

## Status Legend

- 🏆 **Mastered**: Consistently perfect recall
- 💪 **Strong**: Average score ≥4.0, still in practice
- 👍 **Learning**: Average score ≥3.0, making progress
- 📖 **Practicing**: Reviewed but needs more work
- ⭐ **New**: Not yet reviewed

## ML Rapid Fire


### Classical Ml

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/62) | 🏆 0 | 💪 0 | ⭐ 62

- ⭐ [AdaBoost](ml-rapid-fire/classical-ml/AdaBoost.pdf): AdaBoost
- ⭐ [Aggomerative_Clustering](ml-rapid-fire/classical-ml/Aggomerative_Clustering.pdf): Aggomerative Clustering
- ⭐ [Alpha_In_Ridge_Regression](ml-rapid-fire/classical-ml/Alpha_In_Ridge_Regression.pdf): Alpha In Ridge Regression
- ⭐ [Bagging](ml-rapid-fire/classical-ml/Bagging.pdf): Bagging
- ⭐ [Bayesian_Methods_Pros_And_Cons](ml-rapid-fire/classical-ml/Bayesian_Methods_Pros_And_Cons.pdf): Bayesian Methods Pros And Cons
- ⭐ [Boosting](ml-rapid-fire/classical-ml/Boosting.pdf): Boosting
- ⭐ [C](ml-rapid-fire/classical-ml/C.pdf): C
- ⭐ [Classification](ml-rapid-fire/classical-ml/Classification.pdf): Classification
- ⭐ [Curse_Of_Dimensionality](ml-rapid-fire/classical-ml/Curse_Of_Dimensionality.pdf): Curse Of Dimensionality
- ⭐ [DBSCAN](ml-rapid-fire/classical-ml/DBSCAN.pdf): DBSCAN
- ⭐ [Decision_Boundary](ml-rapid-fire/classical-ml/Decision_Boundary.pdf): Decision Boundary
- ⭐ [Decision_Tree_Regression](ml-rapid-fire/classical-ml/Decision_Tree_Regression.pdf): Decision Tree Regression
- ⭐ [Decision_Trees](ml-rapid-fire/classical-ml/Decision_Trees.pdf): Decision Trees
- ⭐ [Does-k-NN-Learn](ml-rapid-fire/classical-ml/Does-k-NN-Learn.pdf): Does k NN Learn
- ⭐ [ElasticNet](ml-rapid-fire/classical-ml/ElasticNet.pdf): ElasticNet
- ⭐ [Ensemble_Methods](ml-rapid-fire/classical-ml/Ensemble_Methods.pdf): Ensemble Methods
- ⭐ [Finding_Linear_Regression_Parameters](ml-rapid-fire/classical-ml/Finding_Linear_Regression_Parameters.pdf): Finding Linear Regression Parameters
- ⭐ [Gaussian_Naive_Bayes_Classifier](ml-rapid-fire/classical-ml/Gaussian_Naive_Bayes_Classifier.pdf): Gaussian Naive Bayes Classifier
- ⭐ [Gini_Index](ml-rapid-fire/classical-ml/Gini_Index.pdf): Gini Index
- ⭐ [Grabcut](ml-rapid-fire/classical-ml/Grabcut.pdf): Grabcut
- ⭐ [Handling_Imbalanced_Classes_In_Support_Vector_Machines](ml-rapid-fire/classical-ml/Handling_Imbalanced_Classes_In_Support_Vector_Machines.pdf): Handling Imbalanced Classes In Support Vector Machines
- ⭐ [Imputation_Using_k-NN](ml-rapid-fire/classical-ml/Imputation_Using_k-NN.pdf): Imputation Using k NN
- ⭐ [Interaction_Term](ml-rapid-fire/classical-ml/Interaction_Term.pdf): Interaction Term
- ⭐ [Intercept_Term](ml-rapid-fire/classical-ml/Intercept_Term.pdf): Intercept Term
- ⭐ [Issues_With_Platt_Scaling](ml-rapid-fire/classical-ml/Issues_With_Platt_Scaling.pdf): Issues With Platt Scaling
- ⭐ [K-Means_Clustering](ml-rapid-fire/classical-ml/K-Means_Clustering.pdf): K Means Clustering
- ⭐ [K-NN_Neighborhood_Size](ml-rapid-fire/classical-ml/K-NN_Neighborhood_Size.pdf): K NN Neighborhood Size
- ⭐ [K-Nearest_Neighbors_Tips_And_Tricks](ml-rapid-fire/classical-ml/K-Nearest_Neighbors_Tips_And_Tricks.pdf): K Nearest Neighbors Tips And Tricks
- ⭐ [Kernel_PCA](ml-rapid-fire/classical-ml/Kernel_PCA.pdf): Kernel PCA
- ⭐ [Kernel_Trick](ml-rapid-fire/classical-ml/Kernel_Trick.pdf): Kernel Trick
- ⭐ [Lasso_For_Feature_Selection](ml-rapid-fire/classical-ml/Lasso_For_Feature_Selection.pdf): Lasso For Feature Selection
- ⭐ [Linear_Discriminant_Analysis_For_Dimensionality_Reduction](ml-rapid-fire/classical-ml/Linear_Discriminant_Analysis_For_Dimensionality_Reduction.pdf): Linear Discriminant Analysis For Dimensionality Reduction
- ⭐ [Linearly_Separable](ml-rapid-fire/classical-ml/Linearly_Separable.pdf): Linearly Separable
- ⭐ [Logistic_Regression](ml-rapid-fire/classical-ml/Logistic_Regression.pdf): Logistic Regression
- ⭐ [Logistic_Regression_Vs_Linear_Regression](ml-rapid-fire/classical-ml/Logistic_Regression_Vs_Linear_Regression.pdf): Logistic Regression Vs Linear Regression
- ⭐ [Logistic_Sigmoid_Function](ml-rapid-fire/classical-ml/Logistic_Sigmoid_Function.pdf): Logistic Sigmoid Function
- ⭐ [Meanshift_Clustering_By_Analogy](ml-rapid-fire/classical-ml/Meanshift_Clustering_By_Analogy.pdf): Meanshift Clustering By Analogy
- ⭐ [Multinomial_Logistic_Regression](ml-rapid-fire/classical-ml/Multinomial_Logistic_Regression.pdf): Multinomial Logistic Regression
- ⭐ [Non-Parametric_Methods](ml-rapid-fire/classical-ml/Non-Parametric_Methods.pdf): Non Parametric Methods
- ⭐ [One-Vs-Rest_Logistic_Regression](ml-rapid-fire/classical-ml/One-Vs-Rest_Logistic_Regression.pdf): One Vs Rest Logistic Regression
- ⭐ [Ordinary_Least_Squares](ml-rapid-fire/classical-ml/Ordinary_Least_Squares.pdf): Ordinary Least Squares
- ⭐ [Parametric_Modeling](ml-rapid-fire/classical-ml/Parametric_Modeling.pdf): Parametric Modeling
- ⭐ [Perceptron](ml-rapid-fire/classical-ml/Perceptron.pdf): Perceptron
- ⭐ [Perceptron_Learning](ml-rapid-fire/classical-ml/Perceptron_Learning.pdf): Perceptron Learning
- ⭐ [Platt_Scaling](ml-rapid-fire/classical-ml/Platt_Scaling.pdf): Platt Scaling
- ⭐ [Polynomial_Regression](ml-rapid-fire/classical-ml/Polynomial_Regression.pdf): Polynomial Regression
- ⭐ [Principal_Component_Analysis](ml-rapid-fire/classical-ml/Principal_Component_Analysis.pdf): Principal Component Analysis
- ⭐ [Principal_Components](ml-rapid-fire/classical-ml/Principal_Components.pdf): Principal Components
- ⭐ [Radius-Based_Nearest_Neighbor_Classifier](ml-rapid-fire/classical-ml/Radius-Based_Nearest_Neighbor_Classifier.pdf): Radius Based Nearest Neighbor Classifier
- ⭐ [Random_Forest](ml-rapid-fire/classical-ml/Random_Forest.pdf): Random Forest
- ⭐ [Regression](ml-rapid-fire/classical-ml/Regression.pdf): Regression
- ⭐ [Ridge_Regression](ml-rapid-fire/classical-ml/Ridge_Regression.pdf): Ridge Regression
- ⭐ [SVC_Radial_Basis_Function_Kernel](ml-rapid-fire/classical-ml/SVC_Radial_Basis_Function_Kernel.pdf): SVC Radial Basis Function Kernel
- ⭐ [Selecting_Number_Of_Components_In_PCA](ml-rapid-fire/classical-ml/Selecting_Number_Of_Components_In_PCA.pdf): Selecting Number Of Components In PCA
- ⭐ [Slack_Variable_In_Soft-Margin_SVM](ml-rapid-fire/classical-ml/Slack_Variable_In_Soft-Margin_SVM.pdf): Slack Variable In Soft Margin SVM
- ⭐ [Supervised_Vs_Unsupervised](ml-rapid-fire/classical-ml/Supervised_Vs_Unsupervised.pdf): Supervised Vs Unsupervised
- ⭐ [Support_Vector_Classifier](ml-rapid-fire/classical-ml/Support_Vector_Classifier.pdf): Support Vector Classifier
- ⭐ [Support_Vector_Machine_Soft-Margin_Classification](ml-rapid-fire/classical-ml/Support_Vector_Machine_Soft-Margin_Classification.pdf): Support Vector Machine Soft Margin Classification
- ⭐ [Support_Vectors](ml-rapid-fire/classical-ml/Support_Vectors.pdf): Support Vectors
- ⭐ [The_Random_In_Random_Forest](ml-rapid-fire/classical-ml/The_Random_In_Random_Forest.pdf): The Random In Random Forest
- ⭐ [Weak_Learners](ml-rapid-fire/classical-ml/Weak_Learners.pdf): Weak Learners
- ⭐ [k-Nearest_Neighbors](ml-rapid-fire/classical-ml/k-Nearest_Neighbors.pdf): k Nearest Neighbors

### Data Engineering

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/35) | 🏆 0 | 💪 0 | ⭐ 35

- ⭐ [Bag_Of_Words](ml-rapid-fire/data-engineering/Bag_Of_Words.pdf): Bag Of Words
- ⭐ [Categorical_Feature](ml-rapid-fire/data-engineering/Categorical_Feature.pdf): Categorical Feature
- ⭐ [Chi-Squared_For_Feature_Selection](ml-rapid-fire/data-engineering/Chi-Squared_For_Feature_Selection.pdf): Chi Squared For Feature Selection
- ⭐ [Dataset_Augmentation](ml-rapid-fire/data-engineering/Dataset_Augmentation.pdf): Dataset Augmentation
- ⭐ [Design_Matrix](ml-rapid-fire/data-engineering/Design_Matrix.pdf): Design Matrix
- ⭐ [Downsampling](ml-rapid-fire/data-engineering/Downsampling.pdf): Downsampling
- ⭐ [Effect_Of_One-Hot_On_Feature_Importance](ml-rapid-fire/data-engineering/Effect_Of_One-Hot_On_Feature_Importance.pdf): Effect Of One Hot On Feature Importance
- ⭐ [Encoding_Ordinal_Categorical_Features](ml-rapid-fire/data-engineering/Encoding_Ordinal_Categorical_Features.pdf): Encoding Ordinal Categorical Features
- ⭐ [Feature_Importance](ml-rapid-fire/data-engineering/Feature_Importance.pdf): Feature Importance
- ⭐ [Feature_Selection_Strategies](ml-rapid-fire/data-engineering/Feature_Selection_Strategies.pdf): Feature Selection Strategies
- ⭐ [Handling_Outliers](ml-rapid-fire/data-engineering/Handling_Outliers.pdf): Handling Outliers
- ⭐ [Imputing_Missing_Values](ml-rapid-fire/data-engineering/Imputing_Missing_Values.pdf): Imputing Missing Values
- ⭐ [Interpolation](ml-rapid-fire/data-engineering/Interpolation.pdf): Interpolation
- ⭐ [Joins](ml-rapid-fire/data-engineering/Joins.pdf): Joins
- ⭐ [MinMax_Scaling](ml-rapid-fire/data-engineering/MinMax_Scaling.pdf): MinMax Scaling
- ⭐ [Missing_At_Random](ml-rapid-fire/data-engineering/Missing_At_Random.pdf): Missing At Random
- ⭐ [Missing_Completely_At_Random](ml-rapid-fire/data-engineering/Missing_Completely_At_Random.pdf): Missing Completely At Random
- ⭐ [Missing_Not_At_Random](ml-rapid-fire/data-engineering/Missing_Not_At_Random.pdf): Missing Not At Random
- ⭐ [Normalizing_Observations](ml-rapid-fire/data-engineering/Normalizing_Observations.pdf): Normalizing Observations
- ⭐ [One-Hot_Encoding](ml-rapid-fire/data-engineering/One-Hot_Encoding.pdf): One Hot Encoding
- ⭐ [Out-Of-Core](ml-rapid-fire/data-engineering/Out-Of-Core.pdf): Out Of Core
- ⭐ [Outlier](ml-rapid-fire/data-engineering/Outlier.pdf): Outlier
- ⭐ [Sparsity](ml-rapid-fire/data-engineering/Sparsity.pdf): Sparsity
- ⭐ [Standardization](ml-rapid-fire/data-engineering/Standardization.pdf): Standardization
- ⭐ [Stemming_Words](ml-rapid-fire/data-engineering/Stemming_Words.pdf): Stemming Words
- ⭐ [Stop_Words](ml-rapid-fire/data-engineering/Stop_Words.pdf): Stop Words
- ⭐ [Strategies_For_Highly_Imbalanced_Classes](ml-rapid-fire/data-engineering/Strategies_For_Highly_Imbalanced_Classes.pdf): Strategies For Highly Imbalanced Classes
- ⭐ [TF-IDF](ml-rapid-fire/data-engineering/TF-IDF.pdf): TF IDF
- ⭐ [Thresholding_Categorical_Feature_Variance](ml-rapid-fire/data-engineering/Thresholding_Categorical_Feature_Variance.pdf): Thresholding Categorical Feature Variance
- ⭐ [Tokenizing_Text](ml-rapid-fire/data-engineering/Tokenizing_Text.pdf): Tokenizing Text
- ⭐ [Tomek_Link](ml-rapid-fire/data-engineering/Tomek_Link.pdf): Tomek Link
- ⭐ [Upsampling](ml-rapid-fire/data-engineering/Upsampling.pdf): Upsampling
- ⭐ [Variance_Thresholding_For_Feature_Selection](ml-rapid-fire/data-engineering/Variance_Thresholding_For_Feature_Selection.pdf): Variance Thresholding For Feature Selection
- ⭐ [When_Can_We_Delete_Observations_With_Missing_Values](ml-rapid-fire/data-engineering/When_Can_We_Delete_Observations_With_Missing_Values.pdf): When Can We Delete Observations With Missing Values
- ⭐ [Word2Vec](ml-rapid-fire/data-engineering/Word2Vec.pdf): Word2Vec

### Deep Learning

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/55) | 🏆 0 | 💪 0 | ⭐ 55

- ⭐ [Architecture_Of_A_Neural_Network](ml-rapid-fire/deep-learning/Architecture_Of_A_Neural_Network.pdf): Architecture Of A Neural Network
- ⭐ [BackProp](ml-rapid-fire/deep-learning/BackProp.pdf): BackProp
- ⭐ [Bagging_Vs_Dropout](ml-rapid-fire/deep-learning/Bagging_Vs_Dropout.pdf): Bagging Vs Dropout
- ⭐ [Basic_Parts_Of_Deep_Learning](ml-rapid-fire/deep-learning/Basic_Parts_Of_Deep_Learning.pdf): Basic Parts Of Deep Learning
- ⭐ [Capacity](ml-rapid-fire/deep-learning/Capacity.pdf): Capacity
- ⭐ [Common_Optimizers_With_Neural_Networks](ml-rapid-fire/deep-learning/Common_Optimizers_With_Neural_Networks.pdf): Common Optimizers With Neural Networks
- ⭐ [Common_Output_Layer_Activation_Functions](ml-rapid-fire/deep-learning/Common_Output_Layer_Activation_Functions.pdf): Common Output Layer Activation Functions
- ⭐ [Dropout](ml-rapid-fire/deep-learning/Dropout.pdf): Dropout
- ⭐ [ELUs](ml-rapid-fire/deep-learning/ELUs.pdf): ELUs
- ⭐ [Early_Stopping_Advantages](ml-rapid-fire/deep-learning/Early_Stopping_Advantages.pdf): Early Stopping Advantages
- ⭐ [Epoch](ml-rapid-fire/deep-learning/Epoch.pdf): Epoch
- ⭐ [Exploding_Gradient_Problem](ml-rapid-fire/deep-learning/Exploding_Gradient_Problem.pdf): Exploding Gradient Problem
- ⭐ [Feedforward_Neural_Networks](ml-rapid-fire/deep-learning/Feedforward_Neural_Networks.pdf): Feedforward Neural Networks
- ⭐ [Gradient_Cliff](ml-rapid-fire/deep-learning/Gradient_Cliff.pdf): Gradient Cliff
- ⭐ [Gradient_Clipping](ml-rapid-fire/deep-learning/Gradient_Clipping.pdf): Gradient Clipping
- ⭐ [Gradient_Descent](ml-rapid-fire/deep-learning/Gradient_Descent.pdf): Gradient Descent
- ⭐ [Gradient_Descent_Rule_Of_Thumb](ml-rapid-fire/deep-learning/Gradient_Descent_Rule_Of_Thumb.pdf): Gradient Descent Rule Of Thumb
- ⭐ [Gradient_Descent_Visualized](ml-rapid-fire/deep-learning/Gradient_Descent_Visualized.pdf): Gradient Descent Visualized
- ⭐ [Hidden_Layer](ml-rapid-fire/deep-learning/Hidden_Layer.pdf): Hidden Layer
- ⭐ [How_Norm_Penalties_Work](ml-rapid-fire/deep-learning/How_Norm_Penalties_Work.pdf): How Norm Penalties Work
- ⭐ [How_To_Choose_Hidden_Unit_Activation_Functions](ml-rapid-fire/deep-learning/How_To_Choose_Hidden_Unit_Activation_Functions.pdf): How To Choose Hidden Unit Activation Functions
- ⭐ [Initialization_Of_Neural_Network_Parameters](ml-rapid-fire/deep-learning/Initialization_Of_Neural_Network_Parameters.pdf): Initialization Of Neural Network Parameters
- ⭐ [Initializing_Weights_In_Feedforward_Neural_Networks](ml-rapid-fire/deep-learning/Initializing_Weights_In_Feedforward_Neural_Networks.pdf): Initializing Weights In Feedforward Neural Networks
- ⭐ [Leaky_ReLU](ml-rapid-fire/deep-learning/Leaky_ReLU.pdf): Leaky ReLU
- ⭐ [Learning_Rate](ml-rapid-fire/deep-learning/Learning_Rate.pdf): Learning Rate
- ⭐ [Linear_Activation_Function](ml-rapid-fire/deep-learning/Linear_Activation_Function.pdf): Linear Activation Function
- ⭐ [Minibatch](ml-rapid-fire/deep-learning/Minibatch.pdf): Minibatch
- ⭐ [Momentum](ml-rapid-fire/deep-learning/Momentum.pdf): Momentum
- ⭐ [Motivation_For_Deep_Layers](ml-rapid-fire/deep-learning/Motivation_For_Deep_Layers.pdf): Motivation For Deep Layers
- ⭐ [Motivation_For_Deep_Learning](ml-rapid-fire/deep-learning/Motivation_For_Deep_Learning.pdf): Motivation For Deep Learning
- ⭐ [Neuron](ml-rapid-fire/deep-learning/Neuron.pdf): Neuron
- ⭐ [Noisy_ReLU](ml-rapid-fire/deep-learning/Noisy_ReLU.pdf): Noisy ReLU
- ⭐ [Normalized_Initialization_Of_Neural_Network_Parameters](ml-rapid-fire/deep-learning/Normalized_Initialization_Of_Neural_Network_Parameters.pdf): Normalized Initialization Of Neural Network Parameters
- ⭐ [One-Sided_Label_Smoothing](ml-rapid-fire/deep-learning/One-Sided_Label_Smoothing.pdf): One Sided Label Smoothing
- ⭐ [Parameter_Norm](ml-rapid-fire/deep-learning/Parameter_Norm.pdf): Parameter Norm
- ⭐ [Parameter_Sharing](ml-rapid-fire/deep-learning/Parameter_Sharing.pdf): Parameter Sharing
- ⭐ [RMSprop](ml-rapid-fire/deep-learning/RMSprop.pdf): RMSprop
- ⭐ [ReLU_Activation_Function](ml-rapid-fire/deep-learning/ReLU_Activation_Function.pdf): ReLU Activation Function
- ⭐ [Saturation](ml-rapid-fire/deep-learning/Saturation.pdf): Saturation
- ⭐ [Saturation_Of_The_Loss_Function](ml-rapid-fire/deep-learning/Saturation_Of_The_Loss_Function.pdf): Saturation Of The Loss Function
- ⭐ [Sigmoid_Activation_Function](ml-rapid-fire/deep-learning/Sigmoid_Activation_Function.pdf): Sigmoid Activation Function
- ⭐ [Softmax_Activation_Function](ml-rapid-fire/deep-learning/Softmax_Activation_Function.pdf): Softmax Activation Function
- ⭐ [Softmax_Normalization](ml-rapid-fire/deep-learning/Softmax_Normalization.pdf): Softmax Normalization
- ⭐ [Softplus_Function](ml-rapid-fire/deep-learning/Softplus_Function.pdf): Softplus Function
- ⭐ [Stochastic_Gradient_Descent](ml-rapid-fire/deep-learning/Stochastic_Gradient_Descent.pdf): Stochastic Gradient Descent
- ⭐ [Supervised_Deep_Learning_Rule_Of_Thumb](ml-rapid-fire/deep-learning/Supervised_Deep_Learning_Rule_Of_Thumb.pdf): Supervised Deep Learning Rule Of Thumb
- ⭐ [TanH_Activation_Function](ml-rapid-fire/deep-learning/TanH_Activation_Function.pdf): TanH Activation Function
- ⭐ [The_Effect_Of_Dropout_On_Hidden_Units](ml-rapid-fire/deep-learning/The_Effect_Of_Dropout_On_Hidden_Units.pdf): The Effect Of Dropout On Hidden Units
- ⭐ [The_Effect_Of_Feature_Scaling_On_Gradient_Descent](ml-rapid-fire/deep-learning/The_Effect_Of_Feature_Scaling_On_Gradient_Descent.pdf): The Effect Of Feature Scaling On Gradient Descent
- ⭐ [Threshold_Activation](ml-rapid-fire/deep-learning/Threshold_Activation.pdf): Threshold Activation
- ⭐ [Typical_Dropout_Probabilities](ml-rapid-fire/deep-learning/Typical_Dropout_Probabilities.pdf): Typical Dropout Probabilities
- ⭐ [Unit-Step_Activation_Function](ml-rapid-fire/deep-learning/Unit-Step_Activation_Function.pdf): Unit Step Activation Function
- ⭐ [Vanishing_Gradient_Problem](ml-rapid-fire/deep-learning/Vanishing_Gradient_Problem.pdf): Vanishing Gradient Problem
- ⭐ [Weight_Decay](ml-rapid-fire/deep-learning/Weight_Decay.pdf): Weight Decay
- ⭐ [XOR_Function](ml-rapid-fire/deep-learning/XOR_Function.pdf): XOR Function

### Mathematics

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/50) | 🏆 0 | 💪 0 | ⭐ 50

- ⭐ [Big_O](ml-rapid-fire/mathematics/Big_O.pdf): Big O
- ⭐ [Chain_Rule_Of_Calculus](ml-rapid-fire/mathematics/Chain_Rule_Of_Calculus.pdf): Chain Rule Of Calculus
- ⭐ [Concave_And_Convex_Functions](ml-rapid-fire/mathematics/Concave_And_Convex_Functions.pdf): Concave And Convex Functions
- ⭐ [Conditioning](ml-rapid-fire/mathematics/Conditioning.pdf): Conditioning
- ⭐ [Derivative](ml-rapid-fire/mathematics/Derivative.pdf): Derivative
- ⭐ [Determinants](ml-rapid-fire/mathematics/Determinants.pdf): Determinants
- ⭐ [Dot_Product](ml-rapid-fire/mathematics/Dot_Product.pdf): Dot Product
- ⭐ [Eigenvector](ml-rapid-fire/mathematics/Eigenvector.pdf): Eigenvector
- ⭐ [Extrema](ml-rapid-fire/mathematics/Extrema.pdf): Extrema
- ⭐ [Frobenius_Norm](ml-rapid-fire/mathematics/Frobenius_Norm.pdf): Frobenius Norm
- ⭐ [Function](ml-rapid-fire/mathematics/Function.pdf): Function
- ⭐ [Gradient](ml-rapid-fire/mathematics/Gradient.pdf): Gradient
- ⭐ [Greedy_Algorithms](ml-rapid-fire/mathematics/Greedy_Algorithms.pdf): Greedy Algorithms
- ⭐ [Greek_Letters_1](ml-rapid-fire/mathematics/Greek_Letters_1.pdf): Greek Letters 1
- ⭐ [Greek_Letters_2](ml-rapid-fire/mathematics/Greek_Letters_2.pdf): Greek Letters 2
- ⭐ [Greek_Letters_3](ml-rapid-fire/mathematics/Greek_Letters_3.pdf): Greek Letters 3
- ⭐ [Greek_Letters_4](ml-rapid-fire/mathematics/Greek_Letters_4.pdf): Greek Letters 4
- ⭐ [Hadamard_Product](ml-rapid-fire/mathematics/Hadamard_Product.pdf): Hadamard Product
- ⭐ [Hessian_Matrix](ml-rapid-fire/mathematics/Hessian_Matrix.pdf): Hessian Matrix
- ⭐ [Hyperplane](ml-rapid-fire/mathematics/Hyperplane.pdf): Hyperplane
- ⭐ [Inflection_Point](ml-rapid-fire/mathematics/Inflection_Point.pdf): Inflection Point
- ⭐ [Jacobian_Matrix](ml-rapid-fire/mathematics/Jacobian_Matrix.pdf): Jacobian Matrix
- ⭐ [L1_Norm](ml-rapid-fire/mathematics/L1_Norm.pdf): L1 Norm
- ⭐ [L2_Norm](ml-rapid-fire/mathematics/L2_Norm.pdf): L2 Norm
- ⭐ [Linear_Combination](ml-rapid-fire/mathematics/Linear_Combination.pdf): Linear Combination
- ⭐ [Linearly_Independent](ml-rapid-fire/mathematics/Linearly_Independent.pdf): Linearly Independent
- ⭐ [Log-Sum-Exp](ml-rapid-fire/mathematics/Log-Sum-Exp.pdf): Log Sum Exp
- ⭐ [Manhattan_Distance](ml-rapid-fire/mathematics/Manhattan_Distance.pdf): Manhattan Distance
- ⭐ [Matrices](ml-rapid-fire/mathematics/Matrices.pdf): Matrices
- ⭐ [Matrix_Inverse](ml-rapid-fire/mathematics/Matrix_Inverse.pdf): Matrix Inverse
- ⭐ [Matrix_Multiplication](ml-rapid-fire/mathematics/Matrix_Multiplication.pdf): Matrix Multiplication
- ⭐ [Max_Norm](ml-rapid-fire/mathematics/Max_Norm.pdf): Max Norm
- ⭐ [Minkowski_Distance](ml-rapid-fire/mathematics/Minkowski_Distance.pdf): Minkowski Distance
- ⭐ [Natural_Log](ml-rapid-fire/mathematics/Natural_Log.pdf): Natural Log
- ⭐ [Notation_1](ml-rapid-fire/mathematics/Notation_1.pdf): Notation 1
- ⭐ [Notation_2](ml-rapid-fire/mathematics/Notation_2.pdf): Notation 2
- ⭐ [Notation_3](ml-rapid-fire/mathematics/Notation_3.pdf): Notation 3
- ⭐ [Notation_4](ml-rapid-fire/mathematics/Notation_4.pdf): Notation 4
- ⭐ [Notation_5](ml-rapid-fire/mathematics/Notation_5.pdf): Notation 5
- ⭐ [Partial_Derivative](ml-rapid-fire/mathematics/Partial_Derivative.pdf): Partial Derivative
- ⭐ [Power_Rule](ml-rapid-fire/mathematics/Power_Rule.pdf): Power Rule
- ⭐ [Saddle_Point](ml-rapid-fire/mathematics/Saddle_Point.pdf): Saddle Point
- ⭐ [Scalars](ml-rapid-fire/mathematics/Scalars.pdf): Scalars
- ⭐ [Span](ml-rapid-fire/mathematics/Span.pdf): Span
- ⭐ [Square_Root](ml-rapid-fire/mathematics/Square_Root.pdf): Square Root
- ⭐ [Stationary_Points](ml-rapid-fire/mathematics/Stationary_Points.pdf): Stationary Points
- ⭐ [Tensors](ml-rapid-fire/mathematics/Tensors.pdf): Tensors
- ⭐ [Therefore_And_Because_Notation](ml-rapid-fire/mathematics/Therefore_And_Because_Notation.pdf): Therefore And Because Notation
- ⭐ [Underflow](ml-rapid-fire/mathematics/Underflow.pdf): Underflow
- ⭐ [Vectors](ml-rapid-fire/mathematics/Vectors.pdf): Vectors

### Model Evaluation

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/65) | 🏆 0 | 💪 0 | ⭐ 65

- ⭐ [AIC](ml-rapid-fire/model-evaluation/AIC.pdf): AIC
- ⭐ [Accuracy](ml-rapid-fire/model-evaluation/Accuracy.pdf): Accuracy
- ⭐ [Adjusted_R-Squared](ml-rapid-fire/model-evaluation/Adjusted_R-Squared.pdf): Adjusted R Squared
- ⭐ [Area_Under_The_Curve](ml-rapid-fire/model-evaluation/Area_Under_The_Curve.pdf): Area Under The Curve
- ⭐ [Avoid_Overfitting](ml-rapid-fire/model-evaluation/Avoid_Overfitting.pdf): Avoid Overfitting
- ⭐ [Bayes_Error](ml-rapid-fire/model-evaluation/Bayes_Error.pdf): Bayes Error
- ⭐ [Bias-Variance_Tradeoff](ml-rapid-fire/model-evaluation/Bias-Variance_Tradeoff.pdf): Bias Variance Tradeoff
- ⭐ [Bias](ml-rapid-fire/model-evaluation/Bias.pdf): Bias
- ⭐ [Brier_Score](ml-rapid-fire/model-evaluation/Brier_Score.pdf): Brier Score
- ⭐ [Confusion_Matrix](ml-rapid-fire/model-evaluation/Confusion_Matrix.pdf): Confusion Matrix
- ⭐ [Cost_And_Loss_Functions](ml-rapid-fire/model-evaluation/Cost_And_Loss_Functions.pdf): Cost And Loss Functions
- ⭐ [Cp](ml-rapid-fire/model-evaluation/Cp.pdf): Cp
- ⭐ [Cross-Entropy](ml-rapid-fire/model-evaluation/Cross-Entropy.pdf): Cross Entropy
- ⭐ [Early_Stopping](ml-rapid-fire/model-evaluation/Early_Stopping.pdf): Early Stopping
- ⭐ [Error_Types](ml-rapid-fire/model-evaluation/Error_Types.pdf): Error Types
- ⭐ [Explained_Sum_Of_Squares](ml-rapid-fire/model-evaluation/Explained_Sum_Of_Squares.pdf): Explained Sum Of Squares
- ⭐ [F1_Score](ml-rapid-fire/model-evaluation/F1_Score.pdf): F1 Score
- ⭐ [False_Positive_Rate](ml-rapid-fire/model-evaluation/False_Positive_Rate.pdf): False Positive Rate
- ⭐ [Forward_Stepwise_Selection](ml-rapid-fire/model-evaluation/Forward_Stepwise_Selection.pdf): Forward Stepwise Selection
- ⭐ [Fowlkes-Mallows](ml-rapid-fire/model-evaluation/Fowlkes-Mallows.pdf): Fowlkes Mallows
- ⭐ [Generalization](ml-rapid-fire/model-evaluation/Generalization.pdf): Generalization
- ⭐ [Grid_Search](ml-rapid-fire/model-evaluation/Grid_Search.pdf): Grid Search
- ⭐ [Hamming_Loss](ml-rapid-fire/model-evaluation/Hamming_Loss.pdf): Hamming Loss
- ⭐ [Hinge_Loss](ml-rapid-fire/model-evaluation/Hinge_Loss.pdf): Hinge Loss
- ⭐ [Hyperparameter_Tuning](ml-rapid-fire/model-evaluation/Hyperparameter_Tuning.pdf): Hyperparameter Tuning
- ⭐ [Hypothesis_Space](ml-rapid-fire/model-evaluation/Hypothesis_Space.pdf): Hypothesis Space
- ⭐ [K-Fold_Cross-Validation](ml-rapid-fire/model-evaluation/K-Fold_Cross-Validation.pdf): K Fold Cross Validation
- ⭐ [Learning_Curve](ml-rapid-fire/model-evaluation/Learning_Curve.pdf): Learning Curve
- ⭐ [Learning_In_Machine_Learning](ml-rapid-fire/model-evaluation/Learning_In_Machine_Learning.pdf): Learning In Machine Learning
- ⭐ [Matthews_Correlation_Coefficient](ml-rapid-fire/model-evaluation/Matthews_Correlation_Coefficient.pdf): Matthews Correlation Coefficient
- ⭐ [Mean_Absolute_Error](ml-rapid-fire/model-evaluation/Mean_Absolute_Error.pdf): Mean Absolute Error
- ⭐ [Mean_Squared_Error](ml-rapid-fire/model-evaluation/Mean_Squared_Error.pdf): Mean Squared Error
- ⭐ [Minimum_Of_A_Loss_Function](ml-rapid-fire/model-evaluation/Minimum_Of_A_Loss_Function.pdf): Minimum Of A Loss Function
- ⭐ [Model_Complexity](ml-rapid-fire/model-evaluation/Model_Complexity.pdf): Model Complexity
- ⭐ [Model_Identifiability](ml-rapid-fire/model-evaluation/Model_Identifiability.pdf): Model Identifiability
- ⭐ [Model_Selection](ml-rapid-fire/model-evaluation/Model_Selection.pdf): Model Selection
- ⭐ [No_Free_Lunch_Theorem](ml-rapid-fire/model-evaluation/No_Free_Lunch_Theorem.pdf): No Free Lunch Theorem
- ⭐ [Occams_Razor](ml-rapid-fire/model-evaluation/Occams_Razor.pdf): Occams Razor
- ⭐ [Out-Of-Bag_Error](ml-rapid-fire/model-evaluation/Out-Of-Bag_Error.pdf): Out Of Bag Error
- ⭐ [Overfit_Vs_Underfit](ml-rapid-fire/model-evaluation/Overfit_Vs_Underfit.pdf): Overfit Vs Underfit
- ⭐ [Overfitting](ml-rapid-fire/model-evaluation/Overfitting.pdf): Overfitting
- ⭐ [Parameters_vs_Hyperparameters](ml-rapid-fire/model-evaluation/Parameters_vs_Hyperparameters.pdf): Parameters vs Hyperparameters
- ⭐ [Precision](ml-rapid-fire/model-evaluation/Precision.pdf): Precision
- ⭐ [Preprocessing_Training_And_Test_Sets](ml-rapid-fire/model-evaluation/Preprocessing_Training_And_Test_Sets.pdf): Preprocessing Training And Test Sets
- ⭐ [R-Squared](ml-rapid-fire/model-evaluation/R-Squared.pdf): R Squared
- ⭐ [Randomized_Search](ml-rapid-fire/model-evaluation/Randomized_Search.pdf): Randomized Search
- ⭐ [Recall](ml-rapid-fire/model-evaluation/Recall.pdf): Recall
- ⭐ [Receiver_Operating_Characteristic](ml-rapid-fire/model-evaluation/Receiver_Operating_Characteristic.pdf): Receiver Operating Characteristic
- ⭐ [Regularization](ml-rapid-fire/model-evaluation/Regularization.pdf): Regularization
- ⭐ [Residual_Sum_Of_Squares](ml-rapid-fire/model-evaluation/Residual_Sum_Of_Squares.pdf): Residual Sum Of Squares
- ⭐ [Sensitivity](ml-rapid-fire/model-evaluation/Sensitivity.pdf): Sensitivity
- ⭐ [Silhouette_Coefficients](ml-rapid-fire/model-evaluation/Silhouette_Coefficients.pdf): Silhouette Coefficients
- ⭐ [Strategies_When_You_Have_High_Variance](ml-rapid-fire/model-evaluation/Strategies_When_You_Have_High_Variance.pdf): Strategies When You Have High Variance
- ⭐ [Test_Training_And_Validation_Sets](ml-rapid-fire/model-evaluation/Test_Training_And_Validation_Sets.pdf): Test Training And Validation Sets
- ⭐ [The_Effect_Of_Model_Complexity_On_Training_And_Test_Error](ml-rapid-fire/model-evaluation/The_Effect_Of_Model_Complexity_On_Training_And_Test_Error.pdf): The Effect Of Model Complexity On Training And Test Error
- ⭐ [Total_Sum-Of-Squares](ml-rapid-fire/model-evaluation/Total_Sum-Of-Squares.pdf): Total Sum Of Squares
- ⭐ [Training_And_Test_Error](ml-rapid-fire/model-evaluation/Training_And_Test_Error.pdf): Training And Test Error
- ⭐ [Training_Error_Rate](ml-rapid-fire/model-evaluation/Training_Error_Rate.pdf): Training Error Rate
- ⭐ [True_Positive_Rate](ml-rapid-fire/model-evaluation/True_Positive_Rate.pdf): True Positive Rate
- ⭐ [Underfitting](ml-rapid-fire/model-evaluation/Underfitting.pdf): Underfitting
- ⭐ [Validation_Curve](ml-rapid-fire/model-evaluation/Validation_Curve.pdf): Validation Curve
- ⭐ [Visualizing_RSS](ml-rapid-fire/model-evaluation/Visualizing_RSS.pdf): Visualizing RSS
- ⭐ [Why_Is_It_Called_A_Cost_Function](ml-rapid-fire/model-evaluation/Why_Is_It_Called_A_Cost_Function.pdf): Why Is It Called A Cost Function
- ⭐ [Youdens_J_Statistic](ml-rapid-fire/model-evaluation/Youdens_J_Statistic.pdf): Youdens J Statistic
- ⭐ [Zero-One_Loss](ml-rapid-fire/model-evaluation/Zero-One_Loss.pdf): Zero One Loss

### Statistics

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/33) | 🏆 0 | 💪 0 | ⭐ 33

- ⭐ [Almost_Everywhere](ml-rapid-fire/statistics/Almost_Everywhere.pdf): Almost Everywhere
- ⭐ [Anscombes_Quartet](ml-rapid-fire/statistics/Anscombes_Quartet.pdf): Anscombes Quartet
- ⭐ [Bayes_Theorem](ml-rapid-fire/statistics/Bayes_Theorem.pdf): Bayes Theorem
- ⭐ [Bootstrap](ml-rapid-fire/statistics/Bootstrap.pdf): Bootstrap
- ⭐ [Chi-Squared](ml-rapid-fire/statistics/Chi-Squared.pdf): Chi Squared
- ⭐ [Combination](ml-rapid-fire/statistics/Combination.pdf): Combination
- ⭐ [Conditional_Probability](ml-rapid-fire/statistics/Conditional_Probability.pdf): Conditional Probability
- ⭐ [Confidence_Intervals](ml-rapid-fire/statistics/Confidence_Intervals.pdf): Confidence Intervals
- ⭐ [Consistency](ml-rapid-fire/statistics/Consistency.pdf): Consistency
- ⭐ [Cumulative_Distribution_Function](ml-rapid-fire/statistics/Cumulative_Distribution_Function.pdf): Cumulative Distribution Function
- ⭐ [Data-Generating_Distribution](ml-rapid-fire/statistics/Data-Generating_Distribution.pdf): Data Generating Distribution
- ⭐ [F-Statistic](ml-rapid-fire/statistics/F-Statistic.pdf): F Statistic
- ⭐ [Heteroskedasticity](ml-rapid-fire/statistics/Heteroskedasticity.pdf): Heteroskedasticity
- ⭐ [IID](ml-rapid-fire/statistics/IID.pdf): IID
- ⭐ [Instrumental_Variables](ml-rapid-fire/statistics/Instrumental_Variables.pdf): Instrumental Variables
- ⭐ [Interquartile_Range](ml-rapid-fire/statistics/Interquartile_Range.pdf): Interquartile Range
- ⭐ [Normal_Distribution](ml-rapid-fire/statistics/Normal_Distribution.pdf): Normal Distribution
- ⭐ [Notions_Of_Probability](ml-rapid-fire/statistics/Notions_Of_Probability.pdf): Notions Of Probability
- ⭐ [Odds](ml-rapid-fire/statistics/Odds.pdf): Odds
- ⭐ [Odds_Ratio](ml-rapid-fire/statistics/Odds_Ratio.pdf): Odds Ratio
- ⭐ [Pearsons_Correlation](ml-rapid-fire/statistics/Pearsons_Correlation.pdf): Pearsons Correlation
- ⭐ [Probability_Density_Function](ml-rapid-fire/statistics/Probability_Density_Function.pdf): Probability Density Function
- ⭐ [Probability_Mass_Function](ml-rapid-fire/statistics/Probability_Mass_Function.pdf): Probability Mass Function
- ⭐ [Random_Variable](ml-rapid-fire/statistics/Random_Variable.pdf): Random Variable
- ⭐ [Simpsons_Paradox](ml-rapid-fire/statistics/Simpsons_Paradox.pdf): Simpsons Paradox
- ⭐ [Sources_Of_Uncertainty](ml-rapid-fire/statistics/Sources_Of_Uncertainty.pdf): Sources Of Uncertainty
- ⭐ [Standard_Deviation](ml-rapid-fire/statistics/Standard_Deviation.pdf): Standard Deviation
- ⭐ [Standard_Error_Of_The_Mean](ml-rapid-fire/statistics/Standard_Error_Of_The_Mean.pdf): Standard Error Of The Mean
- ⭐ [T-Statistic](ml-rapid-fire/statistics/T-Statistic.pdf): T Statistic
- ⭐ [Uniform_Distribution](ml-rapid-fire/statistics/Uniform_Distribution.pdf): Uniform Distribution
- ⭐ [Variance](ml-rapid-fire/statistics/Variance.pdf): Variance
- ⭐ [Variance_Inflation_Factor](ml-rapid-fire/statistics/Variance_Inflation_Factor.pdf): Variance Inflation Factor
- ⭐ [When_N_Equals_Population](ml-rapid-fire/statistics/When_N_Equals_Population.pdf): When N Equals Population
## ML Workflows


### 01 Basics

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/23) | 🏆 0 | 💪 0 | ⭐ 23

- ⭐ [01-learning-types](ml-workflows/01-basics/01-learning-types.md): Explain supervised, unsupervised, weakly supervised, semi-supervised, and active...
- ⭐ [02-empirical-risk](ml-workflows/01-basics/02-empirical-risk.md): What's the risk in empirical risk minimization?
- ⭐ [03-why-empirical](ml-workflows/01-basics/03-why-empirical.md): Why is it empirical?
- ⭐ [04-minimize-risk](ml-workflows/01-basics/04-minimize-risk.md): How do we minimize that risk?
- ⭐ [05-occams-razor](ml-workflows/01-basics/05-occams-razor.md): "Occam's razor states that when the simple explanation and complex explanation b...
- ⭐ [06-deep-learning-conditions](ml-workflows/01-basics/06-deep-learning-conditions.md): What are the conditions that allowed deep learning to gain popularity in the las...
- ⭐ [07-wide-vs-deep](ml-workflows/01-basics/07-wide-vs-deep.md): If we have a wide NN and a deep NN with the same number of parameters, which one...
- ⭐ [08-universal-approximation](ml-workflows/01-basics/08-universal-approximation.md): "The Universal Approximation Theorem states that a neural network with 1 hidden ...
- ⭐ [09-saddle-points-local-minima](ml-workflows/01-basics/09-saddle-points-local-minima.md): What are saddle points and local minima? Which are thought to cause more problem...
- ⭐ [10-parameters-vs-hyperparameters](ml-workflows/01-basics/10-parameters-vs-hyperparameters.md): What are the differences between parameters and hyperparameters?
- ⭐ [11-hyperparameter-tuning-importance](ml-workflows/01-basics/11-hyperparameter-tuning-importance.md): Why is hyperparameter tuning important?
- ⭐ [12-hyperparameter-tuning-algorithm](ml-workflows/01-basics/12-hyperparameter-tuning-algorithm.md): Explain the algorithm for tuning hyperparameters.
- ⭐ [13-classification-vs-regression](ml-workflows/01-basics/13-classification-vs-regression.md): What makes a classification problem different from a regression problem?
- ⭐ [14-classification-regression-conversion](ml-workflows/01-basics/14-classification-regression-conversion.md): Can a classification problem be turned into a regression problem and vice versa?
- ⭐ [15-parametric-vs-nonparametric](ml-workflows/01-basics/15-parametric-vs-nonparametric.md): What's the difference between parametric and non-parametric methods? Give exampl...
- ⭐ [16-when-parametric-vs-nonparametric](ml-workflows/01-basics/16-when-parametric-vs-nonparametric.md): When should we use parametric versus non-parametric methods?
- ⭐ [17-ensembling-benefits](ml-workflows/01-basics/17-ensembling-benefits.md): Why does ensembling independently trained models generally improve performance?
- ⭐ [18-l1-vs-l2-regularization](ml-workflows/01-basics/18-l1-vs-l2-regularization.md): Why does L1 regularization tend to lead to sparsity while L2 regularization push...
- ⭐ [19-production-degradation](ml-workflows/01-basics/19-production-degradation.md): Why does an ML model's performance degrade in production?
- ⭐ [20-deploying-large-models](ml-workflows/01-basics/20-deploying-large-models.md): What problems might we run into when deploying large machine learning models?
- ⭐ [21-production-performance-hypotheses](ml-workflows/01-basics/21-production-performance-hypotheses.md): What are your hypotheses about the causes of good test performance but poor prod...
- ⭐ [22-validate-hypotheses](ml-workflows/01-basics/22-validate-hypotheses.md): How do you validate whether your hypotheses are correct?
- ⭐ [23-address-causes](ml-workflows/01-basics/23-address-causes.md): How would you address the identified causes?
## Math & Quant Foundations


### 01 Probability Stats

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/5) | 🏆 0 | 💪 0 | ⭐ 5

- ⭐ [01-conditional-expectation](math-quant-foundations/01-probability-stats/01-conditional-expectation.md): What is conditional expectation and why is it central to quantitative finance?
- ⭐ [02-variance-decomposition](math-quant-foundations/01-probability-stats/02-variance-decomposition.md): Explain the Law of Total Variance and its applications in finance.
- ⭐ [03-maximum-likelihood](math-quant-foundations/01-probability-stats/03-maximum-likelihood.md): Explain Maximum Likelihood Estimation (MLE) and when it might fail.
- ⭐ [04-bayes-theorem](math-quant-foundations/01-probability-stats/04-bayes-theorem.md): State Bayes' theorem and explain its role in updating beliefs with new informati...
- ⭐ [05-central-limit-theorem](math-quant-foundations/01-probability-stats/05-central-limit-theorem.md): State the Central Limit Theorem and explain why it's fundamental to quantitative...

### 02 Linear Algebra

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/5) | 🏆 0 | 💪 0 | ⭐ 5

- ⭐ [01-eigenvectors-eigenvalues](math-quant-foundations/02-linear-algebra/01-eigenvectors-eigenvalues.md): What are eigenvectors and eigenvalues? Why do they matter for PCA and covariance...
- ⭐ [02-pca-intuition](math-quant-foundations/02-linear-algebra/02-pca-intuition.md): Explain PCA intuitively and its applications in quantitative finance.
- ⭐ [03-projections](math-quant-foundations/02-linear-algebra/03-projections.md): What is an orthogonal projection? How is it used in regression and least squares...
- ⭐ [04-svd](math-quant-foundations/02-linear-algebra/04-svd.md): Explain Singular Value Decomposition (SVD) and its applications.
- ⭐ [05-matrix-calculus](math-quant-foundations/02-linear-algebra/05-matrix-calculus.md): Summarize key matrix calculus results used in ML and optimization.

### 03 Stochastic Processes

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/5) | 🏆 0 | 💪 0 | ⭐ 5

- ⭐ [01-brownian-motion](math-quant-foundations/03-stochastic-processes/01-brownian-motion.md): Define Brownian motion (Wiener process) and its key properties.
- ⭐ [02-geometric-brownian-motion](math-quant-foundations/03-stochastic-processes/02-geometric-brownian-motion.md): What is Geometric Brownian Motion and why is it used for stock prices?
- ⭐ [03-ito-lemma](math-quant-foundations/03-stochastic-processes/03-ito-lemma.md): State Ito's lemma and explain why the extra term appears.
- ⭐ [04-martingales](math-quant-foundations/03-stochastic-processes/04-martingales.md): What is a martingale and why is it central to derivative pricing?
- ⭐ [05-mean-reversion](math-quant-foundations/03-stochastic-processes/05-mean-reversion.md): Explain mean reversion and the Ornstein-Uhlenbeck process.

### 04 Numerical Methods

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/3) | 🏆 0 | 💪 0 | ⭐ 3

- ⭐ [01-newton-raphson](math-quant-foundations/04-numerical-methods/01-newton-raphson.md): Explain Newton-Raphson root finding and its application to implied volatility.
- ⭐ [02-interpolation](math-quant-foundations/04-numerical-methods/02-interpolation.md): Compare linear, polynomial, and spline interpolation. When would you use each?
- ⭐ [03-cubic-splines](math-quant-foundations/04-numerical-methods/03-cubic-splines.md): Explain cubic splines in detail. Why are they preferred for yield curve construc...

### 05 Options Greeks

**Progress:** [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0.0% (0/6) | 🏆 0 | 💪 0 | ⭐ 6

- ⭐ [01-black-scholes](math-quant-foundations/05-options-greeks/01-black-scholes.md): Derive the key intuition behind Black-Scholes. What assumptions does it make?
- ⭐ [02-greeks](math-quant-foundations/05-options-greeks/02-greeks.md): Define the main Greeks and explain their practical significance for trading.
- ⭐ [03-delta-hedging](math-quant-foundations/05-options-greeks/03-delta-hedging.md): Explain delta hedging. Why doesn't it eliminate all risk?
- ⭐ [04-volatility-smile](math-quant-foundations/05-options-greeks/04-volatility-smile.md): What is the volatility smile/skew? What causes it?
- ⭐ [05-term-structure](math-quant-foundations/05-options-greeks/05-term-structure.md): Explain the term structure of volatility and interest rates.
- ⭐ [06-put-call-parity](math-quant-foundations/05-options-greeks/06-put-call-parity.md): State put-call parity and explain its arbitrage implications.

---

*Last updated: 2025-11-28 11:42:51*

*Generated by [scripts/generate_readme.py](scripts/generate_readme.py)*