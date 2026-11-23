
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
├── actions/
│   └── ci/
│       └── python/
│           ├── setup/action.yml
│           └── test/action.yml
└── workflows/
    └── python-docker-ci.yml
```

Cada linguagem/stack pode ter seu próprio conjunto de actions e workflows
reutilizáveis.

## 🐍 Exemplo de Uso: Python

No projeto consumidor, adicione um workflow `.github/workflows/ci.yml`:

```yaml
name: Python CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: CodeIA-Tech/central-cicd/.github/actions/ci/python/setup@main
        with:
          python-version: "3.11"
      - uses: CodeIA-Tech/central-cicd/.github/actions/ci/python/test@main
```

As actions instalam `requirements.txt` quando presente. A action de testes
instala e executa Flake8, Black e isort em modo de verificação, além de executar
pytest quando existe um diretório `tests/`. Ela usa o Python ativo no runner;
seu input `python-version` é mantido por compatibilidade e não seleciona o
interpretador. Configure a versão com a action de setup.

Para projetos com caminhos diferentes, informe `requirements-file` nas duas
actions e `tests-directory` na action de testes. Arquivos de dependências
personalizados ausentes falham; o padrão `requirements.txt` continua opcional.
Use `require-tests: "true"` para exigir o diretório de testes e
`run-lint: "false"` para desativar as três verificações de lint enquanto o
projeto prepara sua adoção. Por padrão, os testes ausentes são ignorados e o
lint permanece habilitado. Um diretório existente sem testes falha no pytest.

## 🐳 Workflow reutilizável: Python e Docker

`python-docker-ci.yml` centraliza testes Python (`unittest` ou `pytest`), build
Docker, smoke test HTTP e publicação opcional no GHCR. A imagem publicada é
carregada do artefato criado após os testes, evitando reconstruí-la no job de
publicação. A publicação ocorre somente em `push` para a branch configurada;
pull requests executam testes, build e smoke test, mas não publicam.

Exemplo de consumidor:

```yaml
name: MCP CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  mcp:
    permissions:
      contents: read
      packages: write
    uses: CodeIA-Tech/central-cicd/.github/workflows/python-docker-ci.yml@<reviewed-commit-sha>
    with:
      python-version: "3.12"
      requirements-file: mcp/requirements.txt
      tests-directory: tests
      test-runner: unittest
      dockerfile: mcp/Dockerfile
      build-context: .
      image-name: ghcr.io/codeia-tech/devops-mcp
      container-port: 8765
      health-path: /health
      publish-image: true
```

O workflow de consumo continua responsável pelos gatilhos. Use a saída
`needs.mcp.outputs.image-ref` para obter a referência imutável publicada. A
permissão `packages: write` deve ser concedida ao job consumidor quando
`publish-image: true`; o workflow só publica na branch configurada e o job de
testes permanece com `contents: read`. A configuração de acesso do pacote GHCR
também deve permitir o `GITHUB_TOKEN` do repositório consumidor. Passe a
referência de `central-cicd` por SHA completo ou release revisada, não por
`main`. O workflow não faz deploy.

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