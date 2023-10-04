## \*arr

Les iso Linux c'est comme le sexe, on est mieux protégé...

```yml
version: "2.2"
services:
  prowlarr:
    image: lscr.io/linuxserver/prowlarr:latest
    container_name: prowlarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Paris
    volumes:
      - ./prowlarr:/config
    ports:
      - 9696:9696
    restart: unless-stopped
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Paris
    volumes:
      - ./sonarr:/config
      - D:\Media:/media-dir
      - D:\Media\transmission:/data
    ports:
      - 8989:8989
    restart: unless-stopped
  radarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Paris
    volumes:
      - ./radarr:/config
      - D:\Media\transmission:/data
      - D:\Media:/media-dir
    ports:
      - 7878:7878
    restart: unless-stopped
  flaresolverr:
    # DockerHub mirror flaresolverr/flaresolverr:latest
    image: ghcr.io/flaresolverr/flaresolverr:latest
    container_name: flaresolverr
    environment:
      - LOG_LEVEL=${LOG_LEVEL:-info}
      - LOG_HTML=${LOG_HTML:-false}
      - CAPTCHA_SOLVER=${CAPTCHA_SOLVER:-none}
      - TZ=Europe/London
    ports:
      - "${PORT:-8191}:8191"
    restart: unless-stopped
  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - WATCHTOWER_CLEANUP=True
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
      - PGID=1000
      - TZ=Europe/Paris
    volumes:
      - ./cache:/config
      - ./config:/cache
      - D:\Media:/media:ro
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
