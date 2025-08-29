# De segundos para HH:MM:SS (e de volta) em Python — simples e rápido

_Transforme segundos em um relógio legível e converta horários de volta para segundos com poucas
linhas de Python._

Neste guia curto e prático, vou mostrar exatamente como converter uma quantidade de segundos em um
formato de horário (`HH:MM:SS`) e também fazer o caminho inverso: pegar um horário como string e
voltar para o total em segundos. Essa é uma necessidade comum em scripts do dia a dia — no meu
caso, usei para montar uma playlist e formatar durações bonitinhas.

A ideia é manter tudo direto ao ponto, com exemplos reais e alguns testes rápidos para você
validar localmente.

## Objetivo

- Receber um número inteiro de segundos e retornar `HH:MM:SS`.
- Receber uma string `HH:MM:SS` e retornar o total em segundos.

## Conversão: segundos → `HH:MM:SS`

Uma forma prática de formatar duração é aproveitar `datetime` e `timedelta`. A gente cria uma data
base e soma os segundos; depois, formata com f-string usando o especificador de data/hora.

```python
from datetime import datetime, timedelta

def seconds_to_hms(total_seconds: int) -> str:
    # Baseia-se em uma data qualquer (ano/mês/dia) e soma a duração
    base = datetime(1, 1, 1, 0, 0, 0) + timedelta(seconds=total_seconds)
    # Formata somente a parte de hora:minuto:segundo
    return f"{base:%H:%M:%S}"
```

Exemplos rápidos:

```python
print(seconds_to_hms(1))       # 00:00:01
print(seconds_to_hms(10))      # 00:00:10
print(seconds_to_hms(60))      # 00:01:00
print(seconds_to_hms(70))      # 00:01:10
print(seconds_to_hms(3600))    # 01:00:00
print(seconds_to_hms(3599))    # 00:59:59
```

### Observação importante (24h)

Essa abordagem trabalha com hora/minuto/segundo. Ao atingir 24 horas (86.400 segundos), o relógio
“zera” para `00:00:00`. Por exemplo:

```python
print(seconds_to_hms(86400))   # 00:00:00  (vira o dia)
print(seconds_to_hms(86399))   # 23:59:59
```

Para muitas aplicações, isso é aceitável. Se você precisa exibir durações maiores que 24h sem
zerar, deixo uma opção mais abaixo.

## Conversão: `HH:MM:SS` → segundos

Agora o caminho inverso: recebemos uma string no formato `HH:MM:SS` e somamos tudo convertido para
segundos. Uma forma elegante é percorrer os componentes de trás para frente, multiplicando por 1,
60, 3600, etc.

```python
def hms_to_seconds(hms: str) -> int:
    parts = hms.split(":")
    total = 0
    multiplier = 1

    for part in reversed(parts):
        total += int(part) * multiplier
        multiplier *= 60

    return total
```

Exemplos rápidos:

```python
print(hms_to_seconds("00:00:01"))  # 1
print(hms_to_seconds("00:01:10"))  # 70
print(hms_to_seconds("01:00:00"))  # 3600
print(hms_to_seconds("00:59:59"))  # 3599
```

## (Opcional) Lidando com durações acima de 24h

Se você quer evitar o “zerar” após 24h, pode formatar manualmente com `divmod` — sem depender de
`datetime` para a saída:

```python
def seconds_to_hms_unbounded(total_seconds: int) -> str:
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(seconds_to_hms_unbounded(86400))   # 24:00:00
print(seconds_to_hms_unbounded(90061))   # 25:01:01
```

## Testes rápidos (sanidade)

Se quiser conferir tudo de uma vez, rode este snippet:

```python
if __name__ == "__main__":
    # ida
    assert seconds_to_hms(1) == "00:00:01"
    assert seconds_to_hms(10) == "00:00:10"
    assert seconds_to_hms(60) == "00:01:00"
    assert seconds_to_hms(70) == "00:01:10"
    assert seconds_to_hms(3600) == "01:00:00"
    assert seconds_to_hms(3599) == "00:59:59"

    # volta
    assert hms_to_seconds("00:00:01") == 1
    assert hms_to_seconds("00:01:10") == 70
    assert hms_to_seconds("01:00:00") == 3600
    assert hms_to_seconds("00:59:59") == 3599

    # limite de 24h (versão datetime zera)
    assert seconds_to_hms(86399) == "23:59:59"
    assert seconds_to_hms(86400) == "00:00:00"

    print("Tudo certo! ✅")
```

## Conclusão

Com poucas linhas você cobre os dois sentidos de conversão entre segundos e `HH:MM:SS`. Para
resultados "estilo relógio", `datetime + timedelta` resolve bem; se a sua necessidade é exibir
durações acima de 24h sem reiniciar, a versão com `divmod` dá conta do recado.

Use o que fizer mais sentido para seu caso e siga em frente. Bons códigos e até o próximo! 🚀
