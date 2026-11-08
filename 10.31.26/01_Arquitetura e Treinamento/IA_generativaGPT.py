import random

# Simulação de conhecimento treinado
# Cada palavra possui possíveis palavras ou expressões seguintes.

memoria_treinada = {
    "O": ["ChatGPT", "Python", "SENAI", "aprendizado"],

    "ChatGPT": ["é", "utiliza", "representa"],
    "Python": ["é", "permite", "facilita"],
    "SENAI": ["oferece", "ensina", "desenvolve"],
    "aprendizado": ["de máquina", "artificial", "contínuo"],

    "é": ["uma inteligência artificial",
          "uma ferramenta tecnológica",
          "um modelo de linguagem"],

    "utiliza": ["redes neurais",
                "modelos de linguagem",
                "aprendizado de máquina"],

    "representa": ["uma inovação tecnológica",
                   "um avanço na computação",
                   "uma nova forma de interação"],

    "permite": ["automatizar tarefas",
                "desenvolver aplicações",
                "processar informações"],

    "facilita": ["a programação",
                 "a análise de dados",
                 "a resolução de problemas"],

    "oferece": ["cursos tecnológicos",
                "formação profissional",
                "conhecimento técnico"],

    "ensina": ["programação",
               "tecnologia",
               "inteligência artificial"],

    "desenvolve": ["competências digitais",
                   "soluções inovadoras",
                   "habilidades profissionais"],

    "uma inteligência artificial": ["capaz de gerar textos",
                                    "que aprende padrões",
                                    "que auxilia pessoas"],

    "uma ferramenta tecnológica": ["para apoiar atividades",
                                   "que aumenta a produtividade"],

    "um modelo de linguagem": ["treinado com grandes volumes de texto",
                               "capaz de prever palavras"],

    "redes neurais": ["para identificar padrões",
                      "inspiradas no funcionamento do cérebro"],

    "modelos de linguagem": ["para gerar respostas",
                             "para compreender contextos"],

    "aprendizado de máquina": ["para reconhecer padrões",
                               "para melhorar previsões"],

    "automatizar tarefas": ["com maior eficiência",
                            "e reduzir atividades repetitivas"],

    "desenvolver aplicações": ["inteligentes e interativas",
                               "para diferentes necessidades"],

    "processar informações": ["com rapidez",
                              "e identificar relações entre dados"],

    "a programação": ["e o desenvolvimento de sistemas",
                      "por meio de algoritmos"],

    "a análise de dados": ["e a tomada de decisões",
                           "em diferentes áreas"],

    "a resolução de problemas": ["de forma eficiente",
                                 "com apoio da tecnologia"],

    "cursos tecnológicos": ["para preparar profissionais",
                            "voltados ao mercado de trabalho"],

    "formação profissional": ["com foco na inovação",
                              "para o futuro da indústria"],

    "conhecimento técnico": ["para desenvolver novas soluções",
                             "e acompanhar a transformação digital"]
}


def gerador_generativo(prompt_inicial, tamanho=6):

    frase = [prompt_inicial]
    palavra_atual = prompt_inicial

    for _ in range(tamanho):

        if palavra_atual in memoria_treinada:

            proxima = random.choice(
                memoria_treinada[palavra_atual]
            )

            frase.append(proxima)
            palavra_atual = proxima

        else:
            break

    return " ".join(frase)


# Testando o simulador
prompt = "O"

print("\nPrompt:", prompt)

print(
    "Saída Generativa:",
    gerador_generativo(prompt, tamanho=5)
)
