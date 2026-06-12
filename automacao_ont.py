from playwright.sync_api import sync_playwright
import time

def resetar_ont():
    try:
      with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()
        
        # 1. Login
        page.goto("http://192.168.1.1")
        page.fill('input[name="Frm_Username"]', 'login_provedor')
        page.fill('input[name="Frm_Password"]', 'senha_provedor')
        page.click('input[type="submit"]')
        
        page.wait_for_load_state("networkidle")
        time.sleep(5)
        
        # 2. Navegação para a coleta de potencia de sinal e numero de serial
        page.click('#internet')
        potencia = page.text_content('#RxPower')
        page.click('#ponInfo')
        page.click('#ponSn')
        time.sleep(1)
        serial_number = page.input_value('#Sn')
        print(f"Potência de sinal: {potencia}")  
        print(f"Serial Number: {serial_number}") 

        # 3. Navegação para a coleta das portas LANs 
        page.click('#localnet')
        lan1 = page.text_content('#Status\\:0')
        lan2 = page.text_content('#Status\\:1')
        lan3 = page.text_content('#Status\\:2')
        lan4  = page.text_content('#Status\\:3')  
        print(f"Status LAN1: {lan1}")
        print(f"Status LAN2: {lan2}")
        print(f"Status LAN3: {lan3}")
        print(f"Status LAN4: {lan4}")

        # 4. Navegação Para o menu de reset (Gerência & Diagnóstico > Administração de sistema > Gerenciamento de redefinição de fábrica)
        print("Navegando pelos menus...")
        page.click('#mgrAndDiag')
        page.click('#devMgr')
        page.click('#ResetManagBar')
        
        # 5. Clique no Reset (abre o pop-up)
        print("Clicando em Restauração de fábrica...")
        page.click('#Btn_reset')
        
        # 6. Confirmação
        print("Confirmando no pop-up...")
        page.wait_for_selector('text="OK"')
        page.click('text="OK"')
        
        print(f""" ======================= ZTE  SERIAL {serial_number} RESTAURADO COM SUCESSO =================================""")
        
        time.sleep(5)
        browser.close()

    except Exception as e:
        print(f"Erro: {e}")

def main():
    while True:
        resetar_ont()
        
        # Pergunta ao usuário
        resposta = input("\nDeseja testar outra ONT? (Y/N): ").strip().upper()
        
        if resposta == 'N':
            print("Encerrando script...")
            break
        elif resposta != 'Y':
            print("Resposta inválida! Digite Y ou N.")

if __name__ == "__main__":
    main()
