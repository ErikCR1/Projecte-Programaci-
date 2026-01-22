# Choose Your Story: Engine & Adventures

![Status](https://img.shields.io/badge/Status-Projecte%20Finalitzat-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/DB-MySQL-orange)

Benvinguts a **Choose Your Story**, un motor de jocs d'aventura conversacional on les teves decisions dictaminen el destí dels protagonistes. Aquest projecte integra programació en Python, gestió de bases de dades relacionals i una infraestructura de servidor segura.

---

## Sobre el Projecte
Aquest programari no és només un joc, sinó un **intèrpret de bases de dades**. El motor llegeix les situacions i opcions directament des de SQL, permetent afegir noves històries sense modificar ni una sola línia de codi Python.

### Les Històries Disponibles:
1. **Rescate Crítico: Infiltración:** Una missió tàctica on cada segon compta. Hauràs de decidir quan usar la força i quan la diplomàcia per salvar un ostatge.
2. **Muerte en la casa de los Gemelos:** Un repte de detectius on hauràs d'analitzar proves físiques (fang, verins) per trobar el culpable entre diversos sospitosos.

---

## Arquitectura Tècnica
El projecte se sustenta en tres pilars:

| Component | Tecnologia | Descripció |
| :--- | :--- | :--- |
| **Lògica** | Python 3 | Gestió del flux del joc, validació d'entrades i connexió SQL. |
| **Dades** | MySQL | Emmagatzematge de passos, opcions, usuaris i historial de partides. |
| **Servidor** | Proxmox / LXC | Entorn virtualitzat on resideix el servei de base de dades. |

### Diagrama de Flux de Dades:
`Usuari` <--> `Python (Local)` <--> `Túnel SSH` <--> `MySQL (Remot)`

---

## Configuració del Sistema

### 1. Preparació de la Base de Dades
Abans de jugar, cal importar els esquemes situats a la carpeta `M02_Base_Dades/`:
1. Executa `estructura.sql` per crear les taules.
2. Executa `dades.sql` per carregar les aventures.

### 2. Connexió Segura (SSH)
Com que el servidor està protegit, és necessari mapejar el port remot al teu local:
```bash
ssh -L 3308:localhost:3306 elteu_usuari@kamehouse.iesevissa.cat
