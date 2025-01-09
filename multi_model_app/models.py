from transformers import pipeline

class ModelIterator:
    def __init__(self, models):
        self.models = models
        self.current_model_index = 0
        self.pipelines = [pipeline("text-generation", model=model) for model in models]

    def switch_model(self):
        self.current_model_index = (self.current_model_index + 1) % len(self.models)

    def query(self, question):
        text_generation_pipeline = self.pipelines[self.current_model_index]
        # Generar una respuesta basada en la pregunta
        result = text_generation_pipeline(question, max_length=50, num_return_sequences=1)
        return result[0]['generated_text'] 