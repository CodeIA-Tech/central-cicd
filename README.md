
# 🚀 Central CI/CD Actions

Bem-vindo ao repositório **Central CI/CD Actions!**
Aqui você encontra **pipelines e actions compartilhadas** para padronizar e acelerar o setup de CI/CD em multiplos projetos para sua organização.


## 💡 Visão Geral

Este repositório tem como objetivo: 

- 🏗️ **Centralizar** ações e pipelines customizadas em um só lugar.
- ♻️ **Reutilizar** código e práticas de CI/CD nos projetos.
- 🔒 **Garantir governança**, compliance e segurança. 
- 📦 **Facilitar onboarding** de novos projetos e times.


## 🧰 Estrutura do Projeto

```yaml
.github/
└── actions/
    └── cd/ 
    └── ci/
        └── python/
            └── setup/
                └── action.yml
            └── test/
                └── action.yml
        ...
```

Cada linguagem/stack pode ter seu próprio conjunto de actions reunitláveis.

## 🐍 Exemplo de Uso: Python

No sey projeto Python, adcine um workflow .github/workflows/ci.yml assim:

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python CI
        uses: CodeIA-Tech/central-cicd/.github/actions/ci/python/setup@main
        with:
            python-version: 3.11
 
     ...
```


## 🛠️ Como contribuir

Quer colaborar? Aqui é espaço aberto!
Veja como contribuir:

- 👩‍💻 Sugira melhorias ou novas actions via issues ou pull requests.
- 📝 Ajude a documentar.
- 🧪 Teste e reporte bugs.

**Passos para contribuir**

1. Fork no repositório.
2. Crie uma branch com sua feature/fix.
3. Abra um **Pull Request** com sua sugestão.
4. Aguarde revisão da comunidade e dos maintainers.


## 🔒 Boas Práticas e Segurança

- Nunca suba secrets ou credenciais sensíveis. 
- Use sempre variáveis e secrets do Github Actions.
- Faça review de PRs de terceiros.

## 📄 Licença 

Distribuído sob licença MIT. Veja LICENSE para mais detalhes. 

## 🤝 Contato

Dúvidas, sugestões ou problemas?
Abra uma issue ou fale com os maintaners! 

Feito com 💙 por toda a comunidade DevOps & Platform Engineering!