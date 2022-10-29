from flask import Flask, jsonify, request

api = Flask(__name__)

paises_api = [
    {"id": "1",
     "nome": "Brasil",
     "capital": "Brasilia",
     "continente": "America do Sul",
     "populacao": "214000000",
     "latitude": "+05o 16'19",
     "longitude": "-60o 12'45",
     "bandeira": "https://http2.mlstatic.com/D_NQ_NP_846593-MLB50471350726_062022-W.jpg"},
    {"id": "2",
     "nome": "Italia",
     "capital": "Roma",
     "continente": "Europa",
     "populacao": "59000000",
     "latitude": "12.4942 41 53 26",
     "longitude": "12 29 39",
     "bandeira": "https://img.freepik.com/vetores-premium/bandeira-italiana-bandeira-da-italia_175392-29.jpg"},
    {"id": "3",
     "nome": "Japao",
     "capital": "Toquio",
     "continente": "Asia",
     "populacao": "125000000",
     "latitude": "139.692 35 41 22",
     "longitude": "139 41 31",
     "bandeira": "https://i.pinimg.com/736x/a5/d6/88/a5d688289cd6850016f14fe93b17da01.jpg"},
]


@api.route("/paises", methods=["GET"])
def paises():
    return jsonify(paises_api)


@api.route("/pais_especifico/<int:id>", methods=["GET"])
def pais_especifico(id):
    filtro = [p for p in paises_api if p["id"] == id]
    if filtro:
        return jsonify(filtro[0])
    else:
        return jsonify({})


@api.route("/paises", methods=["POST"])
def adicionar_pais():
    global paises
    try:
        content = request.get_json()

        ids = [p["id"] for p in paises_api]
        if ids:
            nid = max(ids) + 1
        else:
            nid = 1
        content["id"] = nid
        paises_api.append(content)
        return jsonify({"status": "OK", "msg": "disciplina adicionada com sucesso"})
    except Exception as ex:
        return jsonify({"status": "ERRO", "msg": str(ex)})


@api.route("/pais/<int:id>", methods=["DELETE"])
def deletar(id):
    global paises_api
    try:
        paises = [p for p in paises_api if p["id"] != id]
        return jsonify({"status": "OK", "msg": "disciplina removida com sucesso"})
    except Exception as ex:
        return jsonify({"status": "ERRO", "msg": str(ex)})


if __name__ == "__main__":
    api.run(host="0.0.0.0", debug=True)
