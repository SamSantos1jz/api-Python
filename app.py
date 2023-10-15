from flask import Flask, jsonify, request


app = Flask(__name__)

pecas = [
    {
        'id': 1,
        'peca' : 'bateria',
        'descricao':'bateria moura'
    },
    {
        'id': 2,
        'peca' : 'bubina',
        'descricao':'bubina generica'
    },
    {
        'id': 3,
        'peca' : 'filtro de oleo',
        'descricao':'filtro de oleo generico'
    }
]


@app.route('/pecas', methods=['GET'])
def obter_pecas():
    return jsonify(pecas)

@app.route('/pecas/<int:id>', methods=['GET'])
def obter_pecas_id(id):
    for peca in pecas:
      if peca.get('id') == id:
            return jsonify(peca)

@app.route('/pecas/<int:id>', methods=['PUT'])
def editar_peca_id(id):
    peca_dif = request.get_json()
    for indice,peca in enumerate(pecas):
        if peca.get('id') == id:
            pecas[indice].update(peca_dif)
            return jsonify(pecas[indice])


@app.route('/pecas', methods=['POST'])
def incluir_nova_peca():
    nova_peca = request.get_json()
    pecas.append(nova_peca)

    return jsonify(pecas)

@app.route('/pecas/<int:id>', methods=['DELETE'])
def excluir_peca(id):
    for indice, peca in enumerate(pecas):
        if peca.get('id') == id:
            del pecas[indice]
        return jsonify(pecas)

app.run(port=5000, host='localhost', debug=True)