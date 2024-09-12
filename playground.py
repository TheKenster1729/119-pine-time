# Use a pipeline as a high-level helper
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

login(token = "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")

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125m")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125m") 

prompt = "What is the capital of France?"
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.9,
    max_length=100,
)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")
# pipe(messages)