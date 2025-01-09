import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel


tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
model = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased")
model.eval()


def embed(text: str) -> np.ndarray[float]:
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)

    embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
    return embeddings
