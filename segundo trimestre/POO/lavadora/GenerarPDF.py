from fpdf import FPDF
from datetime import datetime


class GenerarPDF:

    @staticmethod
    def generar(reportes, clientes, total_dia):

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "REPORTE DIARIO SMART LAVA", ln=True, align="C")

        fecha = datetime.now().strftime("%Y-%m-%d")
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Fecha: {fecha}", ln=True)
        pdf.cell(0, 8, f"Clientes atendidos: {clientes}", ln=True)
        pdf.cell(0, 8, f"Total del dia: ${total_dia:,.0f}", ln=True)

        pdf.ln(5)

        for r in reportes:

            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, "----------------------------------------", ln=True)

            pdf.set_font("Arial", "", 11)

            pdf.cell(0, 8, f"Cliente: {r['cliente']}", ln=True)
            pdf.cell(0, 8, f"Kilos: {r['kilos']}", ln=True)
            pdf.cell(0, 8, f"Tipo prenda: {r['tipo']}", ln=True)
            pdf.cell(0, 8, f"Estrato: {r['estrato']}", ln=True)

            pdf.cell(0, 8, f"Costo base: ${r['costo_base']:,.0f}", ln=True)
            pdf.cell(0, 8, f"Aumento: ${r['aumento']:,.0f}", ln=True)
            pdf.cell(0, 8, f"IVA: ${r['iva']:,.0f}", ln=True)

            pdf.cell(0, 8, f"Consumo energia (kWh): {r['consumo']:.3f}", ln=True)
            pdf.cell(0, 8, f"Costo energia: ${r['costo_energia']:,.0f}", ln=True)

            pdf.cell(0, 8, f"Total pagado: ${r['total']:,.0f}", ln=True)

            pdf.ln(5)

        pdf.output("ReporteSmartLava.pdf")

        print("\n📄 PDF generado: ReporteSmartLava.pdf")