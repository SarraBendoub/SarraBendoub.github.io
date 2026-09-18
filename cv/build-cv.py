# -*- coding: utf-8 -*-
"""Genere les PDF du CV a partir des sources HTML (cv-fr.html / cv-en.html).

Usage :  python cv/build-cv.py
Sortie :  cv/Sarra_Ben_Doub_CV_FR.pdf  et  cv/Sarra_Ben_Doub_CV_EN.pdf

Le rendu utilise Chrome en mode headless. La mise en page (format A4, marges)
est definie dans cv.css via la regle @page.
"""
import os
import subprocess
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

JOBS = [
    ("cv-fr.html", "Sarra_Ben_Doub_CV_FR.pdf"),
    ("cv-en.html", "Sarra_Ben_Doub_CV_EN.pdf"),
]


def find_browser():
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    sys.exit("Aucun navigateur Chrome/Edge trouve pour le rendu PDF.")


def build(browser, src, out):
    src_path = HERE / src
    out_path = HERE / out
    if not src_path.exists():
        print("  (ignore, source absente) " + src)
        return None
    avant = out_path.stat().st_mtime if out_path.exists() else 0
    subprocess.run([
        browser,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=10000",
        "--print-to-pdf=" + str(out_path),
        src_path.as_uri(),
    ], check=True, capture_output=True)
    # Chrome sort en code 0 meme quand l'ecriture echoue, typiquement quand le PDF
    # est deja ouvert dans un lecteur. Sans ce controle, le script annonce un succes
    # et le fichier reste celui de la veille.
    if not out_path.exists() or out_path.stat().st_mtime == avant:
        print("  ATTENTION  %-26s NON REGENERE : le fichier est probablement ouvert "
              "dans un lecteur PDF, ferme-le et relance." % out)
        return None
    return out_path


def main():
    browser = find_browser()
    print("Navigateur :", browser)
    for src, out in JOBS:
        out_path = build(browser, src, out)
        if out_path is None:
            continue
        try:
            import fitz
            doc = fitz.open(out_path)
            pages = doc.page_count
            doc.close()
            flag = "  <-- DEBORDE SUR 2 PAGES" if pages > 1 else ""
            print("  %-30s %d page(s)%s" % (out, pages, flag))
        except ImportError:
            print("  %-30s genere" % out)


if __name__ == "__main__":
    main()
