# Question

If we have a wide NN and a deep NN with the same number of parameters, which one is more expressive and why?

# Answer

The deep neural network is more expressive than the wide neural network with the same number of parameters.

**Deep networks are more expressive because they can learn hierarchical representations** - each layer builds progressively more complex features from simpler ones. This compositional approach allows deep networks to represent complex functions more efficiently than wide, shallow networks.

**The key advantage is incremental, layer-by-layer representation learning.** Deep networks learn representations that are jointly optimized - each layer is updated to follow both the representational needs of the layer above and the layer below. In contrast, shallow networks must learn all representations in essentially one transformation step, lacking this hierarchical composition.

**Deep networks enable automatic feature composition without manual engineering.** With each additional layer, deep learning models build up more complex features by combining smaller features (e.g., a face is composed of eyes, ears, a nose, and a mouth). Shallow models struggle with this and often require extensive manual feature engineering to achieve similar performance on complex tasks like perception or language translation.

**Non-linear activation functions are critical for this expressiveness.** Without non-linear activations, adding layers would not extend the hypothesis space - the network would still only be capable of learning linear transformations. Non-linearity allows each layer to genuinely add representational capacity.

**Empirical evidence supports deeper architectures.** Research shows that deep networks with moderate width outperform shallow networks with many neurons. For example, models with 5-9 hidden layers with decreasing width (e.g., 2500→2000→1500→1000→500 neurons) achieve state-of-the-art results, demonstrating that depth provides more value than width for the same parameter budget.

---

## Extracts from my notes

### 202101091725 Deep Learning's Edge Over Shallow Learning.txt

