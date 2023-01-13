import torch
from transformers import (AutoConfig, AutoTokenizer, GPT2LMHeadModel)


def generate_joke(lauch: str) -> str:
    model_name = './StirlitzJokeOnRuGPT2_Medium'
    config = AutoConfig.from_pretrained(model_name)
    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = GPT2LMHeadModel.from_pretrained(model_name, config=config).to(DEVICE)

    text = lauch
    input_ids = tokenizer.encode(text, return_tensors="pt").to(DEVICE)
    model.eval()
    with torch.no_grad():
        out = model.generate(input_ids,
                             do_sample=True,
                             temperature=0.6,
                             top_p=1,
                             top_k=40,
                             max_length=300,
                        )

    generated_text = list(map(tokenizer.decode, out))[0]
    return generated_text[:generated_text.find('<|end|>')]
