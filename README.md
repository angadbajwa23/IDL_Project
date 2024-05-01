# 18786 Project: Enhancing Text-to-Image Generation with Fine-Grained Semantic Control

Enhance the AttnGAN model using state-of-the-art technology such as BERT and CLIP models for richer text interpretation and more detailed image outputs.

### Branch Info

- master: The original branch of AttGAN updated to latest torch versions with improved-gan from OpenAI for Inception Score calculation. Serves as our baseline for DAMSM with RNN text encoder and CNN image encoder.
- bert: DAMSM with BERT based text encoder and CNN image encoder
- clip: DAMSM with RNN based text encoder and CLIP image encoder
- clip-text-image: DAMSM with CLIP text encoder and CLIP image encoder


### Data

1. Download preprocessed metadata for[coco](https://drive.google.com/open?id=1rSnbIGNDGZeHlsUlLdahj0RJ9oo6lgH9) and save them to `data/`
2. Download [coco](http://cocodataset.org/#download) dataset and extract the images to `data/coco/`



### Dependencies


`pip install` the following packages:
- `python-dateutil`
- `easydict`
- `pandas`
- `torchfile`
- `nltk`
- `scikit-image==0.19.0`
- `torch`
