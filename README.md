![467966890_590440046831906_4416080388337468927_n](https://github.com/user-attachments/assets/647fde77-b7e6-4a36-bfff-32d722e410f7)

**UniFormation GK3, GK3 Pro, GK3 Ultra** for Home Assistant ntegration.
##
Features :
- Real-time temperature
- Print status (Idle, Printing, Paused)
- Added via graphical interface (config_flow)
- HACS Compatible

##
Installation :

Install via HACS

1. Navigate to HACS -> Integrations -> "+ Explore & Download Repos" Search for *UniFormation GK3*.
2. Click on the result and select "Download this Repository with HACS".
3. Refresh your browser (due to a known HA bug that may not update the integration list immediately).
4. Go to "Settings" in the Home Assistant sidebar, then select "Devices and Services".
5. Click the blue [+ Add Integration] button at the bottom right, search for "UniFormation GK3", and install it.  

   [![Set up a new integration in Home Assistant](https://my.home-assistant.io/badges/config_flow_start.svg)](https://github.com/SoFarSoGood86/UniFormation-GK3.git)

##
Lovelace card example :

```yaml
!include /config/lovelace/example_card.yaml
```
##
Icon :
L’icône est disponible dans `custom_components/uniformation_gk3/icons/`.

