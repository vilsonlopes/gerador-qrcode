import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def gerar_qrcode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    #print('Insira o que deseja transformar em QRCode: ')
    #input_qr = str(input())

    qr.add_data('developer@developer.py')
    qr.make(fit=True)

    img = qr.make_image(image_factory=StyledPilImage,
                        module_drawer=RoundedModuleDrawer(),
                        color_mask=RadialGradiantColorMask(),
                        )

    img.save('instagram.png')
    img.show()
