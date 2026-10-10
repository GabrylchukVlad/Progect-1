import qrcode

def run_qrcode():
    qr = qrcode.make("https://github.com")
    print("[Qrcode] QR-код успішно згенеровано, розмір:", qr.size)
