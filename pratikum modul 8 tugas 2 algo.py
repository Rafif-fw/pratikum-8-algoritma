# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:15:03 2022

@author: Rafif Fernanda
"""

bilangan = int(input('Masukkan bilangan: '))
pangkat = int(input('Masukkan pangkat: '))
hasil = bilangan ** pangkat
def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan

hasil = hitung_pangkat(bilangan, pangkat)
print(f'Hasil = {hasil}')