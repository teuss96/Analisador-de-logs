import re
import matplotlib.pyplot as plt
import pandas as pd

def analisar_logs(arquivo_log):
    tipos_log = {'ERROR': 0, 'WARNING': 0, 'INFO': 0, 'DEBUG': 0}

    try:
        with open(arquivo_log, 'r') as file:
            for linha in file:
    
                if 'ERROR' in linha:
                    tipos_log['ERROR'] += 1
                elif 'WARNING' in linha:
                    tipos_log['WARNING'] += 1
                elif 'INFO' in linha:
                    tipos_log['INFO'] += 1
                elif 'DEBUG' in linha:
                    tipos_log['DEBUG'] += 1
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_log}' não encontrado!")
        return None

    return tipos_log

def visualizar_logs(tipos_log):
    if tipos_log is None:
        return
    
    df = pd.DataFrame(list(tipos_log.items()), columns=['Tipo', 'Quantidade'])

    plt.figure(figsize=(8, 5))
    plt.bar(df['Tipo'], df['Quantidade'], color=['red', 'orange', 'blue', 'green'])
    plt.xlabel('Tipo de Log')
    plt.ylabel('Quantidade')
    plt.title('Distribuição de Tipos de Log')
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.pie(df['Quantidade'], labels=df['Tipo'], autopct='%1.1f%%', colors=['red', 'orange', 'blue', 'green'], startangle=90)
    plt.title('Distribuição de Tipos de Log (Pizza)')
    plt.axis('equal')  
    plt.show()

def main():
    arquivo_log = 'logs.txt' 

    tipos_log = analisar_logs(arquivo_log)

    if tipos_log:
        visualizar_logs(tipos_log)

if __name__ == '__main__':
    main()
