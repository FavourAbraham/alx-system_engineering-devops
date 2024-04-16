# Project Name.
**0x13. Firewall**

##  Requirements

### Bash Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   All your bash scripts must be executable.
*   Your Bash script must pass `shellcheck` without any error.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.

## Project Description.
Learn about firewalls.


* **0. Block all incoming traffic but** - Configure `ufw` so that it blocks all incoming traffic, except the TCP ports `22` (SSH), `443` (HTTPS SSL), `80` (HTTP). - `0-block_all_incoming_traffic_but`.
---

* **1. Port forwarding** - Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP` and paste ufw config settings in answer file. - `100-port_forwarding`.

    Terminal in `web-01`:
