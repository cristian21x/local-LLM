from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, AutoModelForImageClassification
import torch
from PIL import Image

class ModelIterator:
    def __init__(self, models):
        self.models = models
        self.current_model_index = 0
        self.pipelines = []
        
        for model in models:
            try:
                if "Qwen" in model:
                    tokenizer = AutoTokenizer.from_pretrained(model)
                    generator = pipeline(
                        "text-generation",
                        model=model,
                        tokenizer=tokenizer,
                        device=0 if torch.cuda.is_available() else -1
                    )
                    self.pipelines.append(generator)
                elif "vit" in model:
                    classifier = pipeline(
                        "image-classification",
                        model=model,
                        device=0 if torch.cuda.is_available() else -1
                    )
                    self.pipelines.append(classifier)
                else:
                    self.pipelines.append(None)
            except Exception as e:
                print(f"Error loading model {model}: {str(e)}")
                self.pipelines.append(None)

    def switch_model(self):
        self.current_model_index = (self.current_model_index + 1) % len(self.models)
        while self.pipelines[self.current_model_index] is None:
            self.current_model_index = (self.current_model_index + 1) % len(self.models)

    def query(self, text=None, image=None):
        try:
            pipeline = self.pipelines[self.current_model_index]
            if pipeline is None:
                return "Error: El modelo actual no está disponible."
            
            if text:
                result = pipeline(text, max_length=50, num_return_sequences=1)
                return result[0]['generated_text']
            
            elif image:
                img = Image.open(image)
                result = pipeline(img)
                return result
            
        except Exception as e:
            return f"Error al procesar la entrada: {str(e)}"