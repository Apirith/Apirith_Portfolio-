from pathlib import Path

pdf = (
    b"%PDF-1.4\n"
    b"1 0 obj\n"
    b"<< /Type /Catalog /Pages 2 0 R >>\n"
    b"endobj\n"
    b"2 0 obj\n"
    b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>\n"
    b"endobj\n"
    b"3 0 obj\n"
    b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 200] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>\n"
    b"endobj\n"
    b"4 0 obj\n"
    b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\n"
    b"endobj\n"
    b"5 0 obj\n"
    b"<< /Length 50 >>\n"
    b"stream\n"
    b"BT\n/F1 18 Tf\n50 100 Td\n(Apirith Sothea - placeholder, replace with SolidWorks PDF export) Tj\nET\n"
    b"endstream\n"
    b"endobj\n"
    b"xref\n"
    b"0 6\n"
    b"0000000000 65535 f \n"
    b"0000000010 00000 n \n"
    b"0000000062 00000 n \n"
    b"0000000127 00000 n \n"
    b"0000000244 00000 n \n"
    b"0000000381 00000 n \n"
    b"trailer\n"
    b"<< /Root 1 0 R /Size 6 >>\n"
    b"startxref\n"
    b"0\n"
    b"%%EOF\n"
)

output = Path("assets/cad/fallout-smartwatch/drawing.pdf")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_bytes(pdf)
print(f"Created {output}")
