# Question

Explain supervised, unsupervised, weakly supervised, semi-supervised, and active learning.

# Answer

**Supervised learning**: Given examples of inputs and outputs (training data), a machine learning algorithm determines how to solve the problem. The training data teaches the agent what actions to take by providing correct labels or outputs.

**Unsupervised learning**: Attempts to find hidden structure in data without labeled outputs. No correct answers are provided; the algorithm must discover patterns on its own.

**Weakly supervised learning**: Uses noisy, limited, or imprecise labels instead of ground-truth labels. Examples include learning from crowd-sourced labels, distant supervision, or programmatic labeling rules. More scalable than full supervision but requires handling label noise.

**Semi-supervised learning**: Combines a small amount of labeled data with a large amount of unlabeled data. The dominant approach is pre-training then fine-tuning: (1) pre-train a model on abundant unlabeled data to learn general representations, then (2) fine-tune it on a small labeled dataset for a specific task. Examples include language models trained with next-word prediction or masked language modeling (BERT), then fine-tuned on downstream tasks, or CNNs pre-trained on ImageNet and fine-tuned for specific image classification problems. This approach has shown that larger pre-trained models improve performance even on small supervised tasks.

**Active learning**: The learning algorithm actively queries which data points to label next. The model identifies the most informative examples (e.g., those it's most uncertain about) and requests labels for those, minimizing the amount of labeled data needed while maximizing performance.

---

## Extracts from my notes

### 202101091230 Machine Learning vs Traditional Programming.txt

> In contrast, in supervised machine learning, a programmer is given examples of the inputs and outputs.  They feed those training examples to a machine learning algorithm.  It is the role of the algorithm, not the human, to determine _how_ to solve the problem.


### 202110101051 Supervised vs Reinforcement Learning.txt

> In supervised learning, the training data teaches the agent what actions to take. As an example, you could train a model to play Blackjack optimally. The features would be the agent's hand, the dealers hand, and maybe the amount of cash the agent has. Then you would give the agent the optimal action. Those would be the y-values. Those aren't necessarily the optimal actions. But they are the actions we are training or model to make. This frames blackjack as a supervised learning problem.


### 202110171516 Reinforcement Learning vs Unsupervised Learning.txt

> While RL does seem to have some similarities to unsupervised learning, RL is not unsupervised learning [@book:2274176, p.2]. Unsupervised learning attempts to find hidden structure in the data. The objective of RL is to teach an agent to maximize a reward.


### 202201231154 Summary - Semi-supervised Sequence Learning.txt

> The authors pre-train a language model ([[202103040809 Language Model]]) in two different ways. Both methods use LSTMs ([[202102211230 Long Short-Term Memory]]).
>
> 1. In the first method, they build a conventional language model. They feed it unlabeled data and have the model predict the next word in the sequence.
> 2. In the second method, build and train an autoencoder. The encoder reads an unlabeled document, and the decoder is tasked with trying to output the input sentence. They were inspired by, and follow the architecture in [[202103021827 Summary - Sequence to Sequence Learning with Neural Networks]].
>
> They then take the pre-trained models, and use the weights to initialize their supervised model. Then fine tune those weights on the classification tasks at hand.


### 202201240714 Summary - Improving Language Understanding by Generative Pre-Training (GPT-1).txt

> They described their overall goal as follows [@radford2018improving, p.2]:
>
> > Our goal is to learn a universal representation that transfers with little adaptation to a wide range of tasks.
>
> The big contribution of this paper was to combine a large transformer model with a large dataset used for pre-training a language model. Then to use the pre-trained model, with little adaptation, as the base for a supervised model.


### 202201231144 Summary - BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.txt

> This paper basically coined the term, and was the first to do 'Masked Language Modeling' (MLM).
>
> BERT cemented the trend of (1) pre-train a large language model, then (2) fine-tune it on a specific supervised task. This significantly minimized the amount of 'heavily-engineered task-specific architectures' that were created to solve varying NLP tasks.
>
> Lastly, BERT was one of the first papers to show that when using pre-trained models, bigger is better, even if your supervised task has a relatively small dataset.


### 202101260805 How to Use A Pretrained Convolutional Neural Network.txt

> Training a convolutional neural network requires a lot of data.  In practice, you often don't have very large image datasets to train on.  You can attempt to overcome this by re-using a pretrained CNN.
>
> The feature maps at the bottom of a CNN are the most general.  They are the ones that extract features like texture, edges, corners, etc.  These are often general enough to be re-used across a large class of problems.
>
> From Chollet [@chollet2018deep, p. 154]:
>
> > Thus the steps for fine-tuning a network are as follow:
> >
> > 1. Add your custom network on top of an already-trained base network
> > 2. Freeze the base network.
> > 3. Train the part you added.
> > 4. Unfreeze some layers in the base network.
> > 5. Jointly train both these layers and the part you added.


---

## Gaps (not covered in my notes)

**Weakly supervised learning**: [To be filled in]

**Active learning**: [To be filled in]

