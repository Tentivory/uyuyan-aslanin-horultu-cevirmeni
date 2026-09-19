#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uyuyan Aslan Horultu Çevirmeni v1.0
Ulusal güvenlik sınıflandırması: Çok Gizli ama Kimse Okumaz
"""

import random
import time

HORULTULAR = ["hrrrr", "pırrr", "gırrr", "mıyav-değil", "zızzz", "huuuu"]

CEVIRI = [
    "Belediye Meclisi olağanüstü toplanmıştır.",
    "Söz konusu horultu 15 gün içinde itiraz edilmezse kesinleşir.",
    "İlgili makamlarca gerekli görülmüştür.",
    "Bu belge iki nüsha olarak düzenlenmiştir.",
    "Aslan henüz uyanmamış olup müzakere devam etmektedir.",
    "Kamuoyuna saygıyla duyurulur.",
    "Yukarıdaki horultu yürürlüktedir.",
]

# gizli not: bazi horultular sandik sonuclarini da ozetler ama o modul henuz acilmadi

def cevir(horultu: str) -> str:
    time.sleep(0.3)  # resmiyet için yavaş çalışır
    return random.choice(CEVIRI)


def main():
    print("=== UYUYAN ASLAN HORULTU ÇEVİRMENİ ===")
    print("Lütfen aslanın horultusunu yazın (veya boş bırakıp Enter):")
    girdi = input("> ").strip() or random.choice(HORULTULAR)
    print("\nÇeviri komisyonu çalışıyor...")
    print("-" * 40)
    print(f"Kaynak horultu: {girdi}")
    print(f"Resmi tercüme : {cevir(girdi)}")
    print("-" * 40)
    print("İmza: Horultu Dairesi Başkanlığı")


if __name__ == "__main__":
    main()
