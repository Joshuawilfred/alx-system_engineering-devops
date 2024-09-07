# Postmortem: Laravel Asset Loading Issue on cPanel

## Issue Summary
- **Duration**: The outage lasted for 4 hours, from 14:00 to 18:00 UTC on September 7, 2024.
- **Impact**: The main website's frontend was severely affected. Users experienced broken layouts and missing images. Approximately 80% of users were impacted, as the issue affected all pages using bundled assets via Vite.
- **Root Cause**: Misconfiguration of the cPanel server prevented proper loading of Vite-bundled assets in the Laravel application.

## Timeline
- 14:00 UTC - Issue detected upon deployment of the Laravel application to the production cPanel server.
- 14:15 UTC - Development team noticed broken layouts and missing assets during post-deployment checks.
- 14:30 UTC - Initial investigation focused on potential Vite configuration issues in the Laravel project.
- 15:00 UTC - Debugging path shifted to examining cPanel's Apache configuration after Vite config appeared correct.
- 15:45 UTC - Issue escalated to the DevOps team for server-side investigation.
- 16:30 UTC - Root cause identified as a misconfiguration in cPanel's asset handling for Laravel applications.
- 17:30 UTC - Temporary fix implemented by manually linking assets without Vite bundling.
- 18:00 UTC - Service fully restored with the temporary fix in place.

## Root Cause and Resolution
The root cause was a misconfiguration in cPanel's Apache settings, which prevented proper handling of Vite-bundled assets in the Laravel application. The server was not correctly routing requests for these assets, resulting in 404 errors.

As a temporary resolution, we manually linked each asset using direct URLs (e.g., mydomain/assets/nvj453434tuser.png) instead of relying on Vite's bundling. This allowed the website to function properly while a permanent solution was developed.

## Corrective and Preventative Measures
Improvements and fixes:
1. Update cPanel server configuration to properly handle Laravel applications with Vite.
2. Implement a staging environment that mirrors the production setup for thorough testing.
3. Enhance deployment checklist to include asset loading verification.
4. Set up monitoring for asset loading performance and errors.

Tasks to address the issue:
1. Configure cPanel's Apache to properly route Vite-bundled asset requests.
2. Update deployment scripts to include Vite build process.
3. Create a staging environment on a separate cPanel instance.
4. Implement automated tests for asset loading post-deployment.
5. Set up monitoring alerts for 404 errors related to asset loading.
6. Document the correct cPanel configuration for Laravel + Vite applications.
7. Conduct a team training session on troubleshooting asset loading issues in various hosting environments.

This incident highlighted the importance of thorough pre-deployment testing and the need for environment-specific configurations when working with modern web frameworks and build tools. By implementing these corrective measures, we aim to prevent similar issues in the future and improve our overall deployment process.
