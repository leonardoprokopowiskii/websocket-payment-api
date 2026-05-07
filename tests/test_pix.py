import sys
sys.path.append('../')

import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix()
    pix_info = pix_instance.create_payment(base_dir="../")
    qr_code_path = pix_info['qr_code_path']

    assert "bank_payment_id" in pix_info
    assert "qr_code_path" in pix_info
    assert os.path.isfile(f'../static/img/{qr_code_path}.png')