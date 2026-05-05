# Projeto de Reconhecimento de Imagem e Códigos de Assistência

Este projeto reúne uma página web de classificação de imagens em tempo real com câmera e um conjunto de scripts Python de apoio, incluindo verificação de números primos, refatoração de estatísticas e um exemplo de depuração.

## Estrutura do projeto

- `index.html`
  - Página web de demonstração que utiliza TensorFlow.js e Teachable Machine para classificar imagens da webcam.
  - Inclui interface com botão para ativar a câmera, painel de status e probabilidades de classes.
  - O modelo é carregado a partir de um projeto hospedado no Teachable Machine.

- `test-assistence-code/`
  - `debug.py`
    - Exemplo de script de cálculo de compra com entrada de cliente, quantidade, preço, imposto e desconto.
    - Contém lógica corrigida e comentários explicativos sobre decisões importantes.
  - `num_primos.py`
    - Função `eh_primo(numero)` que determina se um número é primo.
    - Exemplos de uso estão incluídos no bloco `if __name__ == "__main__"`.
  - `refatoracao.py`
    - Função `calculate_statistics(numbers)` que retorna soma, média, maior e menor valor de uma lista.
    - Exibe os resultados de teste no terminal.
  - `explicacao-debug.md`
    - Documento com análise dos erros encontrados e das correções aplicadas em `debug.py`.
  - `explicacao_num_primo.md`
    - Explicação passo a passo de como o verificador de números primos funciona.
  - `explicacao_refatoracao.md`
    - Explicação linha a linha do script original de refatoração e observações sobre melhorias.

## Como usar

### Página web

1. Abra `index.html` em um navegador moderno.
2. Clique no botão **Ativar Câmera**.
3. Permita o acesso à webcam quando solicitado.
4. A página exibirá as classes previstas pelo modelo em tempo real.

> Nota: o modelo é carregado de forma remota via Teachable Machine, então uma conexão com a internet é necessária.

### Scripts Python

Execute os scripts com Python 3 a partir do terminal:

```bash
python test-assistence-code/debug.py
python test-assistence-code/num_primos.py
python test-assistence-code/refatoracao.py
```

## O que cada script faz

- `debug.py`
  - Simula a entrada de dados de um cliente, calcula totais dos itens, aplica imposto fixo de 10% e desconta um cupom percentual.
  - Imprime um recibo formatado no console.

- `num_primos.py`
  - Verifica se cada número em uma lista de teste é primo.
  - Usa otimização com verificação até a raiz quadrada e ignora números pares.

- `refatoracao.py`
  - Calcula estatísticas básicas: soma, média, maior e menor valor.
  - Exemplo de como organizar e documentar uma função mais legível.

## Dependências

- Para o aplicativo web:
  - Navegador com suporte a JavaScript e webcam.
  - Internet para carregar TensorFlow.js e Teachable Machine.

- Para os scripts Python:
  - Python 3.x

## Melhorias sugeridas

- Adicionar um arquivo `requirements.txt` ou `Pipfile` caso sejam necessárias dependências Python adicionais no futuro.
- Criar um script de inicialização para demonstrar `index.html` em um servidor local.
- Adicionar testes automatizados para `num_primos.py` e `refatoracao.py`.

## Contato

Este README foi gerado automaticamente com base nos arquivos existentes do projeto.
