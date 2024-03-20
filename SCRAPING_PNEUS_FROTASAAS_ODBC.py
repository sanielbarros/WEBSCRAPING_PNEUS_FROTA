# #### Para que a automação execute automático todos os dias em um determinado horário, agende uma tarefa no agendador de tarefas do Windows

# #### Importar bibliotecas necessárias


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import date, timedelta
import pyodbc
import requests


# #### Abrir navegador e acessar site


chromer_options = Options()
chromer_options.add_argument("--headless")

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico, options = chromer_options)
endereco = r'https://www.frotasaas.com.br/frotaweb/'
navegador.get(endereco)


def main():
    acessar_sistema()
    lista_sql_query = [
        (f"INSERT INTO logistica.frotasaas_pneus_controle_atualizacao_sulcos (cd_empresa, nm_empresa, cd_filial, "
         "nm_filial, cd_pneu, dh_medicao, cd_veiculo, placa, cd_posicao, dh_instala, sulco1, sulco2, sulco3, sulco4, sulco5, "
         "data_atualizacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", "substituir", "frotasaas_pneus_controle_atualizacao_sulcos"),
        
        (f"INSERT INTO logistica.frotasaas_controle_pneus_em_uso (cd_empresa, cd_filial, cd_ccusto, cd_pneu, cd_modelo, "
         "nr_vida, qt_sulco1, qt_sulco2, qt_sulco3, qt_sulco4, qt_sulco5, vl_custo, situacao, lugar, bl_baixa, "
         "cd_veiculo, nm_modelo, dh_evento, cd_posicao, cd_destino, cd_evento, bl_saida, bl_recauch, bl_compra, "
         "bl_inst, bl_desinst, bl_trent, nm_filial, cd_regiona, nm_empresa, cd_dimensa, cd_desenho, cd_fornec, "
         "cd_vei_loc, qt_hr_even, qt_km_even, km_tperco, hr_tperco, nm_regiona, nm_desenho, nm_ccusto, placa, "
         "nm_fornec, nm_dimensa, data_atualizacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
         "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", "substituir", "frotasaas_controle_pneus_em_uso"),
        
        (f"INSERT INTO logistica.frotasaas_controle_pneus_por_veiculo (cd_veiculo, placa, cd_posicao, qt_hr_even, "
         "qt_km_even, cd_modveic, aa_fabric, aa_modelo, qt_hr_med, qt_km_med, bl_tracao, bl_medprop, cd_cavalo, nm_modveic, "
         "nr_vida, cd_modelo, dot, tt_km_vida, tt_hr_vida, tt_km_pneu, km_na_vida, tt_hr_pneu, hr_na_vida, qt_sulco_i, "
         "km_im_pri, km_re_pri, hr_im_pri, hr_re_pri, km_im_seg, km_re_seg, hr_im_seg, hr_re_seg, km_im_ter, km_re_ter, "
         "hr_im_ter, hr_re_ter, km_im_qua, km_re_qua, hr_im_qua, hr_re_qua, km_im_qui, km_re_qui, hr_im_qui, hr_re_qui, "
         "km_im_sex, km_re_sex, hr_im_sex, hr_re_sex, km_im_set, km_re_set, hr_im_set, hr_re_set, qt_libras, qt_sulco1, "
         "qt_sulco2, qt_sulco3, qt_sulco4, qt_sulco5, cd_filial, nm_filial, cd_regiona, cd_empresa, qt_hr_med1, qt_km_med1,"
         "cd_pneu, nm_modelo, cd_fornec, cd_dimensa, qt_sulco_c, qt_km_perc, qt_hr_perc, sulco_refo, qt_km_rod, qt_hr_rod, "
         "km_vida, hr_vida, nm_empresa, nm_dimensa, nm_fornec, nm_regiona, data_atualizacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, "
         "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
         "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
         "substituir", "frotasaas_controle_pneus_por_veiculo"),
        
        (f"INSERT INTO logistica.frotasaas_relacao_calibragem (cd_empresa, cd_pneu, dh_evento, cd_posicao, qt_km, cd_motdesi, "
         "cd_tprecau, cd_desenho, libras, libras_ini, cd_evento, qt_hr, cd_tpborra, cd_destino, cd_motsuca, nm_modelo, "
         "nr_vida, cd_filial, cd_veiculo, placa, nm_fabrica, nm_dimensa, nm_empresa, nm_filial, nm_modveic, data_atualizacao) " 
         "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", "incrementar", "frotasaas_relacao_calibragem"),
        
        (f"INSERT INTO logistica.frotasaas_pneus_sucateados_por_modelo (qt_km_pri, qt_hr_pri, qt_km_seg, qt_hr_seg, qt_km_ter, "
         "qt_hr_ter, qt_km_qua, qt_hr_qua, qt_km_qui, qt_hr_qui, qt_km_sex, qt_hr_sex, qt_km_set, qt_hr_set, nm_desenho, "
         "cd_pneu, nm_fornec, dh_evento, cd_modelo, vl_custo, nm_fabrica, nm_motsuca, nm_dimensa, nm_filial, nm_empresa, "
         "cd_filial, cd_empresa, cd_veiculo, data_atualizacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
         "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", "substituir", "frotasaas_pneus_sucateados_por_modelo"),
        
        (f"INSERT INTO logistica.frotasaas_pneus_que_retornaram_da_recauchutadora (cd_empresa, nm_empresa, cd_filial, nm_filial, "
         "cd_fornec, nm_fornec, cd_pneu, nm_modelo, cd_regiona, nm_regiona, vl_cons, vl_reform, qt_cons, qt_ref, data_atualizacao, "
         "data_retorno_recauchutadora) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", "incrementar", "frotasaas_pneus_que_retornaram_da_recauchutadora")
    ]
    
    for i, query in enumerate(lista_sql_query):
        try:
            if i == 0:
                relatorio_txt = acessar_rel_controle_atualizacao_sulcos()
            elif i == 1:
                relatorio_txt = acessar_rel_controle_pneus_em_uso()
            elif i == 2:
                relatorio_txt = acessar_rel_controle_pneus_por_veiculo()
            elif i == 3:
                relatorio_txt = acessar_rel_calibragem()
            elif i == 4:
                relatorio_txt = acessar_rel_pneus_sucateados_por_modelo()
            elif i == 5:
                relatorio_txt = acessar_rel_pneus_que_retornaram_da_recauchutadora()
        except NoSuchElementException as e:
            msg = "Relatório: {}.\nNão retornou linhas.".format(lista_sql_query[i][2])
            print("{}. Msg except:".format(msg, e))
            enviar_menssagem_telegram(msg)
            continue
        else:
            tratar_salvar_relatorio(relatorio_txt, lista_sql_query[i][0], lista_sql_query[i][1], lista_sql_query[i][2]) 
    navegador.quit()


