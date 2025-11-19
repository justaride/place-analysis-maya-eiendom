# Place Analysis Template

Dette er master template-prosjektet for alle Place Analysis eiendomsprosjekter.

## ⚠️ VIKTIG

Dette er MASTER-prosjektet. Alle endringer på felles komponenter og sider skal gjøres her først, og deretter synkroniseres til andre prosjekter.

## 🎯 Formål

- **Utvikle** nye features og design
- **Teste** endringer før utrulling
- **Kilde** for synkronisering til produksjonsprosjekter

## 🚀 Quick Start

```bash
# Installer dependencies
npm install

# Start dev server
npm run dev

# Bygg for produksjon
npm run build
```

## 📦 Hva er felles?

### Layout Komponenter
- `src/components/layout/Header.tsx`
- `src/components/layout/Footer.tsx`
- `src/components/layout/Navigation.tsx`

### UI Komponenter
- `src/components/ui/` (Card, Button, Container, etc.)

### Sider
- `src/app/page.tsx` (forside)
- `src/app/om-prosjektet/page.tsx`
- `src/app/layout.tsx`

### Styling
- `tailwind.config.ts`
- `src/app/globals.css`

## 🔄 Synkronisere til andre prosjekter

```bash
# Gå til root
cd ~

# Test-kjør (anbefalt først!)
npm run sync:dry

# Synkroniser alt
npm run sync

# Eller selektivt:
npm run sync:layout   # Kun Header, Footer, Navigation
npm run sync:pages    # Kun forside og om-side
npm run sync:ui       # Kun UI komponenter
```

## 📝 Workflow

1. **Gjør endringer** i dette prosjektet
2. **Test lokalt** med `npm run dev`
3. **Commit** endringer her
4. **Synkroniser** til andre prosjekter med `npm run sync`
5. **Commit og push** i hvert prosjekt

## 🛡️ Hva skal IKKE være her?

- ❌ Produksjonsdata (eiendomsdata, properties)
- ❌ API keys og secrets
- ❌ Plaace screenshots (prosjekt-spesifikke)
- ❌ Analyse-spesifikke komponenter

## 📚 Dokumentasjon

Se `PLACE_ANALYSIS_SYNC_GUIDE.md` i root for komplett dokumentasjon.

---

**Template Version:** 1.0.0
