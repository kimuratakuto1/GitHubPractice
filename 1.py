import qrcode

# QRコードに埋め込むデータ（例: URL）
data = "https://chatgpt.com/"

# QRコードの生成
qr = qrcode.QRCode(
    version=1,  # QRコードのサイズ（1〜40）自動調整ならNoneでOK
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 誤り訂正レベル
    box_size=10,  # 1マスのピクセル数
    border=4,  # QRコードの周りの白枠（マス単位）
)

qr.add_data(data)
qr.make(fit=True)

# QRコード画像を生成
img = qr.make_image(fill_color="black", back_color="white")

# 画像として保存
img.save("qrcode.png")

print("QRコードを qrcode.png として保存しました。")
