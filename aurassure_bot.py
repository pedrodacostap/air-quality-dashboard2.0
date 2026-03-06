import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from playwright.sync_api import sync_playwright
import os

def gerar_relatorio(mes, ano):

    if not os.path.exists("dados"):
        os.makedirs("dados")

    arquivo = f"dados/relatorio_{mes}_{ano}.csv"

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://app.aurassure.com")

        # exemplo de dados
        with open(arquivo, "w") as f:
            f.write("cidade,pm25,lat,lon\n")
            f.write("Altamira,12,-3.2,-52.2\n")
            f.write("Belem,18,-1.4,-48.5\n")

        browser.close()

    return arquivo