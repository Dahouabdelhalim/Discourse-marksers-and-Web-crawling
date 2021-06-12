# 1. FlauBERT models
**FlauBERT** is a French BERT trained on a very large and heterogeneous French corpus. Models of different sizes are trained using the new CNRS  (French National Centre for Scientific Research) [Jean Zay](http://www.idris.fr/eng/jean-zay/ ) supercomputer.

The following figure covers how to fine-tune a pretrained Transformer model, provided by the transformers library, by integrating it with TorchText. We use a pretrained BERT model to provide the embeddings for our input text and input these embeddings to a linear layer that will predict tags based on these embeddings.

![WorkFlow_2](https://user-images.githubusercontent.com/73403859/121178050-601e1f80-c85e-11eb-850c-337e22d5fa08.png)

In our work, we will test all the versions of flaubert to decide which version we will go forward with.The following table contains all the information about the FlauBERT models.

| Model name | Number of layers | Attention Heads | Embedding Dimension | Total Parameters |
| :------:       |   :---: | :---: | :---: | :---: |
| `flaubert-small-cased` | 6    | 8    | 512   | 54 M |
| `flaubert-base-uncased`  | 12  | 12  | 768  | 137 M |
| `flaubert-base-cased`   | 12   | 12      | 768   | 138 M |
| `flaubert-large-cased`  | 24   | 16     | 1024 | 373 M |

The pretrained models are available for download from [here](https://zenodo.org/record/3627732) or via Hugging Face's library.


