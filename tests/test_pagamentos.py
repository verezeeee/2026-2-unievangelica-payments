import sys
import os

# Adiciona o diretório pai ao sys.path para garantir que o módulo 'app' seja encontrado,
# independente da pasta de onde o aluno rode o pytest.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.pagamentos import (
    calcular_desconto,
    aplicar_juros_atraso,
    validar_metodo_pagamento,
    processar_reembolso,
    validar_valor_pagamento,
    calcular_parcelas,
    aplicar_multa_cancelamento
)

# ====================================================================
# ÁREA DO ALUNO
# ====================================================================

def test_calcular_desconto():
    # Teste Correto: 10% de desconto sobre 100 deve ser 90
    assert calcular_desconto(100, 10) == 90
    # Teste Correto: 50% de desconto sobre 200 deve ser 100
    assert calcular_desconto(200, 50) == 100

def test_calcular_desconto_edge_cases():
    # Testar desconto de 0%
    assert calcular_desconto(100, 0) == 100
    # Testar desconto de 100%
    assert calcular_desconto(100, 100) == 0

def test_aplicar_juros_atraso():
    # ERRO PROPOSITAL: A expectativa matemática está errada.
    # A função original aplica juros simples de 1% ao dia.
    # Para 100 reais, 5 dias de atraso seriam 105 reais (100 + 100 * 0.01 * 5).
    # O teste abaixo está esperando 150, como se fosse 10% ao dia.
    # ATIVIDADE: Corrigir a expectativa matemática abaixo para o valor correto (1% ao dia).
    assert aplicar_juros_atraso(100, 5) == 105
    assert aplicar_juros_atraso(100, 0) == 100

def test_aplicar_juros_atraso_edge_cases():
    # Testar valores negativos (dias negativos = desconto)
    assert aplicar_juros_atraso(100, -5) == 95
    # Testar valor zero
    assert aplicar_juros_atraso(0, 10) == 0

# TODO: Implementar Testes: Crie os testes para a função validar_metodo_pagamento
# Implemente nela pelo menos 2 asserções (assert):
# 1 - Teste um método de pagamento aceito.
# 2 - Teste um método rejeitado.

def test_validar_metodo_pagamento():
    assert validar_metodo_pagamento("pix") == True
    assert validar_metodo_pagamento("cartao_credito") == True
    
    assert validar_metodo_pagamento("cheque") == False
    assert validar_metodo_pagamento("bitcoin") == False

def test_validar_metodo_pagamento_case_sensitive():
    # Testar maiúsculas/minúsculas
    assert validar_metodo_pagamento("PIX") == True
    assert validar_metodo_pagamento("Pix") == True
    assert validar_metodo_pagamento("CARTAO_CREDITO") == True

# TODO: Implementar Testes: Crie os testes para a função processar_reembolso
# Implemente nela pelo menos 2 asserções (assert):
# 1 - Teste um reembolso válido (valor reembolsado menor ou igual ao pago).
# 2 - Teste um caso de erro, simulando uma regra de negócio que restringe o reembolso (deve retornar -1).


def test_processar_reembolso():

    assert processar_reembolso(100,50) == 50
    assert processar_reembolso(200,200) == 0

    assert processar_reembolso(100,150) == -1
    assert processar_reembolso(50,60) == -1

def test_validar_valor_pagamento():
    assert validar_valor_pagamento(100) == True
    assert validar_valor_pagamento(0) == False
    assert validar_valor_pagamento(-50) == False

def test_calcular_parcelas():
    assert calcular_parcelas(100, 2) == 50
    assert calcular_parcelas(100, 4) == 25
    assert calcular_parcelas(100, 0) == -1
    assert calcular_parcelas(100, -1) == -1

def test_aplicar_multa_cancelamento():
    assert aplicar_multa_cancelamento(100) == 110
    assert aplicar_multa_cancelamento(200, 5) == 210
    assert aplicar_multa_cancelamento(50, 20) == 60

def test_fluxo_completo_pagamento():
    # Testar fluxo completo: desconto + validação + juros
    valor_original = 100
    valor_com_desconto = calcular_desconto(valor_original, 10)
    assert valor_com_desconto == 90
    
    # Aplicar juros se houver atraso
    valor_final = aplicar_juros_atraso(valor_com_desconto, 5)
    assert valor_final == 94.5
    
    # Validar método de pagamento
    assert validar_metodo_pagamento("pix") == True
    
    # Processar reembolso se necessário
    saldo = processar_reembolso(valor_final, 20)
    assert saldo == 74.5