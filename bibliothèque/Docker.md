## \*arr

Les iso Linux c'est comme le sexe, on est mieux protégé...[^1][^2]

```yml
version: "3.1"
services:
  flaresolverr:
    image: ghcr.io/flaresolverr/flaresolverr:latest
    container_name: flaresolverr
    environment:
      - LOG_LEVEL=${LOG_LEVEL:-info}
      - LOG_HTML=${LOG_HTML:-false}
      - CAPTCHA_SOLVER=${CAPTCHA_SOLVER:-none}
      - TZ=Europe/Paris
    ports:
      - "${PORT:-8191}:8191"
    restart: unless-stopped
  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - WATCHTOWER_CLEANUP= "true"
      - TZ=Europe/Paris
      - WATCHTOWER_SCHEDULE= 0 0 17 * * *
    restart: unless-stopped
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=13001
      - PGID=13000
      - UMASK=002
      - TZ=Europe/Paris
    volumes:
      - ./sonarr:/config
      - Media:/data
    ports:
      - "8989:8989"
    restart: unless-stopped

  radarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    environment:
      - PUID=13002
      - PGID=13000
      - UMASK=002
      - TZ=Europe/Paris
    volumes:
      - ./radarr:/config
      - Media:/data
    ports:
      - "7878:7878"
    restart: unless-stopped

  prowlarr:
    image: lscr.io/linuxserver/prowlarr:develop
    container_name: prowlarr
    environment:
      - PUID=13006
      - PGID=13000
      - UMASK=002
      - TZ=Europe/Paris
    volumes:
      - ./prowlarr:/config
    ports:
      - "9696:9696"
    restart: unless-stopped

  arch-qbittorrentvpn:
    image: binhex/arch-qbittorrentvpn:latest
    container_name: qbittorrent
    cap_add:
      - NET_ADMIN
    ports:
      - 6881:6881
      - 6881:6881/udp
      - 8080:8080
      - 8118:8118
    volumes:
      - 'Media\downloads:/data/downloads'
      - ./qbittorent:/config
    environment:
      - VPN_ENABLED=yes
      - VPN_USER=*********
      - VPN_PASS=*********
      - VPN_PROV=pia
      - VPN_CLIENT=openvpn
      - STRICT_PORT_FORWARD=yes
      - ENABLE_PRIVOXY=yes
      - LAN_NETWORK=192.168.144.33/24
      - NAME_SERVERS=84.200.69.80,37.235.1.174,1.1.1.1,37.235.1.177,84.200.70.40,1.0.0.1
      - VPN_INPUT_PORTS=1234
      - VPN_OUTPUT_PORTS=5678
      - DEBUG=false
      - WEBUI_PORT=8080
      - PUID=13007
      - PGID=13000
      - UMASK=002
    restart: unless-stopped
```

## Jellyfin

Pour héberger vos médias acquis légalement.

```yml
version: "2.20"
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    ports:
      - 8096:8096
    environment:
      - PUID=1000
      - PGID=13000
      - UMASK=002
      - TZ=Europe/Paris
    volumes:
      - ./jellyfin/cache:/config
      - ./jellyfin/config:/cache
      - Media\Media:/media:ro
    restart: "unless-stopped"
  jellystat-db:
    image: postgres
    container_name: jellystat-db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: mypassword
    volumes:
      - ./data/postgres:/var/lib/postgresql/data # Mounting the volume
  jellystat:
    image: cyfershepard/jellystat:latest
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: mypassword
      POSTGRES_IP: jellystat-db
      POSTGRES_PORT: 5432
      JWT_SECRET: "my-secret-jwt-key"
    ports:
      - "3000:3000" #Server Port
      - "3004:3004" #websocket port
    volumes:
      - ./data/jellystat:/app/backend/backup-data # Mounting the volume

    depends_on:
      - jellystat-db
networks:
  default:
```

[^1]: Vous l'avez ou l'avez pas
[^2]: NOT a legal advice
