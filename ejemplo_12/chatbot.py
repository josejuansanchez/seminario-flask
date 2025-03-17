import tensorflow as tf
import numpy as np
import json

"""
TODO: La clase está incompleta
"""
class Chatbot:
    def __init__(self, model_path, vocab_path, labels_path):
        """
        El constructor está incompleto
        """
        pass

    def procesar_mensaje(self, mensaje):
        # Simulación de predicción
        categorias = {
            0: "Consulta general",
            1: "Soporte técnico",
            2: "Información de servicios"
        }
        import random
        prediccion = random.choice([0, 1, 2])
        return f"{categorias[prediccion]}"