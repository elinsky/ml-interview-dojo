# Question

What are the conditions that allowed deep learning to gain popularity in the last decade?

# Answer

Deep learning gained popularity in the last decade due to three converging trends: hardware advances, datasets and benchmarks, and algorithmic improvements. These factors came together around 2012 with the AlexNet breakthrough on ImageNet.

**Hardware advances** provided the computational power needed to train deep networks. CPUs became ~5000x faster between 1990 and 2010, and NVIDIA's release of CUDA in 2007 enabled easy GPU programming for parallel matrix computations in backpropagation. GPUs were crucial for training large models efficiently.

**Large datasets** became available through internet growth and storage hardware progress. ImageNet provided 15 million labeled images, enabling models to learn complex patterns. Larger datasets allowed larger models, which perform better than smaller ones.

**Algorithmic breakthroughs** around 2009-2010 made training deep networks practical. Better activation functions (ReLU), improved weight initialization schemes, and better optimizers (Adam, RMSProp) enabled successful gradient flow through many layers. Backpropagation showed it was efficient to compute gradients, and dropout and batch normalization helped prevent overfitting and speed training.

**The AlexNet paper (2012)** demonstrated the power of combining these advances. By using GPU + ReLU activation functions, Krizhevsky et al. achieved state-of-the-art performance on ImageNet classification. This breakthrough sparked the current deep learning revolution.

**Deep learning's architectural advantage** also played a role: the ability to automatically learn hierarchical representations without manual feature engineering. Multi-layer networks can compose complex features from simpler ones, eliminating the need for domain experts to hand-craft feature extractors.

---

## Extracts from my notes

### 202101091757 Technical Trends Driving Deep Learning's Success.txt

