![467966890_590440046831906_4416080388337468927_n](https://github.com/user-attachments/assets/647fde77-b7e6-4a36-bfff-32d722e410f7)

# UniFormation GK3 Integration.



**UniFormation GK3, GK3 Pro, GK3 Ultra** for Home Assistant.

## ⚡ Fonctionnalités
- Température en temps réel
- État de l’impression (Idle, Printing, Paused)
- Ajout via interface graphique (config_flow)
- Compatible HACS

## 🛠️ Installation
1. Ajouter le dépôt GitHub dans HACS  
   `https://github.com/SoFarSoGood86/UniFormation-GK3.git`
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
