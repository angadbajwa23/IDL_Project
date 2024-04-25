import torch
import torch.nn as nn
import clip

class CLIP_ENCODER(nn.Module):
    def __init__(self, nef):
        super(CLIP_ENCODER, self).__init__()
        self.nef = nef
        self.clip_model, _ = clip.load('ViT-B/32', device='cuda')
        self.clip_model = self.clip_model.float()  # Load model to CUDA
        for param in self.clip_model.parameters():
            param.requires_grad = False

        self.emb_features = nn.Linear(768, nef*17*17)
        self.emb_cnn_code = nn.Linear(self.clip_model.visual.output_dim, nef)

    def forward(self, x):
        img = x
        x = x.float()  # Ensure input is in float32
        with torch.no_grad():
            x = self.clip_model.visual.conv1(x)
            x = x.flatten(2)
            x = x.transpose(1, 2)
            x = self.clip_model.visual.ln_pre(x)

            for i, layer in enumerate(self.clip_model.visual.transformer.resblocks):
                x = layer(x)
                if i == 7:
                    intermediate_features = x.mean(dim=1)

        features = self.emb_features(intermediate_features)
        with torch.no_grad():
            image_features = self.clip_model.encode_image(img)
        cnn_code = self.emb_cnn_code(image_features)
        return features, cnn_code

# Usage
model = CLIP_ENCODER(nef=256).to('cuda')
images = torch.randn(5, 3, 224, 224).to('cuda').float()
features, cnn_code = model(images)
