import streamlit as st
import re

st.header("Calculadora", divider="gray")

def evaluate_expression(value):
  if re.match(r'^[0-9+\-*/(). ]+$', value):
    try:
      result = eval(value)
      return result
    except Exception as e:
      return f"Erro na expressão: {str(e)}"
  else:
    return 'erro'

expression = st.text_input("Entre com a Expressão Matemática")

if expression:
  result = evaluate_expression(expression)

  if (result == 'erro'):
    st.write("Expressão matemática inválida!")
  else:
    st.write("Resultado: ", result, ".")
