# #### Essa automação serve para corrigir dias que a automação "SCRAPING_PNEUS_FROTSAAS_ODBC" por algum motivo não executou automático (apenas tabelas incrementais).

# #### Importar bibliotecas necessárias

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
from datetime import date, timedelta, datetime
import pyodbc


# #### Abrir navegador e acessar site


chromer_options = Options()
chromer_options.add_argument("--headless")

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)
endereco = r'https://www.frotasaas.com.br/frotaweb/'
navegador.get(endereco)


def main():
    relatorio_ajuste = int(input('Qual relatório deseja ajustar?\n1 - Relação Calibragem\n2 - Pneus retornados da recauchutadora'))
    
    acessar_sistema()
    lista_sql_query = [
        (f"INSERT INTO logistica.frotasaas_relacao_calibragem (cd_empresa, cd_pneu, dh_evento, cd_posicao, qt_km, cd_motdesi, "
         "cd_tprecau, cd_desenho, libras, libras_ini, cd_evento, qt_hr, cd_tpborra, cd_destino, cd_motsuca, nm_modelo, "
         "nr_vida, cd_filial, cd_veiculo, placa, nm_fabrica, nm_dimensa, nm_empresa, nm_filial, nm_modveic, data_atualizacao) " 
         "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", "incrementar", "frotasaas_relacao_calibragem"),
        
        (f"INSERT INTO logistica.frotasaas_pneus_que_retornaram_da_recauchutadora (cd_empresa, nm_empresa, cd_filial, nm_filial, "
         "cd_fornec, nm_fornec, cd_pneu, nm_modelo, cd_regiona, nm_regiona, vl_cons, vl_reform, qt_cons, qt_ref, data_atualizacao, "
         "data_retorno_recauchutadora) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", "incrementar", "frotasaas_pneus_que_retornaram_da_recauchutadora")
    ]
    
    if relatorio_ajuste == 1:
        print("Acessando relatório de calibragem...")
        relatorio_txt = acessar_rel_calibragem()
        tratar_salvar_relatorio(relatorio_txt, lista_sql_query[0][0], lista_sql_query[0][1], lista_sql_query[0][2], "")
    elif relatorio_ajuste == 2:
        print("Acessando relatório de pneus que retornaram da recauchutadora")
        data_inicio_filtro = datetime.strptime(input('Qual a data do filtro para iniciar o loop? No formato 2023-11-20'),'%Y-%m-%d')
        dias_a_frente = int(input('Quantas vezes deve executar o loop a partir da data de início do filtro?'))
        print('Será loopado até {}'.format(data_inicio_filtro + timedelta(days=dias_a_frente)))
        
        for i in range(dias_a_frente):
            data_filtro = data_inicio_filtro + timedelta(days=i)
            print('Dia {}'.format(datetime.fromisoformat(str(data_filtro)).date()))
            data_filtro = datetime.fromisoformat(str(data_filtro)).date()
            try:
                relatorio_txt = acessar_rel_pneus_que_retornaram_da_recauchutadora(data_filtro)
            except Exception as e:
                print('Sem resultado. Não foi encontrado elemento para o seletor!')
                continue
            else:
                tratar_salvar_relatorio(relatorio_txt, lista_sql_query[1][0], lista_sql_query[1][1], lista_sql_query[1][2], data_filtro)

    else:
        navegador.quit()


def acessar_sistema():    
    navegador.find_element(By.ID, 'txtcd_empresa').send_keys('SEU_CODIGO_EMPRESA', Keys.TAB) # SUBSTITUA PELO SEU CÓDIGO DE EMPRESA NO SISTEMA FROTASAAS
    time.sleep(1)
    navegador.find_element(By.ID, 'txtcd_usuario').send_keys('SEU_USUARIO')  # SUBSTITUA PELO SEU USUÁRIO
    navegador.find_element(By.ID, 'txtcd_filial').send_keys('SUA_FILIAL') # SUBSTITUA PELA SUA FILIAL
    navegador.find_element(By.ID, 'pwdsenha').send_keys('SUA_SENHA') # SUBSTITUA PELA SEU SENHA
    navegador.find_element(By.NAME, 'btnentrar').click()
    time.sleep(2)


# #### Acessar e gerar relatórios


