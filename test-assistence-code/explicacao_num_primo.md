# Verificador de Números Primos em Python

## Definição e Validação da Função

```python
def eh_primo(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
```
- Define a função `eh_primo` que recebe um parâmetro `numero`
- **numero < 2**: Números menores que 2 não são primos
- **numero == 2**: 2 é o único número primo par
- **numero % 2 == 0**: Rejeita números pares (exceto 2 já tratado)

## Loop Principal

```python
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True
```
- Itera por números ímpares até a raiz quadrada do número
- **range(3, int(numero ** 0.5) + 1, 2)**: começa em 3, vai até √numero, incrementa de 2 em 2
- Se encontrar um divisor, retorna **False**
- Se passar por todos, retorna **True** (é primo)

## Execução e Testes

```python
if __name__ == "__main__":
    numeros_teste = [1, 2, 3, 4, 5, 10, 17, 20, 29, 100]
    for num in numeros_teste:
        resultado = eh_primo(num)
        print(f"{num} é primo: {resultado}")
```
- Define uma lista com números para testar
- Executa a função para cada número e imprime o resultado
- Exemplo: `"2 é primo: True"`, `"4 é primo: False"`

## Resumo

| Etapa | Descrição | Ação |
|-------|-----------|------|
| 1 | numero < 2 | Retorna False |
| 2 | numero == 2 | Retorna True |
| 3 | numero par | Retorna False |
| 4 | Verifica divisores até √n | Retorna False se encontrar |
| 5 | Passou todas as verificações | Retorna True (é primo!) |

**Complexidade**: O(√n) de tempo, O(1) de espaço. Verifica apenas até a raiz quadrada pois qualquer divisor maior teria um correspondente menor.
