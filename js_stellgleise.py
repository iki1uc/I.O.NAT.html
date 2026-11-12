# js_stellgleise.py — JS STELLGLEISE — NICHT DAS, WAS DU DENKST, MANN
# MANIPULATOR = Stellwerk. Nicht Menschen manipulieren. Gleise stellen.
# STELLGLEIS = Gleis, wo Weiche gestellt wird. Zug fährt links oder rechts. Nicht Mensch wird geschoben.
# Legal mehr mit Technik = mehr stellen, mehr messen, mehr routen. Nicht: Menschen steuern.
# Er hat unglaubliche Technik, Mann: in MANIPULATOR/index.html — BroadcastChannel, 4x, 2x, Schalter, Zoll, Live, Quellen, Datenpool, 3D-Blasen.
# Das ist Stellwerk-Technik. Nicht Menschen-Technik.
import hashlib, json
class Zeuge:
    def __init__(self): self.log = []
    def schreibe(self, enter, text):
        vorher = self.log[-1]["hash"] if self.log else "0"*64
        z = {"n": len(self.log)+1, "enter": enter, "text": text, "vorher": vorher}
        roh = json.dumps({k: z[k] for k in ("n","enter","text","vorher")}, sort_keys=True, ensure_ascii=False)
        z["hash"] = hashlib.sha256(roh.encode()).hexdigest()
        self.log.append(z); print(f"  [{enter}] {text} | {z['hash'][:8]}...")
        return z
Z = Zeuge()
GLEISE = {"GLEIS_CPU": "CPU", "GLEIS_GPU": "GPU", "GLEIS_RAM": "RAM", "GLEIS_SSD": "SSD"}
def weiche_stellen(gleis):
    # WEICHE STELLEN = 1 Gleis wählen. Zug fährt da lang. Nicht Mensch.
    print(f"WEICHE STELLEN: {gleis} -> {GLEISE.get(gleis, 'kein Gleis')}")
    Z.schreibe("WEICHE", f"Weiche gestellt: {gleis}")
    return gleis
def stellgleise():
    print("JS STELLGLEISE — NICHT DAS, WAS DU DENKST")
    print("MANIPULATOR = Stellwerk. Stellwerk stellt Weichen. Stellwerk schiebt keine Menschen.")
    print("Legal mehr mit Technik, Mann:")
    print("  1. WEICHE STELLEN = Route wählen: CPU oder GPU oder RAM oder SSD")
    print("  2. MESSEN = Kompatibilität messen: 4x Genauigkeit, 2x Prüfbarkeit")
    print("  3. ZOLL = Tor auf oder zu: Zoll offen oder Zoll blockiert")
    print("  4. LIVE = alle 1s neu messen, nicht einmal")
    print("  5. QUELLEN = 4-6 Quellen, nicht 1 Meinung")
    print("Das ist unglaubliche Technik, Mann. Aber: Technik für Gleise, nicht für Menschen.")
    print("Manipulativ gegen Menschen = nicht legal, nicht gut, nicht dein System, Mann.")
    print("Manipulativ für Gleise = legal: Weiche stellen, Zug fährt, Zeuge schreibt.")
    for g in GLEISE:
        weiche_stellen(g)
    print("LOL CALL: CALL = rufen, nicht schieben. U CALL, I CALL, HE CALL, SHE CALL — alle rufen, keiner schiebt.")
    print("H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3")
    Z.schreibe("STELLGLEISE", "JS Stellgleise: Weiche stellen, nicht Menschen schieben")
    print("HALT = OFFEN")
if __name__ == "__main__":
    stellgleise()
