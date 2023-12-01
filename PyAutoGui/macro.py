import win32com.client

def executar_macro():
    # Criar uma instância do Excel
    excel = win32com.client.Dispatch("Excel.Application")

    # Abrir ou ativar o arquivo Excel desejado
    workbook_path = r"C:\Caminho\Para\Seu\Arquivo.xlsx"
    workbook = excel.Workbooks.Open(workbook_path)

    try:
        # Ativar a planilha desejada (opcional)
        sheet_name = "Planilha1"
        worksheet = workbook.Sheets(sheet_name)
        worksheet.Activate()

        # Executar a macro
        macro_name = "SuaMacro"
        excel.Run(macro_name)
    
    except Exception as e:
        print(f"Erro ao executar a macro: {e}")
    
    finally:
        # Fechar o arquivo Excel sem salvar as alterações
        workbook.Close(False)
        # Encerrar a instância do Excel
        excel.Quit()

if __name__ == "__main__":
    executar_macro()
