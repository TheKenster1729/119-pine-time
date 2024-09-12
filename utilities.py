from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
from sklearn.neighbors import KDTree
import json
import numpy as np

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
    
class PersonalityComparison:
    def __init__(self, scores):
        self.scores = scores
        self.data = json.load(open("scores.json"))

        # make scores an array
        X = np.array([list(self.data[i].values()) for i in self.data.keys()])
        self.tree = KDTree(X)

    def find_nearest_neighbors(self, query):
        query = np.array([query])
        distances, indices = self.tree.query(query, k=1)
        if indices[0][0] == 0:
            return "You are most similar to Kenny"
        elif indices[0][0] == 1:
            return "You are most similar to Ruben"
        else:
            return "You are most similar to Will"