# #### Acessando o sistema


def acessar_sistema():    
    navegador.find_element(By.ID, 'txtcd_empresa').send_keys('SEU_CODIGO_EMPRESA', Keys.TAB) # SUBSTITUA PELO SEU CÓDIGO DE EMPRESA NO SISTEMA FROTASAAS
    time.sleep(1)
    navegador.find_element(By.ID, 'txtcd_usuario').send_keys('SEU_USUARIO')  # SUBSTITUA PELO SEU USUÁRIO
    navegador.find_element(By.ID, 'txtcd_filial').send_keys('SUA_FILIAL') # SUBSTITUA PELA SUA FILIAL
    navegador.find_element(By.ID, 'pwdsenha').send_keys('SUA_SENHA') # SUBSTITUA PELA SEU SENHA
    navegador.find_element(By.NAME, 'btnentrar').click()
    time.sleep(2)


# #### Acessar e gerar relatórios


#script = "window.parent.parent.parent.chamaTela('../telas/TL15533.asp','Controle de Atualização de Sulcos')"
#navegador.execute_script(script)

def acessar_rel_controle_atualizacao_sulcos():
    navegador.get(endereco + r'/telas/TL15533.asp')
    data_hoje = date.today()
    navegador.find_element(By.ID, 'txtdt_limite').send_keys(data_hoje.strftime('%d/%m/%Y'))
    navegador.find_element(By.ID, 'txtfilial_ini').send_keys(Keys.BACK_SPACE,'88')
    navegador.find_element(By.ID, 'txtfilial_fim').send_keys(Keys.BACK_SPACE,'333')
    time.sleep(1)
    lista_radio = navegador.find_elements(By.ID, 'radSaida')

    for radio in lista_radio:
        if int(radio.get_attribute('tabindex')) == 19:
            radio.click()

    navegador.find_element(By.ID, 'btngerar').click()
    janelas = navegador.window_handles
    navegador.switch_to.window(janelas[-1])
    iframe_texto = navegador.find_element(By.TAG_NAME, 'iframe')
    navegador.switch_to.frame(iframe_texto)
    relatorio_txt = navegador.find_element(By.XPATH, '/html/body/pre').text
    return relatorio_txt
    
def acessar_rel_controle_pneus_em_uso():
    navegador.get(endereco + r'/telas/TL15510.asp')
    dropdown_pneu_selecionado = Select(navegador.find_element(By.ID, 'selescolha'))
    dropdown_pneu_selecionado.select_by_index(5)
    navegador.find_element(By.ID, 'txtfilial_ini').send_keys(Keys.BACK_SPACE,'88')
    navegador.find_element(By.ID, 'txtfilial_fim').send_keys(Keys.BACK_SPACE,'333')
    lista_radio = navegador.find_elements(By.ID, 'radSaida')
    
    for radio in lista_radio:
        if int(radio.get_attribute('tabindex'))== 53:
               radio.click()
                
    navegador.find_element(By.ID, 'btngerar').click()
    janelas = navegador.window_handles
    navegador.switch_to.window(janelas[-1])
    iframe_texto = navegador.find_element(By.TAG_NAME, 'iframe')
    navegador.switch_to.frame(iframe_texto)
    relatorio_txt = navegador.find_element(By.XPATH, '/html/body/pre').text
    return relatorio_txt
    
def acessar_rel_controle_pneus_por_veiculo():
    navegador.get(endereco + r'/telas/TL15521.asp')
    navegador.find_element(By.ID, 'chkbl_projecao').click()
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
    
def acessar_rel_calibragem():
    navegador.get(endereco + r'/telas/TL15531.asp')
    data_ontem = date.today() - timedelta(days=1)
    navegador.find_element(By.ID, 'txtdt_ini').send_keys(data_ontem.strftime('%d/%m/%Y'))
    navegador.find_element(By.ID, 'txtdt_fim').send_keys(data_ontem.strftime('%d/%m/%Y'))
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

def acessar_rel_pneus_sucateados_por_modelo():
    navegador.get(endereco + r'/telas/TL15544.asp')
    navegador.find_element(By.ID, 'chkquebrafil').click()
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

def acessar_rel_pneus_que_retornaram_da_recauchutadora():
    navegador.get(endereco + r'/telas/TL15542.asp')
    data_ontem = date.today() - timedelta(days=1)
    navegador.find_element(By.ID, 'txtdt_ini').send_keys(data_ontem.strftime('%d/%m/%Y'))
    navegador.find_element(By.ID, 'txtdt_fim').send_keys(data_ontem.strftime('%d/%m/%Y'))
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
    conexao = pyodbc.connect('DSN=' + 'postgres_local') # SUBSTITUA 'postgres_local' pelo nome da sua fonte de dados no ODBC. A configuração do banco é feita no ODBC!
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
    
def tratar_salvar_relatorio(relatorio_txt, sql_query, metodo_atualizacao, nome_tabela):
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
            data_ontem = data_hoje - timedelta(days=1)
            item.append(data_ontem.strftime('%d/%m/%Y'))
    print(lista_delimitada)
    
    try:
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
        enviar_menssagem_telegram(msg)
        fechar_conexao(conexao, cursor)
        fechar_janela_aberta()        


# #### Enviar logs para bot no Telegram


def enviar_menssagem_telegram(msg):
    token = 'SEU_TOKEN' # SEU TOKEN DO TELEGRAM
    chat_id = 'SEU CHAT_ID' # SEU ID DO CHAT TELEGRAM
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)




if __name__ == "__main__":
    main()

