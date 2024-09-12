from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

class LLM:
    def __init__(self, model_name):
        login(token = "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")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate(self, prompt):
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        gen_tokens = self.model.generate(
            input_ids, do_sample=True, temperature=0.9, max_length=100)
        gen_text = self.tokenizer.batch_decode(gen_tokens)[0]
        return gen_text