> Deep Learning took off after 2012.  Many credit the AlexNet paper [@NIPS2012_c399862d] as kicking off the most recent AI revolution.  In general there are three trends that have driven the recent success of deep learning [@chollet2018deep, p. 20] [@lecun1998gradient, p. 40]:
>
> 1. Hardware
> 2. Datasets and Benchmarks
> 3. Algorithmic Advances
>
> # Hardware
>
> From François Chollet [@chollet2018deep, p. 20]:
>
> > Between 1990 and 2010, off-the-shelf CPUs became faster by a factor of approximately 5,000.
>
> Faster CPUs enable more complex models to be built and trained.
>
> Additionally, NVIDIA released CUDA in 2007.  This enabled anyone to write code for their GPUs.  With GPUs widely available, it became easy to train models that could take advantage of parallel computations.  Particularly for deep learning, the matrix calculations in the backpropogation algorithm are able to take advantage of GPU hardware.
>
> Faster CPUs, the advent of GPUs, and faster network connectivity also contribute to larger dataset sizes [@goodfellow2016deep, p21], which helps producer larger, more accurate models.
>
> # Datasets and Benchmarks
>
> There are two primary drivers of increased quantity and availability of data: progress in storage hardware, and the internet.
>
> From François Chollet [@chollet2018deep, p. 21]:
>
> > When it comes to data, in addition to the exponential progress in storage hardware over the past 20 years (following Moore's law), the game changer has been the rise of the internet, making it feasible to collect and distribute very large datasets for machine learning.
>
> Ian Goodfellow credits increasing dataset sizes as ``the most important new development`` that is driving recent success in deep learning [@goodfellow2016deep, p18].  He credits this trend to the digitization of society, which spawned the age of 'big data.'
>
> Additionally, as datasets get larger, models can get larger.  Larger models tend to perform better than smaller ones.  So as datasets get larger, neural networks become more effective [@goodfellow2016deep, p21].
>
> # Algorithmic Advances
>
> Up until the early 2010s, most neural networks could only be trained with a few layers.  From François Chollet [@chollet2018deep, p. 21]:
>
> > This changed around 2009-2010 with the advent of several simple but important algorithmic improvements that allowed for better gradient backpropogation:
> >
> >  * Better _activation functions_ for neural layers
> >  * Better _weight-initialization schemes_, starting with layer-wise pretraining, which was quickly abandoned
> >  * Better _optimization schemes_ such as RMSProp and Adam
>
> It was the combination of these factors that allowed researchers and practitioners to start successfully training neural networks.  OpenAI's recent GPT-3 model was trained with 96 layers [@brown2020language].


### 202101302158 Summary - ImageNet Classification with Deep Convolutional Neural Networks.txt

> BLUF - The big idea that Krizhevsky et al. showed in this paper [@NIPS2012_c399862d] is that they were able to use a GPU plus ReLU activation functions to much more efficiently train a CNN on image data.  The significant gains in computational efficiency allowed them to build a much bigger model than before, and train it on a large dataset.  These factors allowed them to achieve state of the art performance on image recognition tasks.  **Essentially the main contribution was GPU + ReLU and putting it all together to get state of the art performance.**
>
> ## Data
>
> The ImageNet datasets is 15 million high resolution pictures of varying resolution.  It contains about 1000 classes of objects.  The ILSVRC competition uses a 1.2 million image subset of ImageNet.
>
> ## Learning
>
> They used stochastic gradient descent with a mini-batch size of 128.  They used momentum and weight decay.  They also used a learning rate schedule.
>
> ## Overfitting
>
> In order to reduce overfitting, they used dropout and data augmentation.
>
> ## Architecture
>
> * GPU implementation
> * ReLU activation function
>     * Doesn't saturate
>     * Faster training time than tanh.
> * Dropout
> * 5 convolutional layers
> * A few max pooling layers
>     * Interestingly they used **overlapping pooling**.  I wonder if this ever caught on.
> * 3 fully connected layers on the top
> * Softmax output


### 202101201802 Three Factors Led to the Adoption of Gradient Descent for ML.txt

> According to Yann LeCun, three factors led to the widespread adoption of gradient descent (see [[202101050843 Gradient Descent]]) within the machine learning community [@lecun1998gradient, p. 3]:
>
> 1. The first was the realization that getting stuck in a local minima wasn't a problem in practice.  This was noticed when attempting to train Boltzmann machines with gradient-based learning-techniques.
> 2. Second, Rumelhart, Hinton, and Williams [@RumelhartDavidE1987LIRb] showed that it was possible to efficiently compute gradients via backpropagation.
> 3. Third, it was shown that multi-layer neural networks could be trained efficiently with the sigmoid activation function (see [[202012261450 Sigmoid Neuron]]) and backpropagation (see [[202101130721 Mathematics of Backpropagation]]).


### 202101171822 Dropout.txt

> ## Objective
>
> Dropout is a form of regularization (see [[202104170846 Regularization]]) that can be applied to a layer in a neural network.  It works by randomly dropping  neurons during training.  This prevents neurons from relying too much on each other (**co-adapting** too much), and adds noise to the training process, which has a regularizing effect, hence reducing the risk of overfitting.
>
> Benefits:
>
> * Reduced risk of overfitting
> * Reduced generalization error [@JMLR:v15:srivastava14a, p. 1931]
>
> Drawbacks:
>
> * Increased training time [@JMLR:v15:srivastava14a, p. 1952]


### 202101311539 Batch Normalization.txt

> ## Objective
>
> The big idea behind Batch Normalization is that if you eliminate **internal covariate shift**, then your model will learn the optimal set of weights faster.
>
> Note that this paper also set a new state-of-the-art performance on ImageNet classification.  So not only does Batch Normalization speed up training, it also improves classification accuracy.
>
> Benefits:
>
> * Faster training
>     * Can use larger learning rates
> * Regularization (see [[202104170846 Regularization]])


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


### 202101200745 Summary - Gradient-Based Learning Applied to Document Recognition by LeCun.txt

> LeCun's big idea in this paper is that we can now move away from using hand-build feature extraction modules (see [[202101241643 Feature Engineering]]) as a pre-processing step to the classifier model [@lecun1998gradient, p. 1].  In this traditional model, the human engineer hand-designs a feature extractor that takes messy, complex data and reduces the number of dimensions, injecting prior domain knowledge into the data.  This simpler data can then be fed into a general purpose classifier.  Building feature extractors is time intensive because they are domain specific.  But the recent increase in the quantity of training data, increase in computing power, and improvement in learning algorithms has made the general purpose classifier models good enough that we can stop building feature extractors.
>
> Convolutional Neural Networks reduce the need to preprocess input data [@lecun1998gradient, p. 40] (this is one of deep learning's edge over shallow learning [[202101091725 Deep Learning's Edge Over Shallow Learning]]).  It is unlikely that a human is able to choose the optimal transformation of the input data.  Having a machine learn the transformations will likely result in better performance, and reduces manual work and the need for domain knowledge.
>
> Image recognition systems will continue to improve as we get more training data, faster computers, and better learning algorithms [@lecun1998gradient, p. 2] [@lecun1998gradient, p. 40] (see also [[202101091757 Technical Trends Driving Deep Learning's Success]].  LeCun has the same three factors as Chollet).


### 202012271742 Connectionism.txt

> Ian Goodfellow mentions [@goodfellow2016deep, p17]:
>
> > [A] major accomplishment of the connectionist movement was the successful use of back-propagation to train deep neural networks with internal representations and the popularization of the back-propagation algorithm.


### 202105270800 Transformers.txt

> ### Pros
>
> One benefit of transformers is that they allow you to take sequential data as input into a model, but still allow you to parallelize the computations. This is in contrast to a recurrent neural network (see [[202102201032 Recurrent Neural Networks]]) where computations need to be performed sequentially.
>
> * Training is fast and efficient
> * Transfer learning works (at least for the large language models)
> * Transformer language models can be trained large amounts of unsupervised text. This is similar to how Word2Vec (see [[202102131437 Word2Vec]]) learns word embeddings.
> * The transformer can see the whole document at each time step. In contrast, a RNN can only see time step 4 after it has processed that time step. It can't see it from time step 3 or earlier.


### 202101201758 SGD Converges Faster Than GD With Large Redundant Datasets.txt

> Empirically, stochastic gradient descent ([[202101070827 Stochastic Gradient Descent]]) seems to learn faster than batch gradient descent ([[202101050843 Gradient Descent]]) when you have "large, redundant datasets" [@lecun1998gradient, p. 41].  Why is this the case?  Redundant data means that many of the training examples are almost identical.  Imagine you had a dataset, and then duplicated all of the training examples.  If you were to run batch gradient descent, you would end doing twice as many gradient calculations as necessary.  A single epoch of training wouldn't get any benefit from the duplicated data.  Whereas running SGD once on the whole training set would essentially equal two iterations on true gradient descent.  This thought experiment should generalize well to datasets where training examples are slightly different, and not identical.


