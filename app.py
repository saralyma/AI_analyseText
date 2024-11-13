from flask import Flask, request, jsonify, render_template
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import os

app = Flask(__name__)

# Configuração do cliente Azure
endpoint = "https://lablanguageservtest.cognitiveservices.azure.com/"
key = "5OPbSVBNUGSsuw99eSu4pAjPmjU4lp38e35SO4iT85EeaAhsOaqjJQQJ99AKACYeBjFXJ3w3AAAaACOGrAvx"

credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resumir", methods=["POST"])
def resumir_texto():
    data = request.get_json()
    texto = data.get("texto")

    # Extrair frases-chave para o resumo
    response = client.extract_key_phrases([texto])
    frases_chave = response[0].key_phrases

    # Gerar o resumo com as frases-chave
    resumo = " - ".join(frases_chave)
    
    return jsonify({"resumo": resumo})

if __name__ == "__main__":
    app.run(debug=True)
