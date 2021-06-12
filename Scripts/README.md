The following figure covers how to fine-tune a pretrained Transformer model, provided by the transformers library, by integrating it with TorchText. We use a pretrained BERT model to provide the embeddings for our input text and input these embeddings to a linear layer that will predict tags based on these embeddings.

![WorkFlow_2](https://user-images.githubusercontent.com/73403859/121178050-601e1f80-c85e-11eb-850c-337e22d5fa08.png)

def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs
