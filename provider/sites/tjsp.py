import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.edge.options import Options


class TJSP:
    def realiza_consulta(self, filtro, documento):
        service = Service(executable_path=os.getenv('EXECUTAVEL')+"msedgedriver.exe")
        options = Options()
        options.add_argument("-headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Edge(service=service, options=options)
        browser.get(os.getenv('URL_TJSP'))

        if (filtro in (0,1,3)):
            value = 'DOCPARTE'
        elif (filtro == 2):
            value = 'NMPARTE'
        else:
            return False

        try:
            select_el = browser.find_element('xpath','//*[@id="cbPesquisa"]')
            select_ob = Select(select_el)
            select_ob.select_by_value(value)
            if value == "NMPARTE":
                browser.find_element('xpath','//*[@id="pesquisarPorNomeCompleto"]').click()
            browser.find_element('xpath',f'//*[@id="campo_{value}"]').send_keys(documento)
            browser.find_element('xpath','//*[@id="botaoConsultarProcessos"]').click()

        except Exception as e:
            print(f"Erro ao acessar site: {e}")
            
        return browser