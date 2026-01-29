# Deployment Configuration for HTTPS

## HTTPS Support

This Django application is configured to enforce HTTPS using Django security settings.
In production, HTTPS must be enabled at the web server level using SSL/TLS certificates.

## Example: Nginx HTTPS Configuration

- Obtain an SSL certificate (e.g., Let's Encrypt)
- Configure Nginx to redirect HTTP to HTTPS
- Enable SSL directives

Example redirect:

server {
listen 80;
server_name example.com;
return 301 https://$host$request_uri;
}

Example SSL block:

server {
listen 443 ssl;
server_name example.com;

    ssl_certificate /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }

}
