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

## Config-options

|Environment-Variable|Value|Explanation|Standard|
|---|---|---|---|
|`PASSWORD_LOGIN`|`boolean`|If set to `true` login over `UTKUMA_PASSWORD` and `UTKUMA_TOKEN`, otherwise `UTKUMA_TOKEN` has to be set.|❌
|`UTKUMA_PASSWORD`|`string`|The password for your account (Necessary if `PASSWORD_LOGIN` is set to `true`)|❌
|`UTKUMA_USERNAME`|`string`|The username of your account (Necessary if `PASSWORD_LOGIN` is set to `true`)|❌
|`UTKUMA_TOKEN`|`string`|The token for your account (Necessary if `PASSWORD_LOGIN` is set to `false`)|❌
|`UTKUMA_URL`|`string`|The base-url of your uptime-kuma-instance (eg. `https://demo.uptime.kuma.pet:27000/`)|❌
|`ANALYTICS_ENABLED`|`boolean`|If set to `true` or not set, [Plausible](https://plausible.io) will be used (hosted on my own server)|`true`