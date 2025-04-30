from flask import Flask, request, jsonify

app = Flask(__name__)

mensagens = []
proximo_id = 1

@app.route('/mensagens', methods=['POST'])
def criar_mensagem():
    global proximo_id
    conteudo = request.json.get('conteudo')
    if not conteudo:
        return jsonify({"erro": "Campo 'conteudo' é obrigatório"}), 400
    nova = {"id": proximo_id, "conteudo": conteudo}
    mensagens.append(nova)
    proximo_id += 1
    return jsonify(nova), 201

@app.route('/mensagens', methods=['GET'])
def listar_mensagens():
    return jsonify(mensagens), 200

@app.route('/mensagens/<int:id>', methods=['GET'])
def obter_mensagem(id):
    for m in mensagens:
        if m['id'] == id:
            return jsonify(m), 200
    return jsonify({"erro": "Mensagem não encontrada"}), 404

@app.route('/mensagens/<int:id>', methods=['PUT'])
def atualizar_mensagem(id):
    for m in mensagens:
        if m['id'] == id:
            conteudo = request.json.get('conteudo')
            if not conteudo:
                return jsonify({"erro": "Campo 'conteudo' é obrigatório"}), 400
            m['conteudo'] = conteudo
            return jsonify(m), 200
    return jsonify({"erro": "Mensagem não encontrada"}), 404

@app.route('/mensagens/<int:id>', methods=['DELETE'])
def deletar_mensagem(id):
    global mensagens
    mensagens = [m for m in mensagens if m['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

