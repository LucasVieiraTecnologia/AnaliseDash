import flet as ft

def main(page: ft.Page):
    page.title = "Dash Skin Analyzer"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 600
    page.padding = 20
    # Cores inspiradas na Dash
    page.bgcolor = "#0f111a" 

    # Componentes
    preco_compra = ft.TextField(
        label="Preço de Compra (R$)", 
        value="5.07", 
        border_color="#3f51b5",
        focused_border_color="#7986cb"
    )
    preco_segunda = ft.TextField(
        label="Preço da 2ª mais barata (R$)", 
        value="5.50",
        border_color="#3f51b5"
    )
    taxa_plataforma = ft.TextField(
        label="Taxa da Dash (%)", 
        value="10",
        border_color="#3f51b5"
    )
    
    res_container = ft.Container(
        content=ft.Column([
            resultado_texto := ft.Text(size=22, weight="bold"),
            detalhes_texto := ft.Text(size=16, color="#b0b0b0")
        ]),
        padding=10,
        border_radius=10,
        visible=False
    )

    def calcular(e):
        try:
            p_compra = float(preco_compra.value.replace(",", "."))
            p_segunda = float(preco_segunda.value.replace(",", "."))
            taxa = float(taxa_plataforma.value) / 100
            
            venda_alvo = p_segunda - 0.01
            recebido_liquido = venda_alvo * (1 - taxa)
            lucro = recebido_liquido - p_compra
            roi = (lucro / p_compra) * 100

            res_container.visible = True
            if lucro > 0:
                resultado_texto.value = f"✅ LUCRO: R$ {lucro:.2f}"
                resultado_texto.color = ft.Colors.GREEN_ACCENT_400
                res_container.bgcolor = "#1a2e1a"
            else:
                resultado_texto.value = f"❌ PREJUÍZO: R$ {abs(lucro):.2f}"
                resultado_texto.color = ft.Colors.RED_ACCENT_400
                res_container.bgcolor = "#2e1a1a"
            
            detalhes_texto.value = (
                f"Venda Sugerida: R$ {venda_alvo:.2f}\n"
                f"Taxa (10%): R$ {venda_alvo * taxa:.2f}\n"
                f"Retorno (ROI): {roi:.2f}%"
            )
        except:
            resultado_texto.value = "Erro: Use números válidos"
            resultado_texto.color = ft.Colors.ORANGE_400
            res_container.visible = True
        
        page.update()

    # Usando ft.FilledButton que é o padrão novo
    btn_calcular = ft.FilledButton(
        "Analisar Skin", 
        on_click=calcular, 
        width=400,
        style=ft.ButtonStyle(bgcolor="#5c6bc0")
    )

    page.add(
        ft.Text("Dash Analyzer", size=28, weight="bold", color="#ffffff"),
        ft.Text("Calculadora de Arbitragem", size=14, color="#7986cb"),
        ft.Divider(height=20, color="transparent"),
        preco_compra,
        preco_segunda,
        taxa_plataforma,
        ft.Divider(height=10, color="transparent"),
        btn_calcular,
        ft.Divider(height=10, color="transparent"),
        res_container
    )

# Corrigido para a versão nova do Flet
if __name__ == "__main__":
    ft.run(main)