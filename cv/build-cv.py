# -*- coding: utf-8 -*-
"""Genere les PDF du CV a partir des sources HTML (cv-fr.html / cv-en.html).

Usage :  python cv/build-cv.py

Quatre PDF sont produits, deux par langue :

  Sarra_Ben_Doub_CV_FR.pdf      banque, assurance, leasing  -> portfolio principal
  Sarra_Ben_Doub_CV_EN.pdf
  Sarra_Ben_Doub_CV_FR_IA.pdf   editeurs, ESN, cabinets     -> portfolio /ai
  Sarra_Ben_Doub_CV_EN_IA.pdf

La source HTML porte la version banque. La version IA en est derivee a la volee :
seuls le titre, la phrase de recherche et l'adresse du portfolio changent. Tout le
reste (experiences, projets, chiffres) reste commun, donc une seule source a corriger.

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

from variantes_ia import REMPLACEMENTS_IA  # noqa: E402  (table des remplacements banque -> IA)

JOBS = [
    ("cv-fr.html", "Sarra_Ben_Doub_CV_FR.pdf", None),
    ("cv-en.html", "Sarra_Ben_Doub_CV_EN.pdf", None),
    ("cv-fr.html", "Sarra_Ben_Doub_CV_FR_IA.pdf", "ia"),
    ("cv-en.html", "Sarra_Ben_Doub_CV_EN_IA.pdf", "ia"),
]


def find_browser():
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    sys.exit("Aucun navigateur Chrome/Edge trouve pour le rendu PDF.")


def preparer_source(src, variante):
    """Renvoie (chemin_html, temporaire). La variante IA passe par un fichier jetable."""
    source = HERE / src
    if not variante:
        return source, False
    texte = source.read_text(encoding="utf-8")
    for avant, apres in REMPLACEMENTS_IA[src]:
        if texte.count(avant) != 1:
            sys.exit("Variante %s : motif absent ou ambigu dans %s :\n  %s"
                     % (variante, src, avant[:70]))
        texte = texte.replace(avant, apres)
    tmp = HERE / ("_tmp_%s_%s" % (variante, src))
    tmp.write_text(texte, encoding="utf-8")
    return tmp, True


def build(browser, src, out, variante=None):
    out_path = HERE / out
    if not (HERE / src).exists():
        print("  (ignore, source absente) " + src)
        return None
    src_path, temporaire = preparer_source(src, variante)
    avant = out_path.stat().st_mtime if out_path.exists() else 0
    try:
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
    finally:
        if temporaire:
            src_path.unlink(missing_ok=True)
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
    for src, out, variante in JOBS:
        out_path = build(browser, src, out, variante)
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
