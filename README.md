# 2026-2-unievangelica-payments

Atividade de testes unitários para o sistema de pagamentos - Versão Aprimorada com Testes Completos

## 📋 Estrutura do Projeto

- `app/pagamentos.py`: Módulo principal com funções de cálculo de desconto, juros, validação de pagamento e processamento de reembolso
- `tests/test_pagamentos.py`: Suite completa de testes unitários usando pytest
- `venv/`: Ambiente virtual Python

## 🚀 Como Executar os Testes

### Método 1: Usando Ambiente Virtual (Recomendado)

1. **Criar e ativar o ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Instalar dependências:**
   ```bash
   pip install pytest
   ```

3. **Executar todos os testes:**
   ```bash
   pytest tests/test_pagamentos.py -v
   ```

### Método 2: Sem Ambiente Virtual

```bash
python3 -m pytest tests/test_pagamentos.py -v
```

## 📊 Relatório de Testes

### Status Atual: ✅ **11 TESTES PASSANDO**

### 🐛 Bugs Corrigidos

#### 1. Bug em `test_aplicar_juros_atraso`
- **Problema:** Teste esperava valor incorreto (150) em vez do cálculo correto de juros simples de 1% ao dia (105)
- **Correção:** Ajustado de `assert aplicar_juros_atraso(100, 5) == 150` para `assert aplicar_juros_atraso(100, 5) == 105`
- **Impacto:** Teste agora reflete corretamente a fórmula: `valor + (valor * 0.01 * dias)`

### ✅ Testes Implementados

#### Testes Originais Corrigidos
1. **`test_calcular_desconto`** - Testa cálculo de desconto padrão
2. **`test_aplicar_juros_atraso`** - Testa aplicação de juros simples de 1% ao dia ✅ **CORRIGIDO**

#### Testes Obrigatórios Implementados
3. **`test_validar_metodo_pagamento`** - Testa métodos de pagamento aceitos e rejeitados
4. **`test_processar_reembolso`** - Testa reembolsos válidos e inválidos

#### Testes Adicionais (Edge Cases)
5. **`test_calcular_desconto_edge_cases`** - Testa desconto de 0% e 100%
6. **`test_aplicar_juros_atraso_edge_cases`** - Testa valores negativos e zero
7. **`test_validar_metodo_pagamento_case_sensitive`** - Testa case insensitive

#### Novas Funcionalidades e Testes
8. **`test_validar_valor_pagamento`** - Valida valores positivos/negativos
9. **`test_calcular_parcelas`** - Calcula parcelas com validação
10. **`test_aplicar_multa_cancelamento`** - Aplica multas por cancelamento
11. **`test_fluxo_completo_pagamento`** - Teste de integração completa

## 🆕 Novas Funcionalidades Adicionadas

### 1. `validar_valor_pagamento(valor)`
Valida se o valor do pagamento é positivo.
```python
assert validar_valor_pagamento(100) == True
assert validar_valor_pagamento(0) == False
assert validar_valor_pagamento(-50) == False
```

### 2. `calcular_parcelas(valor_total, num_parcelas)`
Calcula o valor de cada parcela com validação.
```python
assert calcular_parcelas(100, 2) == 50
assert calcular_parcelas(100, 0) == -1  # Inválido
```

### 3. `aplicar_multa_cancelamento(valor, taxa_multa=10)`
Aplica multa por cancelamento (padrão 10%).
```python
assert aplicar_multa_cancelamento(100) == 110
assert aplicar_multa_cancelamento(200, 5) == 210
```

## 🎯 Menu Interativo Aprimorado

O sistema agora inclui 7 opções no modo interativo:

1. Calcular Desconto
2. Aplicar Juros de Atraso
3. Validar Método de Pagamento
4. Processar Reembolso
5. **Validar Valor de Pagamento** (NOVO)
6. **Calcular Parcelas** (NOVO)
7. **Aplicar Multa por Cancelamento** (NOVO)

Execute o modo interativo com:
```bash
python3 app/pagamentos.py
```

## 📈 Evolução dos Testes

| Estado    | Testes Passando | Testes Falhando |
| -----------| -----------------| -----------------|
| **ANTES** | 1               | 1               |
| **AGORA** | 11              | 0               |


## 📝 Resumo das Atividades Realizadas

1. ✅ **Corrigido bug** no teste de juros (150 → 105)
2. ✅ **Implementados** testes obrigatórios para `validar_metodo_pagamento` e `processar_reembolso`
3. ✅ **Adicionados** 7 testes adicionais com edge cases e novas funcionalidades
4. ✅ **Implementadas** 3 novas funções no sistema de pagamentos
5. ✅ **Atualizado** menu interativo com novas opções
6. ✅ **Documentado** todo o processo neste README

## 🏆 Resultado Final

**Status:** Todos os 11 testes passando com sucesso! 🎉

O sistema agora está muito mais robusto com cobertura completa de testes, validação de edge cases e funcionalidades adicionais que demonstram domínio das técnicas de teste de software.