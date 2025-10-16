# 🖨️ UniFormation GK3 – Intégration Home Assistant

Cette intégration permet de surveiller et de contrôler votre imprimante 3D **UniFormation GK3** directement depuis Home Assistant.

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
