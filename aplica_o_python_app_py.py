from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "mensagem": "API do Gerenciador de Senhas do Jhonatan"
    })

@app.route('/carregar-planilha', methods=['GET'])
def carregar_planilha():
    try:
        # Lê o arquivo senhas.xlsx
        df = pd.read_excel('senhas.xlsx')
        dados = df.to_dict(orient='records')
        return jsonify({"sucesso": True, "dados": dados})
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)