import numpy as np
from numpy import ndarray
from Pyfhel import Pyfhel

import numpy as np

def string_to_numpy(str_to_convert: str) -> ndarray:
    arr_str = np.array([ord(c) for c in str_to_convert], dtype=np.float64)
    return arr_str

def numpy_to_string(numpy_to_convert: ndarray) -> str:
    decrypted_str = ''.join([chr(int(round(c))) for c in numpy_to_convert])
    return decrypted_str

import numpy as np
from Pyfhel import Pyfhel

def ckks_string():
    n_mults = 0  
    HE = Pyfhel(key_gen=True, context_params={
        'scheme': 'CKKS',
        'n': 2**14,         
        'scale': 2**30,     
        'qi_sizes': [60]  # 체인에 하나의 큰 소수만 있으면 됨
    })
    HE.relinKeyGen()
    print("\nCKKS 컨텍스트 생성")
    print(f"\t{HE}")

    # 문자열을 numpy 배열로 변환
    str_to_encrypt = "Hello world"
    arr_str = string_to_numpy(str_to_encrypt)

    # CKKS 배열 인코딩 및 암호화
    ctxt_str = HE.encryptFrac(arr_str)

    print("\n문자열 인코딩 및 암호화")
    print("->\t원본 문자열: ", str_to_encrypt,'\n\t==> ctxt_str: ', ctxt_str)

    # 암호화된 데이터의 복호화 및 출력
    decrypted_arr = HE.decryptFrac(ctxt_str)
    decrypted_str = numpy_to_string(decrypted_arr)
    print("\n복호화된 문자열: ", decrypted_str)

ckks_string()
