![467966890_590440046831906_4416080388337468927_n](https://github.com/user-attachments/assets/647fde77-b7e6-4a36-bfff-32d722e410f7)

# UniFormation GK3 Integration.



**UniFormation GK3, GK3 Pro, GK3 Ultra** for Home Assistant.

## ⚡ Fonctionnalités
- Température en temps réel
- État de l’impression (Idle, Printing, Paused)
- Ajout via interface graphique (config_flow)
- Compatible HACS


## Installation

### Option 1: HACS (Home Assistant Community Store)

To install via HACS:

1. Navigate to HACS -> Integrations -> "+ Explore & Download Repos".
   `https://github.com/SoFarSoGood86/UniFormation-GK3.git`
2. Search for `UniFormation GK3`.
3. Click on the result and select "Download this Repository with HACS".
4. Refresh your browser (due to a known HA bug that may not update the integration list immediately).
5. Go to "Settings" in the Home Assistant sidebar, then select "Devices and Services".
6. Click the blue [+ Add Integration] button at the bottom right, search for "UniFormation GK3", and install it.  
   [![Set up a new integration in Home Assistant](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=nodered)


## 🧭 Exemple de carte Lovelace

```yaml
!include /config/lovelace/example_card.yaml
```

## 📸 Icône
L’icône est disponible dans `custom_components/uniformation_gk3/icons/`.

## 📜 Licence
MIT
