# M01: Sistemes Informàtics - Infraestructura del Projecte

## 🖥️ Servidor de Producció (Proxmox)
L'entorn d'execució per a la base de dades és un contenidor Linux (LXC) allotjat al servidor Proxmox de l'institut (`kamehouse.ieti.site`).

### Especificacions del Servidor:
- **Sistema Operatiu:** Ubuntu Server / Debian (LXC).
- **Servei DB:** MySQL Server.
- **Gestió de Processos:** PM2 (per assegurar que els serveis web i de base de dades estiguin sempre actius).

---

## 🔐 Seguretat i Accés Remot
Per complir amb les normatives de seguretat, el servidor no té ports oberts a l'exterior (excepte SSH).

### 1. Autenticació mitjançant Claus RSA
En lloc d'utilitzar contrasenyes tradicionals, s'ha configurat l'accés mitjançant **claus públiques/privades**:
1. Generació de clau local: `ssh-keygen -t rsa`.
2. Pujada de la clau pública al portal de claus del Proxmox.
3. Permisos de seguretat: `chmod 600 ~/.ssh/id_rsa`.

### 2. Túnel SSH (Port Forwarding)
Per connectar el codi Python (client) amb la base de dades MySQL (servidor), s'ha implementat un túnel SSH. Això permet redirigir el trànsit del port remot al port local de forma xifrada i segura.

**Comandes utilitzades:**
- **Obrir túnel:** `bash ./proxmoxTunelStart.sh`
- **Connexió manual:** `ssh -L 3308:localhost:3306 usuari@kamehouse.iesesteveterradas.cat`

*Nota: S'utilitza el port local 3308 per evitar conflictes amb instal·lacions locals de MySQL.*

---

## 🛠️ Gestió i Desplegament
S'han utilitzat scripts d'automatització per a les tasques de manteniment:

- **Redirecció de trànsit:** Ús de `iptables` per redirigir peticions del port 80 al 3000 (NodeJS) per a la web promocional.
- **Desplegament:** Ús de `proxmoxDeploy.sh` per empaquetar i enviar fitxers al servidor.
- **Monitorització:** Ús de `pm2 list` per verificar l'estat dels serveis en temps real.

---

## 📋 Configuració de Xarxa Local
Perquè el joc funcioni, el fitxer `funcions.py` apunta a l'adreça de bucle invertit configurada pel túnel:
- **Host:** `127.0.0.1`
- **Port:** `33