> Deep learning has been vastly more successful than other machine learning methods.  Chollet attributes this to two factors: deep learning models are able to learn a hierarchy of features, and they are able to learn them jointly [@chollet2018deep, p. 18].
>
> In shallow learning, model inputs are transformed into a new representation space either once or twice.  As an example, in a linear regression (see [[202106150747 Linear Regression Model]]), the data is transformed once into a single representation of weights and a bias.  In contrast, a 10-layer neural network will transform the data into 10 different representations.
>
> Shallow models have difficulty solving more complex problems like perception or language translation.   Sometimes this can be overcome through feature engineering (see [[202101241643 Feature Engineering]].  A skilled engineer familiar with the problem domain can often transform data into a new representation before it is fed into the model, thereby improving performance.
>
> From François Chollet [@chollet2018deep, p. 103]:
>
> > Before deep learning, feature engineering used to be critical, because classical shallow algorithms didn't have hypothesis spaces rich enough to learn useful features by themselves.  The way you presented the data to the algorithm was essential to its success.
>
> This isn't necessary with deep learning (LeCun showed this in [[202101200745 Summary - Gradient-Based Learning Applied to Document Recognition by LeCun]]).  With each additional layer, deep learning models are able to build up more complex features by combining smaller features.  E.g. a face is composed of eyes, ears, a nose, and a mouth.
>
> From François Chollet [@chollet2018deep, p. 18]:
>
> > These are the two essential characteristics of how deep learning learns from data: the _incremental, layer-by-layer way in which increasingly complex representations are developed,_ and the fact that _these intermediate incremental representations are learned jointly,_ each layer being updated to follow both the representational needs of the layer above and the needs of the layer below.
>
> From Ian Goodfellow [goodfellow2016deep, p. 5]
>
> > Deep learning solves this central problem in representation learning by introducing representations that are expressed in terms of other, simpler representations.  Deep learning enables the computer to build complex concepts out of simpler concepts.
>
> You could attempt to stack multiple shallow models on top of each other to make a deeper model, but this tends not to work in practice [@chollet2018deep, p. 18].  This is a greedy approach; each layer tries to do the best that it can.  Whereas a deep neural network is able to more thoughtfully compose large features from smaller features.


### 202101110713 Representations in Machine Learning.txt

> From François Chollet [@chollet2018deep, p. 28]:
>
> > The core building block of neural networks is the _layer_, a data-processing module that you can think of as a filter for data.  Some data goes in, and it comes out in a more useful form.  Specifically, layers extract _representations_ out of the data fed into them--hopefully, representations that are more meaningful for the problem at hand.  Most of deep learning consists of chaining together simple layers that will implement a form of progressive _data distillation_.  A deep-learning model is like a sieve for data processing, made of a succession of increasingly refined data filters--the layers.
>
> Ian Goodfellow mentions [@goodfellow2016deep, p3]:
>
> > The choice of representation has an enormous effect on the performance of machine learning algorithms.


### 202101120811 Activation Functions.txt

> Activation functions allow neural networks to model non-linear transformations of the input data [@chollet2018deep, p. 72].  Without activation functions, neural networks would only be able to learn the set of all possible linear transformations of the input data into a N-dimensional space, where N is the number of neurons in the layer.  Adding more layers to the model does not extend the hypothesis space.  So without a non-linear activation function, neural networks would not be able to build up successively more complicated representations (see [[202101110713 Representations in Machine Learning]], and [[202101091725 Deep Learning's Edge Over Shallow Learning]]) in the higher layers of the network.


### 202101201941 Convolutional Neural Networks.txt

> ## Local Receptive Fields
>
> Local receptive fields give you the ability to detect corners, edges, etc [@lecun1998gradient, p. 6].  The local receptive field acts as a sliding window that scans over its inputs, looking for a particular feature (based on its weights).  When convolutional layers are stacked on top of each other, local receptive fields give the model the ability to recognize higher order features.
>
> ## Architecture Guidance
>
> The number of feature maps in each layer, and their size, often follow a "bi-pyramid" structure [@lecun1998gradient, p. 67].  This means that the deep layers have few feature maps, but large-resolution maps.  In deep layers, you are focused on recognizing a few small primitive features (corners, edges).  Whereas the top layers have many more feature maps, but each is of a lower resolution.  This is because the top layers are recognizing higher order features (e.g. faces).  Each higher order feature occupies a larger section of the image, and you can compose many higher order features out of the smaller primitive features from earlier layers (see [[202101110713 Representations in Machine Learning]], and [[202101091725 Deep Learning's Edge Over Shallow Learning]]) .


### 202101210721 Summary - Deep Big Simple Neural Nets Excel on Hand-Written Digit Recognition.txt

> The big idea in this paper is that a simple neural network, fortified with large amounts of data and large amounts of compute can excel on image recognition tasks without having to resort to using more complex modeling methods.  This is evidence that data and compute are far more important than algorithms and software.  It is also evidence for the 'bigger models are better' trend.
>
> ## Architecture and Design
>
> * Initialize weights with a uniform distribution between $[-0.05, 0.05]$.
> * Use a tanh activation function
> * Use between 2 and 9 hidden layers
> * Decrease the number of hidden units per layer as you approach the output layer.
> * Use standard backpropagation.
> * Use a variable learning rate
> * At the start of each epoch, deform the training images via rotation, scaling, and shearing.  Train on the deformed images.  The objective here is to augment the dataset.
> * The top performing model had 5 hidden layers (2500, 2000, 1500, 1000, 500) and an output layer of 10 neurons.
>
> ## Results
>
> The best model had a test error of 0.35%.


### 202101200745 Summary - Gradient-Based Learning Applied to Document Recognition by LeCun.txt

> LeCun's big idea in this paper is that we can now move away from using hand-build feature extraction modules (see [[202101241643 Feature Engineering]]) as a pre-processing step to the classifier model [@lecun1998gradient, p. 1].  In this traditional model, the human engineer hand-designs a feature extractor that takes messy, complex data and reduces the number of dimensions, injecting prior domain knowledge into the data.  This simpler data can then be fed into a general purpose classifier.  Building feature extractors is time intensive because they are domain specific.  But the recent increase in the quantity of training data, increase in computing power, and improvement in learning algorithms has made the general purpose classifier models good enough that we can stop building feature extractors.
>
> Convolutional Neural Networks reduce the need to preprocess input data [@lecun1998gradient, p. 40] (this is one of deep learning's edge over shallow learning [[202101091725 Deep Learning's Edge Over Shallow Learning]]).  It is unlikely that a human is able to choose the optimal transformation of the input data.  Having a machine learn the transformations will likely result in better performance, and reduces manual work and the need for domain knowledge.


