![467966890_590440046831906_4416080388337468927_n](https://github.com/user-attachments/assets/52a0435f-4f8f-4a22-a993-ebbb376ff694)

# UniFormation GK3 Integration.

**UniFormation GK3, GK3 Pro, GK3 Ultra** for **Home Assistant** intégration.

## ⚡ Fonctionnalités
- Température en temps réel
- État de l’impression (Idle, Printing, Paused)
- Ajout via interface graphique (config_flow)
- Compatible HACS

## 🛠️ Installation
1. Ajouter le dépôt GitHub dans HACS  
   `https://github.com/SoFarSoGood86/homeassistant-UniFormation-GK3`
2. Installer l’intégration `UniFormation GK3`
3. Redémarrer Home Assistant
4. Aller dans **Paramètres > Appareils & Services > Ajouter une intégration** et sélectionner *UniFormation GK3*.

## 🧭 Exemple de carte Lovelace

```yaml
!include /config/lovelace/example_card.yaml
```

## 📸 Icône
L’icône est disponible dans `custom_components/uniformation_gk3/icons/`.

## 📜 Licence
MIT
