# import torch

# checkpoint = torch.load('C:\\Users\\mehal\\Downloads\\18786Project\\AttnGAN\\models\\cocoAttnGAN2_100.pth', map_location=lambda storage, loc: storage)
# print(checkpoint.keys())

# # Print the dimensions of each parameter
# for name, param in checkpoint.items():
#     print(f"{name}: {param.size()}")

import torch
import torch.nn as nn
from transformers import CLIPTextModel, CLIPProcessor

class CLIP_ENCODER(nn.Module):
    def __init__(self, model_name='openai/clip-vit-base-patch32', embedding_dim=256):
        super(CLIP_ENCODER, self).__init__()
        # Use CLIPTextModel for text-only tasks
        self.clip_text_model = CLIPTextModel.from_pretrained(model_name)
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.embedding_dim = embedding_dim
        # Define the transformation layer to adjust embedding dimensions
        self.transform_sentence = nn.Linear(self.clip_text_model.config.hidden_size, embedding_dim)
        self.transform_word = nn.Linear(self.clip_text_model.config.hidden_size, embedding_dim)

    def forward(self, captions):
        # Process captions to match the input format expected by CLIP
        inputs = self.processor(text=captions, return_tensors="pt", padding=True, truncation=True).to(self.clip_text_model.device)
        attention_mask = inputs['attention_mask']
        # Get the outputs from the CLIP text model
        outputs = self.clip_text_model(**inputs)

        # Transform sentence embeddings to the desired dimension
        sentence_embeddings = self.transform_sentence(outputs.pooler_output)

        # Transform each word embedding to the desired dimension
        word_embeddings = self.transform_word(outputs.last_hidden_state).transpose(1, 2)

        return word_embeddings, sentence_embeddings, attention_mask

# Usage example
captions = ["a cat of a cat in a den is sleeping", "dog"]
model = CLIP_ENCODER()
word_embeddings, sentence_embeddings, attention_mask = model(captions)


print(word_embeddings.shape, sentence_embeddings.shape, attention_mask)
