# RH-Plugin-Dropgate

A RotorHazard plugin that adds functionality for an automatic dropgate.

## Features

- Control a dropgate using a Raspberry Pi GPIO pin.
- Configure the GPIO pin directly from the RotorHazard settings menu.
- Optionally set up a mirrored timer for advanced synchronization.

---

## Installation

1. **Set up RotorHazard**  
   Install RotorHazard on your Raspberry Pi (Zero or compatible).

2. **Add the Plugin**  
   Copy the entire contents of the `RH-Dropgate-Plugin` directory into the RotorHazard plugin directory on your Raspberry Pi.

3. **Configure GPIO**  
   If you're not using the default GPIO pin (12), specify a different GPIO pin in the RotorHazard settings menu.

4. **Optional: Use a Mirror Timer**  
   For advanced setups, configure a mirror timer as described in the [RotorHazard mirror documentation](https://github.com/RotorHazard/RotorHazard/blob/main/doc/Cluster.md).

---

## Required Hardware

### **Recommended Raspberry Pi**

- **Raspberry Pi Zero W / Zero 2 W**  
   Affordable and compact, ideal for this project.  
- **Other Options (RPI3/4/5)**  
   These are compatible but may require a different case and are more expensive.

---

### **Power Supplies**

- **12V BEC**  
   Ensure at least 5A capacity for the electromagnets.  
   - Recommended: XL4015 or XL4005.

- **5V BEC**  
   Powers the Raspberry Pi.  
   - Example: Mateksys 30 to 5V BEC.

---

### **Relay**

- **12V Relay**  
   Requires a minimum of 5A capacity (higher is better).  
   - Example: [TinyTronics 12V Relay](https://www.tinytronics.nl/nl/schakelaars/relais/12v-relais-1-channel-hoog-actief-of-laag-actief-30a).

---

### **Electromagnets**

- **12V 40mm Electromagnets**  
   Requires 2 magnets. Designed for 40mm versions, such as the 25KG JF-XP4020 model.  
   The dropgate's round bar may reduce the magnet's efficiency, so choose stronger magnets when possible.  
   - Example: [JF-XP4020](https://www.tinytronics.nl/nl/mechanica-en-actuatoren/elektromagneten/elektromagneet-25kg-12v-dc-jf-xp4020).

---

### **Connectors**

- **XT60E Connectors**  
   - 2x XT60EF (Female).  
   - 3x XT60E (Male).

---

### **Optional: Micro USB (OTG) Ethernet Adapter**

While the Raspberry Pi Zero W has WiFi, a wired connection is more stable.

---

### **Double-Sided Tape**

Use tape to secure the relay, 5V BEC, and 12V BEC to the case.  
Recommended: Thick, heat-resistant tape (e.g., "gecko tape").

---

### **M3 Screws**

- **4x M3x6mm**: For the lid.  
- **4x M3x16mm**: For the Raspberry Pi Zero W bracket.  
- **6x M3x12mm**: For the XT60 connectors.

---

### **3D Prints**

- **1x Case**  
- **2x Magnet/Pole Holders**

3D print files are located in the `/prints` folder.

---

### **Other Hardware**

- **32mm Tubes**: Cut to desired lengths/heights.  
- **Aluminum Rod**: Matches the length of your dropgate banner.  
- **Metal Rod Ends**: Attach to the aluminum rod to stick to the magnets.