def acessar_rel_calibragem():
    navegador.get(endereco + r'/telas/TL15531.asp')
    data_inicio = input('Qual a data de início do filtro? No formato 01/01/2000.')
    data_fim = input('Qual a data do final do filtro? No formato 01/01/2000.')
    data_hoje = date.today()
    navegador.find_element(By.ID, 'txtdt_ini').send_keys(data_inicio)
    navegador.find_element(By.ID, 'txtdt_fim').send_keys(data_fim)
    navegador.find_element(By.ID, 'txtfilial_ini').send_keys(Keys.BACK_SPACE,'88')
    navegador.find_element(By.ID, 'txtfilial_fim').send_keys(Keys.BACK_SPACE,'333')
    lista_radio = navegador.find_elements(By.ID, 'radSaida')
    
    for radio in lista_radio:
        if int(radio.get_attribute('tabindex'))== 19:
               radio.click()
                
    navegador.find_element(By.ID, 'btngerar').click()
    janelas = navegador.window_handles
    navegador.switch_to.window(janelas[-1])
    iframe_texto = navegador.find_element(By.TAG_NAME, 'iframe')
    navegador.switch_to.frame(iframe_texto)
    relatorio_txt = navegador.find_element(By.XPATH, '/html/body/pre').text
    return relatorio_txt

def acessar_rel_pneus_que_retornaram_da_recauchutadora(data_filtro):
    navegador.get(endereco + r'/telas/TL15542.asp')
    navegador.find_element(By.ID, 'txtdt_ini').send_keys(data_filtro.strftime('%d/%m/%Y'))
    navegador.find_element(By.ID, 'txtdt_fim').send_keys(data_filtro.strftime('%d/%m/%Y'))
    navegador.find_element(By.ID, 'txtfilial_ini').send_keys(Keys.BACK_SPACE,'88')
    navegador.find_element(By.ID, 'txtfilial_fim').send_keys(Keys.BACK_SPACE,'333')
    lista_radio = navegador.find_elements(By.ID, 'radSaida')
    
    for radio in lista_radio:
        if int(radio.get_attribute('tabindex'))== 19:
               radio.click()
                
    navegador.find_element(By.ID, 'btngerar').click()
    janelas = navegador.window_handles
    navegador.switch_to.window(janelas[-1])
    iframe_texto = navegador.find_element(By.TAG_NAME, 'iframe')
    navegador.switch_to.frame(iframe_texto)
    relatorio_txt = navegador.find_element(By.XPATH, '/html/body/pre').text
    return relatorio_txt


# #### Tratando dados e gravando em banco postgress via ODBC


def abrir_conexao():
    conexao = pyodbc.connect('DSN=' + 'postgres_local')
    return conexao
    
def fechar_conexao(conexao, cursor):
    cursor.close()
    conexao.close()
    
def fechar_janela_aberta():
    # Após interagir com a nova aba/janela, ela é fechada
    navegador.close()
    # Volta para a janela original
    janelas = navegador.window_handles
    navegador.switch_to.window(janelas[0])
    
def tratar_salvar_relatorio(relatorio_txt, sql_query, metodo_atualizacao, nome_tabela, data_filtro):
    print("Tratando dados...")
    lista_delimitada = []
    for i, linha in enumerate(relatorio_txt.splitlines()):
        linha_delimitada = []
        for delimitacao in linha.split(';'):
            delimitacao = delimitacao.replace('"','').replace(',','.')
            linha_delimitada.append(delimitacao)
        lista_delimitada.append(linha_delimitada)
    data_hoje = date.today()
    for item in lista_delimitada:
        item.append(data_hoje.strftime('%d/%m/%Y'))
        if nome_tabela == "frotasaas_pneus_que_retornaram_da_recauchutadora":
            #data_ontem = data_hoje - timedelta(days=1)
            item.append(data_filtro.strftime('%d/%m/%Y'))
    print(lista_delimitada)
    
    try:
        print("Enviando dados para o banco...")
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        if metodo_atualizacao == 'substituir':
            cursor.execute("DELETE FROM logistica." + nome_tabela)
            conexao.commit()
            cursor.executemany(sql_query, lista_delimitada)
            conexao.commit()
        elif metodo_atualizacao == 'incrementar':
            cursor.executemany(sql_query, lista_delimitada)
            conexao.commit()
        else:
            print("Erro na identificação o método de atualização.")
        msg = "Relatório: {}.\nProcessado {} linhas.\nAtualização (tipo): {}.".format(nome_tabela, i+1, metodo_atualizacao)
    except Exception as e:
        msg = "Relatório: {}.\nFalha na comunicação com o banco! Erro: {}".format(nome_tabela, e)
    finally:
        print(msg)
        fechar_conexao(conexao, cursor)
        fechar_janela_aberta()




if __name__ == "__main__":
    main()




