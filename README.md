# uptime-kuma-static
## Introduction
I really love [Uptime Kuma](https://github.com/louislam/uptime-kuma) by **[Louis Lam
](https://github.com/louislam)**, but I wanted a status-page like [Statuspage.io](https://statuspage.io) or similar,
so I created this piece of software. It fetches the data from [Uptime Kuma](https://github.com/louislam/uptime-kuma) and
renders a HTML-Template with the data, which can look like this:
![Screenshot of the rendered template](https://i.imgur.com/pwzr71t.png "Screenshot of the rendered template")


## Set up

### With Docker
1. Pull the image: `docker pull ghcr.io/mawoka-myblock/uptime-kuma-static:latest`
2. Create the container:
```bash
docker run -d \
  -e "PASSWORD_LOGIN=true" \
  -e "UTKUMA_PASSWORD=YOUR_PASSWORD" \
  -e "UTKUMA_USERNAME=YOUR_USERNAME" \
  -e "UTKUMA_URL=YOUR_URL" \
  -e "ANALYTICS_ENABLED=true"
  -v "$(pwd)"/out:/app/out \
  --name utkuma-static ghcr.io/mawoka-myblock/uptime-kuma-static:latest
```
3. Just serve the `index.html` in the `out/`-directory with your favourite
webserver (I prefer nginx (Btw: Did you know that `nginx` is pronounced
`"engine-x"`?)) 
4. Have fun