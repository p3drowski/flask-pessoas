from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de dados simulada
pessoas = [
    {"id": 1, "nome": "Pedro Pessoa", "idade": 19, "cidade": "Belo Horizonte", "cpf": "11111111111"},
    {"id": 2, "nome": "João Feniman", "idade": 30, "cidade": "São Paulo", "cpf": "22222222222"},
    {"id": 3, "nome": "Maria Eduarda", "idade": 20, "cidade": "Curitiba", "cpf": "33333333333"},
    {"id": 4, "nome": "Amabile Rocha", "idade": 29, "cidade": "Campinas", "cpf": "44444444444"},
    {"id": 5, "nome": "Douglas Costa", "idade": 35, "cidade": "Rio de Janeiro", "cpf": "55555555555"},
    {"id": 6, "nome": "Rafael Oliveira", "idade": 33, "cidade": "Salvador", "cpf": "66666666666"},
    {"id": 7, "nome": "Helio Silva", "idade": 30, "cidade": "Fortaleza", "cpf": "77777777777"},
    {"id": 8, "nome": "Alexandro Santos", "idade": 31, "cidade": "Porto Alegre", "cpf": "88888888888"},
    {"id": 9, "nome": "Lucas Martins", "idade": 27, "cidade": "Brasília", "cpf": "99999999999"},
    {"id": 10, "nome": "Carolina Souza", "idade": 30, "cidade": "Recife", "cpf": "00000000000"},
]

# ------------------------
# Rota 1 - listar todas
# ------------------------
@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    return jsonify({
        "quantidade": len(pessoas),
        "pessoas": pessoas
    })

# ------------------------
# Rota 2 - buscar por CPF
# Exemplo: /pessoas/cpf/11111111111
# ------------------------
@app.route('/pessoas/cpf/<cpf>', methods=['GET'])
def buscar_por_cpf(cpf):
    for p in pessoas:
        if p["cpf"] == cpf:
            return jsonify(p)
    return jsonify({"erro": "CPF não encontrado"}), 404

# ------------------------
# Rota 3 - buscar por idade
# Exemplo: /pessoas/idade/30
# ------------------------
@app.route('/pessoas/idade/<int:idade>', methods=['GET'])
def buscar_por_idade(idade):
    resultados = [p for p in pessoas if p["idade"] == idade]
    if resultados:
        return jsonify({
            "quantidade": len(resultados),
            "pessoas": resultados
        })
    return jsonify({"erro": "Nenhuma pessoa encontrada com essa idade"}), 404

# ------------------------
# Rota 4 - buscar via parâmetro (?cpf= ou ?idade=)
# Exemplo: /buscar?cpf=11111111111  ou  /buscar?idade=30
# ------------------------
@app.route('/buscar', methods=['GET'])
def buscar_via_parametro():
    cpf = request.args.get('cpf')
    idade = request.args.get('idade')

    # Busca por CPF
    if cpf:
        for p in pessoas:
            if p["cpf"] == cpf:
                return jsonify(p)
        return jsonify({"erro": "CPF não encontrado"}), 404

    # Busca por idade
    if idade:
        try:
            idade = int(idade)
        except ValueError:
            return jsonify({"erro": "A idade deve ser um número"}), 400

        resultados = [p for p in pessoas if p["idade"] == idade]
        if resultados:
            return jsonify({
                "quantidade": len(resultados),
                "pessoas": resultados
            })
        return jsonify({"erro": "Nenhuma pessoa encontrada com essa idade"}), 404

    return jsonify({"erro": "Informe 'cpf' ou 'idade' como parâmetro"}), 400

# ------------------------
# Inicializa o servidor
# ------------------------
if __name__ == '__main__':
    print("Servidor rodando em http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
