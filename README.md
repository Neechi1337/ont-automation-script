# ONT Automation Tool 🚀

Script em Python desenvolvido para automatizar e otimizar o fluxo de teste, verificação e reset de ONTs em laboratórios de manutenção de provedores de internet (ISPs).

## 🛠️ Funcionalidades
* Interface interativa via terminal.
* Automação de comandos de verificação/configuração de equipamentos de rede.
* Tratamento de exceções para evitar travamentos durante testes em lote.

## 📐 Cenário de Aplicação e Topologia de Rede
O script foi desenvolvido e validado especificamente para atuar com o modelo **ZTE F6600L**. Para garantir a eficiência dos testes em lote e a integridade da rede do laboratório, o ambiente foi estruturado da seguinte forma:

* **Hardware Alvo:** Homologado para **ZTE F6600L** (firmware padrão de operadora/ISP).
* **Conexão Física:** O sistema é conectado simultaneamente a **4 cabos de rede** (utilizando uma porta para cada interface da ONT sob teste).
* **Prevenção de Loop (Anti-Loop):** Para evitar tempestades de broadcast (broadcast storm) ou loops de camada 2 ao conectar todas as portas de uma vez, foi integrada uma **RouterBoard (RB)** no fluxo.
* **Isolamento por Sub-redes:** A RB foi configurada para segmentar o tráfego de cada uma das portas em **sub-redes e VLANs distintas**, garantindo que as interfaces se comuniquem com o script de automação de forma isolada e segura.
