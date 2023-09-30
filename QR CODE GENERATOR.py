import qrcode as qr
from PIL import Image

def generate_qr_code(url, output_file, size=200, logo=None):
    qr_code = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_code.add_data(url)
    qr_code.make(fit=True)

    qr_img = qr_code.make_image(fill_color="black", back_color="yellow")

    if logo:
        logo_img = Image.open(logo)
        logo_img = logo_img.resize((size // 4, size // 4))
        qr_img.paste(logo_img, (size // 3, size // 3))

    qr_img = qr_img.resize((size, size))
    qr_img.save(output_file)

def main():
    print("QR Code Generator")
    num_qr_codes = int(input("Enter the number of QR codes to generate: "))

    for i in range(num_qr_codes):
        print(f"\nGenerating QR code {i + 1}")
        url = input("Enter the URL: ")
        output_file = input("Enter the output file name (e.g., qr_code.png): ")
        size = int(input("Enter the size of the QR code (default is 200): "))
        logo = input("Enter the path to a logo image (leave empty for no logo): ")

        generate_qr_code(url, output_file, size, logo)
        print(f"QR code generated and saved as '{output_file}'")

if __name__ == "__main__":
    main()
