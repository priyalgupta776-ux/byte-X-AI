1. Problem Statement
The challenge required a classifier for six natural-scene categories: buildings, forest, glacier, mountain,
sea, and street. The central constraint was that ResNet-18 was fixed and had to be trained from scratch.
Consequently, the intended optimization strategy was data-centric: improve the training data rather than
changing the model architecture or using pretrained weights.
The supplied data contained 600 labeled seed images (100 per class), 6,000 initially undefined images, a
balanced 1,200-image validation set, and an 1,800-image hidden test set. The final active training table
could contain at most 3,000 rows with weight = 1, including the 600 seed labels.
2. Dataset and Classes
The six target classes were mapped to integer labels as follows: 0 = buildings, 1 = forest, 2 = glacier, 3 =
mountain, 4 = sea, and 5 = street. Undefined samples were kept outside the six-class training target until
selected and verified during data curation.
3. Model and Training
The implementation used torchvision ResNet-18 with random initialization (weights=None), satisfying the
train-from-scratch requirement. The ResNet feature representation was followed by a classifier with layers
512→256→128→6, ReLU activations, and dropout.
Training used Adam with learning rate 0.0001, batch size 16, and 10 epochs, with a StepLR learning-rate
schedule. Training augmentation included resize, random crop, horizontal flip, and random affine
transformations. Validation used resize and center crop before normalization.
4. 3LC Data-Centric Workflow
Each training run was tracked in 3LC with per-sample predictions, confidence, classification metrics, and
embeddings. The workflow followed a repeated train → analyze → curate → retrain cycle.
In the analysis stage, the 3LC Dashboard was used to inspect embeddings, predictions, confidence, and
difficult examples. Undefined samples were treated as candidates rather than automatically accepted
pseudo-labels. Selected samples were reviewed, assigned verified labels, and activated with weight = 1;
samples not selected remained inactive with weight = 0.
5. Embedding-Guided Analysis
Embeddings were reduced to three dimensions using UMAP for visualization in the 3LC Dashboard. This
provided a visual representation of the learned feature space and helped inspect clusters, ambiguous
examples, and model behavior across the six classes.
Confidence and predicted-label filters were used to narrow the large undefined pool to promising
candidates. High confidence was used as a candidate-selection signal, followed by visual verification. This was especially important for visually similar categories such as glacier and mountain.
6. Label Curation and Weighting
The data-centric improvement came from selectively incorporating useful examples from the undefined
pool. Instead of activating all predictions, candidates were filtered and inspected. Verified examples were
assigned their appropriate class and weight = 1, while unselected samples retained weight = 0.
The labeling budget was respected throughout the process: the final active training table was limited to
3,000 weight-1 rows, including the origin
7. Iterative Results
The main development accuracy checkpoints were: baseline 67.25%, first improvement ≈71%,
subsequent improvement ≈73.92%, then ≈76.83%, and a finalized development result of approximately
76%. This progression showed that repeated data curation improved performance while the model
architecture remained constrained.
8. Prediction and Submission
After the final training iteration, the trained checkpoint was used by the prediction pipeline to generate
test predictions. The required submission format contains image_id, prediction, and confidence.
Predictions use class IDs 0–5 and confidence values in the range 0-1.
9. Key Learnings
The main lesson was that aggregate accuracy alone does not explain model behavior. Per-sample metrics
and embeddings make it possible to find useful data, investigate uncertain examples, and improve the
training distribution.
A second lesson was that confidence should guide inspection rather than replace it. High-confidence
predictions can still be wrong, so visual verification is important before turning undefined samples into training data.
10. Conclusion
The final solution followed the intended data-centric methodology of the challenge. Rather than changing
ResNet-18, using pretrained weights, or introducing external image data, the project progressively
improved the training dataset through 3LC tables, embeddings, per-sample metrics, labeling, and sample
weighting.
Starting from 67.25% development accuracy, the iterative process reached approximately 76% on the
finalized development/validation run. The resulting project provides both a trained scene classifier and an
auditable record of the data-centric experimentation process.
