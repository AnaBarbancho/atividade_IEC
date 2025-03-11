from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configura as opções do Chrome para ignorar erros de SSL
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# Inicia o ChromeDriver com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)

# Acessa o site
driver.get("https://exemplo.com")

# Aguarda até que o título da página seja carregado
driver.implicitly_wait(10)

# Verifica se o título contém a palavra "exemplo"
assert "exemplo.com" in driver.title  # Ajuste conforme o título real da página

# Fecha o navegador
driver.quit()
