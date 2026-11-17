"""Generate the guide pages for the Fix My Site site. Usage: python make_guides.py <site_dir>"""
import json, os, sys, html

SITE = sys.argv[1]
BASE = "https://mugo-ndungu.github.io/fixmysite/"
TODAY = "2026-11-17"

GUIDES = [
 {
  "slug": "website-not-showing-on-google",
  "title": "Website not showing on Google? How to find and fix the cause",
  "h1": "Website not showing on Google?",
  "desc": "Your small business website isn't on Google? Usually a noindex tag, a robots.txt block or a hidden-site setting is the cause. Here's how to check and fix it.",
  "answer": "Most often a setting is telling Google to stay away: a \"noindex\" tag, a robots.txt block, or a \"hide from search engines\" option in your site builder. Remove it, then ask Google to look again in Search Console. Pages usually come back within days to a few weeks.",
  "body": """
<h2>1. Check whether Google has any of your pages</h2>
<p>Search Google for <code>site:yourbusiness.com</code> (with your own address). No results means Google has none of your pages. A few results but not the ones you want means individual pages are blocked.</p>

<h2>2. Look for a "noindex" tag</h2>
<p>Open your homepage, right-click and choose <b>View page source</b>, then search the page (Ctrl+F or Cmd+F) for <code>noindex</code>. If you find <code>&lt;meta name="robots" content="noindex"&gt;</code>, that line is telling Google not to list the page.</p>
<p>Where it usually comes from:</p>
<ul>
  <li><b>WordPress:</b> Settings, then Reading. Untick "Discourage search engines from indexing this site". SEO plugins such as Yoast or Rank Math can also set noindex on single pages.</li>
  <li><b>Wix:</b> in your dashboard's SEO settings, make sure "Let search engines index your site" is switched on. Check each page's SEO settings too.</li>
  <li><b>Squarespace:</b> in the SEO settings, turn off "Hide site from search engines", and check the SEO tab of each page.</li>
  <li><b>Shopify:</b> a store still behind its password page can't be listed. Remove the password once the store is ready.</li>
</ul>

<h2>3. Check robots.txt</h2>
<p>Visit <code>yourbusiness.com/robots.txt</code>. If you see <code>User-agent: *</code> followed by <code>Disallow: /</code>, the whole site is blocked. That line is often left behind from when the site was being built. Remove it, or ask whoever built the site to.</p>

<h2>4. Ask Google to come back</h2>
<p>Add your site to <a href="https://search.google.com/search-console" rel="noopener">Google Search Console</a> (free), open <b>URL Inspection</b>, paste your homepage address and click <b>Request indexing</b>. If your site has a sitemap, submit it under <b>Sitemaps</b>.</p>
""",
  "price": "$100-150",
  "fix": "I find the setting, remove it on every page that has it, and ask Google to recrawl.",
 },
 {
  "slug": "website-not-secure-warning",
  "title": "Website says \"Not secure\"? How to fix an SSL certificate warning",
  "h1": "Browser says your website is \"Not secure\"?",
  "desc": "Visitors see \"Not secure\" or \"Your connection is not private\" on your business website? It's the SSL certificate. Here's how to find the cause and fix it.",
  "answer": "The warning appears when your site's SSL certificate is missing, has expired, or was issued for a different address (for example www but not the plain domain). Most hosts give you a free certificate that renews itself. It just has to be issued correctly and cover every version of your address.",
  "body": """
<h2>1. Find out which problem you have</h2>
<p>In Chrome, click the warning next to your address, then the certificate details. Look at two things: the <b>valid until</b> date, and the name it was <b>issued to</b>. An old date means it expired. A different name means it belongs to another address, often your hosting company's server.</p>

<h2>2. If it expired</h2>
<ul>
  <li><b>cPanel hosting</b> (common with many US hosts): open <b>SSL/TLS Status</b> and click <b>Run AutoSSL</b>.</li>
  <li><b>Other hosts:</b> look for "SSL" in your control panel. Most offer a free Let's Encrypt certificate that renews automatically.</li>
  <li>If a certificate was installed by hand years ago, it won't renew on its own. Replace it with an automatic one.</li>
</ul>

<h2>3. If it's for the wrong address</h2>
<p>Make sure the certificate covers both <code>yourbusiness.com</code> and <code>www.yourbusiness.com</code>, or redirect one to the other. This is the most common cause of a warning that only some visitors see.</p>

<h2>4. Wix, Squarespace and Shopify</h2>
<p>These builders issue the certificate for you once your domain is connected properly. A warning on one of them usually means the domain's DNS settings point somewhere else.</p>

<h2>5. Send everyone to the secure address</h2>
<p>Turn on "Force HTTPS" (or redirect http to https) so nobody lands on the insecure version. If the padlock still shows a warning with a valid certificate, some images or scripts are loading over plain http. They need updating to https.</p>
""",
  "price": "$100-200",
  "fix": "I install a free certificate that renews itself, cover every version of your address, and send all visitors to the secure one.",
 },
 {
  "slug": "wix-domain-not-connected",
  "title": "Wix \"This domain isn't connected to a site\": how to fix it",
  "h1": "Wix says \"This domain isn't connected to a site\"?",
  "desc": "Your Wix address shows \"This domain isn't connected to a site\"? Here's why it happens (expired plan, unpublished site or DNS) and how to reconnect your domain.",
  "answer": "Wix shows this page when your domain reaches Wix but isn't attached to a published site. The usual causes are a Premium plan that lapsed, a site that was unpublished, or DNS settings that changed at your domain company.",
  "body": """
<h2>1. Check the domain in your Wix account</h2>
<p>Log in to Wix and open the <b>Domains</b> page from your account settings. It shows each domain, which site it's attached to, and whether anything needs fixing.</p>

<h2>2. Check your Premium plan</h2>
<p>Connecting your own domain needs an active Wix Premium plan. If a card payment failed, the plan may have ended and the domain disconnected with it. Renew the plan and reconnect the domain.</p>

<h2>3. Make sure the site is published</h2>
<p>Open the site in the Wix editor and click <b>Publish</b>. An unpublished site can't show on your domain.</p>

<h2>4. If you bought the domain somewhere else</h2>
<p>If your domain is with GoDaddy, Namecheap or another company, Wix shows the exact records to set there (either Wix's name servers or pointing records). Enter them at your domain company. Changes can take up to 48 hours to work everywhere.</p>

<h2>5. If you've moved to a new website</h2>
<p>Seeing this after switching away from Wix means the domain still points at Wix. Change the DNS records at your domain company to point to your new host instead.</p>
""",
  "price": "$50-150",
  "fix": "I reconnect the domain (or point it to your new site), check both the www and plain addresses, and confirm your Google listing points to the right place.",
 },
 {
  "slug": "squarespace-website-expired",
  "title": "Squarespace \"Website Expired\": how to bring your site back",
  "h1": "Squarespace says \"Website Expired\"?",
  "desc": "Your Squarespace site shows \"Website Expired\"? The subscription ended, usually from a failed payment. Here's how to log in, resubscribe and keep it from happening again.",
  "answer": "Squarespace shows this page when the website's subscription has ended, most often because a card payment failed. The owner can log in and resubscribe to bring the site back. Don't wait: expired sites are only kept for a limited time.",
  "body": """
<h2>1. Log in as the owner</h2>
<p>Click <b>Owner login</b> on the expired page, or go to squarespace.com and log in with the email address the site was set up with.</p>

<h2>2. Renew the subscription</h2>
<p>Open the site's billing settings, update the card if needed, and choose a plan. The site comes back as it was once the subscription is active.</p>

<h2>3. If you can't get into the account</h2>
<p>Use Squarespace's password reset with the original email. If that email address no longer works (common when a former employee or web designer set the site up), contact Squarespace support and ask them to help you prove ownership.</p>

<h2>4. Check your domain too</h2>
<p>If your domain was bought through Squarespace, it renews separately from the website. Make sure it hasn't expired as well, or your address may stop working even after the site is back.</p>

<h2>5. Stop it happening again</h2>
<p>Use a card that won't expire soon, and make sure billing emails go to an inbox someone actually reads.</p>
""",
  "price": "from $150",
  "fix": "I sort out access and billing with you, bring the site back, check the domain, or move the site to a cheaper setup if Squarespace no longer suits you.",
 },
 {
  "slug": "google-maps-wrong-website-link",
  "title": "Google Maps shows the wrong website for your business? How to fix it",
  "h1": "Google Maps shows the wrong website for your business?",
  "desc": "The \"Website\" button on your Google Maps listing goes to the wrong page or a stranger's site? Here's how to change it in your Google Business Profile.",
  "answer": "The \"Website\" button comes from your Google Business Profile. If it points to an old address, an expired domain or an unrelated site, change it in the profile. If you don't manage the profile yet, claim it first.",
  "body": """
<h2>1. Open your Business Profile</h2>
<p>Sign in to the Google account that manages your business, then search Google for your business name. Your profile appears with an <b>Edit profile</b> option.</p>

<h2>2. Change the website link</h2>
<p>Go to <b>Edit profile</b>, then <b>Contact</b>, and update <b>Website</b> to your correct address, starting with <code>https://</code>. Save. Google may review the change, so allow a few days.</p>

<h2>3. If you don't manage the profile</h2>
<p>On your Google Maps listing, look for <b>Own this business?</b> or <b>Claim this business</b> and follow the steps. Google verifies you by phone, email, video or postcard depending on the business.</p>

<h2>4. Check the other links too</h2>
<p>Menu, booking and appointment links can point to old pages as well. Check them while you're in the profile.</p>

<h2>5. If the wrong link keeps coming back</h2>
<p>Anyone can suggest edits to a listing. If yours keeps changing to someone else's site, keep the profile verified, review suggested edits, and report it to Google Business Profile support.</p>
""",
  "price": "$50",
  "fix": "I correct the link, check your menu and booking links, and make sure the page it points to actually loads.",
 },
 {
  "slug": "wix-site-not-showing-on-google",
  "title": "Wix site not showing on Google? How to get it listed",
  "h1": "Wix site not showing on Google?",
  "desc": "Your Wix website isn't showing up on Google? Check the indexing setting, hidden pages and your domain, then connect Google Search Console. Step by step.",
  "answer": "Usually one of three things: the site is set to stay out of search results, the pages you care about are individually hidden, or Google simply hasn't been told the site exists yet. Wix has settings for all three, and fixing them takes minutes. Google then needs days to a few weeks.",
  "body": """
<h2>1. Check the site-wide setting</h2>
<p>In your Wix dashboard, open the SEO settings and make sure <b>Let search engines index your site</b> is switched on. If it's off, nothing on the site can appear in Google.</p>

<h2>2. Check individual pages</h2>
<p>In the Wix editor, open each important page's SEO settings (Pages, then the page's settings, then SEO basics). Make sure it isn't set to be hidden from search results. Pages copied from a template are sometimes hidden by default.</p>

<h2>3. Make sure people can reach the site on your own domain</h2>
<p>Google lists the address it can actually reach. If your domain shows "This domain isn't connected to a site", fix that first (see the <a href="../wix-domain-not-connected/">Wix domain guide</a>). Also make sure the site is published.</p>

<h2>4. Tell Google about it</h2>
<p>Wix's SEO setup checklist can connect your site to Google Search Console for you. Once connected, use <b>URL Inspection</b> on your homepage and click <b>Request indexing</b>. Wix creates your sitemap automatically at <code>yourbusiness.com/sitemap.xml</code>, so submit that too.</p>

<h2>5. Give each page a clear title</h2>
<p>A page called "Home" with no description gives Google nothing to match. In each page's SEO settings, use a title that says what you do and where, for example "Plumber in Lakeland, FL | Smith Plumbing".</p>
""",
  "price": "$100-150",
  "fix": "I check every setting and page, connect Search Console, write clear page titles and descriptions, and request indexing.",
 },
 {
  "slug": "wordpress-site-redirecting-to-spam",
  "title": "WordPress site redirecting to spam? What to do (hacked site)",
  "h1": "WordPress site redirecting visitors to spam?",
  "desc": "Visitors to your WordPress site end up on spam, scam or gambling pages? It's been hacked. Here's how to confirm it, clean it, and ask Google to remove the warning.",
  "answer": "If visitors (often only some of them, or only from Google or phones) are sent to spam or scam pages, the site has been hacked, usually through an outdated plugin, theme or weak password. It needs cleaning, closing the hole, and then asking Google to clear any warning.",
  "body": """
<h2>1. Confirm it</h2>
<p>Many hacks only redirect some visitors, so the owner never sees it. Try opening the site from a Google search result, in a private window, and on a phone using mobile data. Search Console's <b>Security issues</b> report shows whether Google has flagged the site.</p>

<h2>2. Take a backup before touching anything</h2>
<p>Back up the files and database from your hosting panel. Even an infected backup helps if something goes wrong during the clean-up.</p>

<h2>3. Lock the door</h2>
<ul>
  <li>Change every password: hosting account, WordPress admin users, FTP or SFTP, and the database.</li>
  <li>In WordPress, go to Users and delete any administrator you don't recognise.</li>
  <li>Update WordPress, every plugin and every theme. Delete plugins and themes you don't use.</li>
</ul>

<h2>4. Find and remove the malicious code</h2>
<p>Run a security scanner plugin such as Wordfence or Sucuri. Common hiding places are the <code>.htaccess</code> file, <code>wp-config.php</code>, the active theme's files, and unfamiliar PHP files in the uploads folder. If you have a clean backup from before the hack, restoring it and then updating everything is often the quickest route.</p>

<h2>5. Ask Google to clear the warning</h2>
<p>Once the site is clean, open <b>Security issues</b> in Search Console and request a review. Warnings are usually removed within a few days of a successful review.</p>
""",
  "price": "a custom quote, usually $200-350",
  "fix": "I back up the site, remove the infection, close the hole it came through, update everything, and request Google's review.",
 },
 {
  "slug": "shopify-store-password-page",
  "title": "Shopify store stuck on the password page? How to open it",
  "h1": "Shopify store stuck on the \"Opening soon\" password page?",
  "desc": "Customers only see your Shopify password page? Here's how to remove store password protection, and why you can't until you pick a paid plan.",
  "answer": "Every new Shopify store starts behind a password page. You remove it in your Online Store preferences, but Shopify only lets you do that once you've chosen a paid plan. While the password is on, customers can't buy and Google can't list your products.",
  "body": """
<h2>1. Choose a plan</h2>
<p>If you're still on a free trial, Shopify won't let you remove the password. In your Shopify admin, go to Settings, then Plan, and choose a plan.</p>

<h2>2. Turn off password protection</h2>
<p>In your Shopify admin, open <b>Online Store</b>, then <b>Preferences</b>. Find <b>Password protection</b>, untick the box that restricts access to visitors with the password, and save.</p>

<h2>3. Check it from outside</h2>
<p>Open your store in a private browser window or on your phone. You should see your homepage, not the "Opening soon" page.</p>

<h2>4. Check the basics before customers arrive</h2>
<ul>
  <li>Your domain is connected and loads with the padlock (https).</li>
  <li>Payments and shipping rates are set up, and you've placed a test order.</li>
  <li>Your store's title and description in the Preferences page say what you sell.</li>
</ul>

<h2>5. Tell Google</h2>
<p>Shopify creates your sitemap at <code>yourstore.com/sitemap.xml</code>. Add the store to Google Search Console and submit it, so your products start appearing in search.</p>
""",
  "price": "$50-100",
  "fix": "I open the store, check the domain, payments and a test order, and get your sitemap to Google.",
 },
 {
  "slug": "website-500-internal-server-error",
  "title": "500 Internal Server Error on your website? How to fix it",
  "h1": "Website showing \"500 Internal Server Error\"?",
  "desc": "Your business website shows a 500 Internal Server Error? Here are the usual causes (a plugin, the .htaccess file, PHP memory or version) and how to fix each one.",
  "answer": "A 500 error means the server hit a problem it couldn't explain to the browser. On small business sites it's usually a recent change: a plugin or theme update, a broken .htaccess file, PHP running out of memory, or the host changing the PHP version.",
  "body": """
<h2>1. Think about what changed</h2>
<p>Did anything update or change in the last day or two? A plugin, theme, WordPress itself, or a setting at your host? The most recent change is the most likely cause.</p>

<h2>2. Read the error log</h2>
<p>Your hosting control panel has an <b>Errors</b> or <b>Error log</b> section. The newest lines usually name the file or plugin that failed, which saves a lot of guessing.</p>

<h2>3. WordPress: switch off the plugins</h2>
<p>Using your host's File Manager or FTP, rename the folder <code>wp-content/plugins</code> to <code>plugins-off</code>. If the site comes back, a plugin was the cause. Rename the folder back, then switch plugins on one at a time in the dashboard until the error returns.</p>

<h2>4. Check the .htaccess file</h2>
<p>Rename <code>.htaccess</code> in your site's main folder to <code>.htaccess-old</code>. If the site loads, the file was broken. In WordPress, go to Settings, then Permalinks, and click Save to create a fresh one.</p>

<h2>5. Memory and PHP version</h2>
<p>If the log mentions "memory exhausted", raise the PHP memory limit in your hosting panel. If the error started when your host upgraded PHP, switch back to the previous version temporarily, then update the plugin or theme that can't cope with the new one.</p>

<h2>6. Still broken?</h2>
<p>Contact your host's support with the time it started and the error log lines. Server-level problems are theirs to fix.</p>
""",
  "price": "$150-350",
  "fix": "I read the logs, find the cause, bring the site back online with a backup taken first, and stop it happening again.",
 },
 {
  "slug": "godaddy-website-ssl-not-working",
  "title": "GoDaddy website showing \"Not secure\"? How to fix SSL",
  "h1": "GoDaddy website showing \"Not secure\"?",
  "desc": "Your GoDaddy website shows \"Not secure\" or a certificate warning? How to check your SSL certificate, your domain settings and your plan, step by step.",
  "answer": "On GoDaddy the cause depends on what you use. A GoDaddy Website Builder site gets its certificate automatically once the domain points to it correctly. A GoDaddy hosting plan needs a certificate set up on the account, and some plans don't include one.",
  "body": """
<h2>1. Work out what you have</h2>
<p>In your GoDaddy account, open <b>My Products</b>. You'll see whether you have Website Builder (Websites + Marketing), web hosting such as cPanel, or only a domain with the website hosted somewhere else.</p>

<h2>2. Website Builder sites</h2>
<p>The certificate is issued automatically, but only when your domain points to the builder. If you still see a warning, check the domain's DNS settings: an old record pointing to previous hosting is the usual culprit. Fix the records, then allow a few hours.</p>

<h2>3. GoDaddy hosting (cPanel)</h2>
<p>Look for an <b>SSL Certificates</b> section in your account. If there's a certificate, check its status: "pending" usually means the domain isn't pointing to the hosting yet, and "expired" needs renewing. If your plan doesn't include one, you can buy one from GoDaddy or use a free certificate where your plan supports it.</p>

<h2>4. Domain at GoDaddy, website elsewhere</h2>
<p>The certificate comes from wherever the website is hosted, not from GoDaddy. Set it up with that host, and make sure GoDaddy's DNS records point to it.</p>

<h2>5. Cover both addresses and force https</h2>
<p>Make sure both <code>yourbusiness.com</code> and <code>www.yourbusiness.com</code> work with the padlock, and that plain http redirects to https. See the <a href="../website-not-secure-warning/">general "Not secure" guide</a> for more.</p>
""",
  "price": "$100-200",
  "fix": "I find out what's wrong on your GoDaddy account, set up a working certificate for both addresses, and send every visitor to the secure one.",
 },
 {
  "slug": "contact-form-not-sending-emails",
  "title": "Website contact form not sending emails? How to fix it",
  "h1": "Website contact form not sending emails?",
  "desc": "Customers fill in your website's contact form but the emails never arrive? Check spam, the recipient address and how the site sends mail. WordPress, Wix and Squarespace.",
  "answer": "Usually the messages are being sent but not delivered: they land in spam, go to an old email address, or get blocked because the website sends mail in a way inboxes don't trust. A proper sending setup (SMTP) fixes most WordPress cases.",
  "body": """
<h2>1. Send yourself a test</h2>
<p>Fill in the form yourself, then check your inbox and spam folder. Check the spam folder of every address the form might send to.</p>

<h2>2. Check where the form sends</h2>
<p>Open the form's settings and look at the notification or recipient email. It's often still set to the web designer's address, or an old staff mailbox.</p>

<h2>3. WordPress: send mail properly</h2>
<p>By default WordPress sends email straight from the web server, and many inboxes treat that as spam or reject it. Install an SMTP plugin such as WP Mail SMTP and connect it to your real email account (Google Workspace, Microsoft 365, or your email provider). Then send a test from the plugin's settings.</p>

<h2>4. Wix and Squarespace</h2>
<p>Check the form's settings for the address notifications go to, and look in the platform's own inbox or form submissions area: messages are usually stored there even when the email doesn't arrive.</p>

<h2>5. Fix your domain's email records</h2>
<p>If you send from an address on your own domain, your domain needs SPF and DKIM records so inboxes trust its mail. Your email provider lists the exact records to add at your domain company.</p>
""",
  "price": "$100-250",
  "fix": "I trace where the messages go, set up reliable sending, fix your domain's email records if needed, and test it end to end.",
 },
 {
  "slug": "domain-expired-website-down",
  "title": "Domain expired and website down? How to get it back fast",
  "h1": "Domain expired and your website (and email) stopped working?",
  "desc": "Your business domain expired and the website or email stopped working? How to check, renew it before it's gone, and make sure it never lapses again.",
  "answer": "When a domain expires, the website and any email on it stop working. Most registrars let the owner renew at the normal price for a short time after expiry, then charge a much higher restore fee, and eventually release the domain for anyone to buy. Act today.",
  "body": """
<h2>1. Confirm the domain has expired</h2>
<p>Look your domain up at <a href="https://lookup.icann.org" rel="noopener">lookup.icann.org</a>. It shows the expiry date and which company the domain is registered with (the registrar), such as GoDaddy, Namecheap or Squarespace.</p>

<h2>2. Log in to the registrar and renew</h2>
<p>Renew from the domain's page in your account. If it expired recently, renewal is usually at the normal price. The website and email come back once the renewal goes through, sometimes within minutes, sometimes a few hours.</p>

<h2>3. If you can't get into the registrar account</h2>
<p>This is common when a former web designer or employee registered the domain. Contact the registrar's support straight away and ask how to prove you own the business. Keep proof ready: business registration, invoices, and the domain's old contact details if you know them.</p>

<h2>4. If renewal now costs a lot more</h2>
<p>After the first grace period, registrars move domains into a "redemption" stage with a restore fee. It's often still worth paying: a new domain means new business cards, lost Google rankings, and missing emails.</p>

<h2>5. Make sure it never happens again</h2>
<ul>
  <li>Turn on <b>auto-renew</b> and renew for several years at once.</li>
  <li>Make sure the registrar's contact email is one you read, not an old employee's.</li>
  <li>Keep a card on file that won't expire soon.</li>
</ul>
""",
  "price": "$50-150 (plus the registrar's own renewal fee)",
  "fix": "I work out where the domain is and what it takes to recover it, handle the renewal steps with you, and check the website, email and Google listing all work again.",
 },
 {
  "slug": "wordpress-critical-error",
  "title": "WordPress \"There has been a critical error on this website\": how to fix it",
  "h1": "WordPress says \"There has been a critical error on this website\"?",
  "desc": "Your WordPress site shows \"There has been a critical error on this website\"? Use the recovery email, find the plugin or theme at fault, and get the site back. Step by step.",
  "answer": "This message means a plugin, theme or code change crashed WordPress. WordPress usually emails the site's admin address a link to log in using recovery mode, where you can switch off whatever caused it.",
  "body": """
<h2>1. Look for the recovery email</h2>
<p>Check the inbox of the site's admin email for a message titled "Your Site is Experiencing a Technical Issue". It names the plugin or theme at fault and includes a recovery mode link. Use the link to log in, then deactivate that plugin or switch theme.</p>

<h2>2. No email? Switch off the plugins</h2>
<p>Open your host's File Manager or connect by FTP. Rename the folder <code>wp-content/plugins</code> to <code>plugins-off</code>. If the site comes back, rename it back and switch plugins on one at a time in the dashboard until the error returns. That's your culprit.</p>

<h2>3. Check the theme</h2>
<p>If switching off plugins didn't help, rename your active theme's folder inside <code>wp-content/themes</code>. WordPress falls back to a default theme (such as Twenty Twenty-Four) if one is installed.</p>

<h2>4. Turn on the error log</h2>
<p>In <code>wp-config.php</code>, set <code>WP_DEBUG</code> and <code>WP_DEBUG_LOG</code> to <code>true</code>. Reload the site, then read <code>wp-content/debug.log</code>: the last lines name the file that failed. Turn debugging off again when you're done.</p>

<h2>5. Check the PHP version</h2>
<p>If the error started when your host upgraded PHP, an old plugin or theme may not support the new version. Switch back temporarily in your hosting panel, then update or replace the plugin.</p>
""",
  "price": "$150-350",
  "fix": "I find the failing plugin, theme or code, bring the site back with a backup taken first, and update or replace what broke.",
 },
 {
  "slug": "locked-out-of-wordpress-admin",
  "title": "Locked out of WordPress admin? How to get back in",
  "h1": "Locked out of your WordPress admin?",
  "desc": "Can't log in to WordPress: forgotten password, reset email not arriving, security plugin lockout or a login loop? How to get back into your dashboard safely.",
  "answer": "Start with the password reset link. If the reset email never arrives, you can reset the password from your hosting account instead. Security plugin lockouts and login loops can be cleared from the hosting side too.",
  "body": """
<h2>1. Use "Lost your password?"</h2>
<p>Go to <code>yourbusiness.com/wp-login.php</code> and click <b>Lost your password?</b>. Enter your username or email. Check spam if the email doesn't arrive within a few minutes.</p>

<h2>2. Reset email never arrives</h2>
<p>Your site may not be able to send email at all (see the <a href="../contact-form-not-sending-emails/">contact form guide</a>). Reset the password from your hosting account instead:</p>
<ul>
  <li>Many hosts have a WordPress manager with a "change admin password" or "log in to WordPress" button.</li>
  <li>Otherwise open <b>phpMyAdmin</b>, find the <code>wp_users</code> table (the prefix may differ), edit your user, and set <code>user_pass</code> to a new password using the <b>MD5</b> function. WordPress upgrades it to a stronger hash when you log in.</li>
</ul>

<h2>3. Locked out by a security plugin</h2>
<p>Too many failed attempts can block you. In File Manager or FTP, rename the security plugin's folder inside <code>wp-content/plugins</code> (for example <code>wordfence</code>), log in, rename it back and remove the block in its settings.</p>

<h2>4. Login page keeps reloading</h2>
<p>Clear your browser's cookies for the site, or try a private window. If it still loops, check that the <b>siteurl</b> and <b>home</b> values in the <code>wp_options</code> table both match your real address, including https and www.</p>

<h2>5. Once you're in</h2>
<p>Use a strong, unique password, remove admin accounts nobody uses, and add a second administrator you control, so one lost password can't lock the business out again.</p>
""",
  "price": "$100-200",
  "fix": "I get you back in through your hosting account, clear the lockout, fix whatever blocked the reset email, and tidy up your admin accounts.",
 },
 {
  "slug": "website-slow-to-load",
  "title": "Small business website slow to load? How to find and fix it",
  "h1": "Website slow to load?",
  "desc": "Your business website takes ages to load, especially on phones? How to measure it with PageSpeed Insights and fix the usual causes: big images, plugins, hosting and add-on scripts.",
  "answer": "Slow small business sites usually come down to a few things: huge photos, no caching, too many plugins or add-on scripts, and cheap overloaded hosting. Measure first, fix the biggest problem, then measure again.",
  "body": """
<h2>1. Measure it</h2>
<p>Run your homepage through <a href="https://pagespeed.web.dev" rel="noopener">PageSpeed Insights</a> and look at the <b>mobile</b> result. Note the load times and the list of "opportunities". Run it again after each fix to see what actually helped.</p>

<h2>2. Shrink the photos</h2>
<p>The most common problem: a phone photo of 5 MB or more shown in a 600-pixel box. Resize images to the size they're displayed, and save them as WebP or compressed JPEG. On WordPress, an image optimisation plugin can do this for existing images.</p>

<h2>3. Turn on caching</h2>
<p>Caching serves ready-made pages instead of building each one from scratch. Many hosts include it; on WordPress, use the caching plugin your host recommends (for example LiteSpeed Cache on LiteSpeed servers).</p>

<h2>4. Cut plugins and add-on scripts</h2>
<p>Every chat widget, tracking pixel, slider and social feed adds weight. Remove the ones nobody uses, and delete inactive WordPress plugins.</p>

<h2>5. Check the hosting and PHP version</h2>
<p>If the server itself takes over a second to respond, the hosting plan is the bottleneck. Updating to a current PHP version in your hosting panel is a free speed boost for WordPress sites.</p>
""",
  "price": "$200-350",
  "fix": "I measure the site, fix the biggest slowdowns first (images, caching, plugins, scripts), and show you before and after scores.",
 },
 {
  "slug": "website-not-mobile-friendly",
  "title": "Website not mobile-friendly? How to check and fix it",
  "h1": "Website doesn't work properly on phones?",
  "desc": "Customers have to pinch and zoom to read your website on a phone? How to check mobile-friendliness and fix it: viewport tag, responsive theme, text, buttons and pop-ups.",
  "answer": "Most visitors to small business websites are on phones. If yours shows a tiny desktop page, has text you must zoom to read, or buttons too small to tap, people leave. Older sites often just lack one line of code; others need a responsive theme.",
  "body": """
<h2>1. Check it like a customer</h2>
<p>Open your site on your own phone, without zooming. Can you read the text, tap the phone number, and find opening hours and the booking button? On a computer, Chrome's developer tools have a device mode that shows the same thing.</p>

<h2>2. The missing viewport tag</h2>
<p>View the page source and search for <code>viewport</code>. If there's no <code>&lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;</code> line, phones show the desktop page shrunk down. Adding it is the first step, though the layout may then need adjusting.</p>

<h2>3. Fixed-width layouts</h2>
<p>Sites built years ago often use fixed widths, such as a 960-pixel page. They need flexible widths and images that scale down. On WordPress, Wix or Squarespace, switching to a modern responsive theme or template solves most of it.</p>

<h2>4. Text, buttons and phone numbers</h2>
<p>Body text should be at least 16 pixels. Buttons and links need room to tap. Make your phone number a tap-to-call link.</p>

<h2>5. Pop-ups that cover the page</h2>
<p>Full-screen pop-ups and cookie banners that can't be closed on a phone stop people dead. Make sure each one has a visible close button.</p>
""",
  "price": "$250-500",
  "fix": "I make your existing site work on phones, keeping your content and look, and test it on real screen sizes.",
 },
 {
  "slug": "domain-not-pointing-to-new-website",
  "title": "Domain not showing your new website? How to fix DNS",
  "h1": "Moved to a new website but your domain still shows the old one (or nothing)?",
  "desc": "Changed web host or builder but your domain shows the old site, an error, or works only with or without www? How to check name servers, A and CNAME records, and keep your email working.",
  "answer": "Your domain's DNS settings decide where visitors go. After a move, they often still point to the old host, point to both, or only cover one of www or the plain domain. Changes can take up to 48 hours to reach everyone.",
  "body": """
<h2>1. Find out who controls your DNS</h2>
<p>Look up your domain at <a href="https://lookup.icann.org" rel="noopener">lookup.icann.org</a> and note the <b>name servers</b>. Those decide where you edit DNS. It may be your registrar, your old host, or a service such as Cloudflare.</p>

<h2>2. Enter exactly what the new host asks for</h2>
<p>Your new host or builder gives you either new name servers or specific records: usually an <b>A record</b> for the plain domain and a <b>CNAME</b> for www. Enter them where your DNS is controlled.</p>

<h2>3. Remove the old records</h2>
<p>A common mistake: leaving the old A record in place next to the new one. Visitors then land on the old site or the new one at random. Delete records that point to the old host.</p>

<h2>4. Cover both www and the plain domain</h2>
<p>Test <code>yourbusiness.com</code> and <code>www.yourbusiness.com</code>. Both should reach the new site, with one redirecting to the other, and both with the padlock.</p>

<h2>5. Don't break your email</h2>
<p>If you change name servers, your email records (<b>MX</b>, plus SPF and DKIM) must be recreated at the new DNS provider, or email stops. Copy them before switching.</p>

<h2>6. Give it time, then test from outside</h2>
<p>Allow a few hours, sometimes up to 48. A public DNS checker website shows what different parts of the world see, which is more reliable than your own browser's cache.</p>
""",
  "price": "$50-150",
  "fix": "I point your domain at the new site, remove the old records, make both www and the plain domain work securely, and keep your email running.",
 },
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="name" href="../"><b>Alex Mugo</b><span>website repairs</span></a>
    <nav>
      <a class="hide-sm" href="../#prices">Prices</a>
      <a class="hide-sm" href="../#guides">Guides</a>
      <a class="btn solid" href="../#check">Get a free check</a>
    </nav>
  </header>
  <main class="article">
    <a class="crumb" href="../#guides">Guides</a>
    <h1>{h1}</h1>
    <p class="answer">{answer}</p>
{body}
    <div class="cta">
      <h2>Rather I just fix it?</h2>
      <p>{fix} Fixed price {price}, agreed first, and you pay when it works.</p>
      <a class="btn solid" href="../#check">Get a free check</a>
    </div>
    <div class="related"><b>Other guides</b>
{related}
    </div>
  </main>
  <footer>
    <span>Alex Mugo Ndungu, website repairs for small businesses</span>
    <span><a href="mailto:mugo.ndung@gmail.com">mugo.ndung@gmail.com</a></span>
  </footer>
</div>
</body>
</html>
"""

for g in GUIDES:
    url = BASE + g["slug"] + "/"
    ld = {
      "@context": "https://schema.org",
      "@graph": [
        {"@type": "Article", "headline": g["title"], "description": g["desc"], "url": url,
         "datePublished": TODAY, "dateModified": TODAY,
         "author": {"@type": "Person", "name": "Alex Mugo Ndungu", "url": BASE},
         "publisher": {"@type": "Person", "name": "Alex Mugo Ndungu"}},
        {"@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Website repair", "item": BASE},
          {"@type": "ListItem", "position": 2, "name": g["h1"], "item": url}]}
      ]}
    i = GUIDES.index(g)
    picks = [GUIDES[(i + k) % len(GUIDES)] for k in range(1, 7)]
    related = "\n".join(f'      <a href="../{o["slug"]}/">{html.escape(o["h1"])}</a>' for o in picks) + \
              '\n      <a href="../#guides">All guides</a>'
    page = HEAD.format(title=html.escape(g["title"]), desc=html.escape(g["desc"]), url=url,
                       ld=json.dumps(ld, indent=2), h1=html.escape(g["h1"]), answer=html.escape(g["answer"]),
                       body=g["body"], fix=html.escape(g["fix"]), price=g["price"], related=related)
    d = os.path.join(SITE, g["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page)
    print("wrote", g["slug"])

# sitemap
urls = [BASE] + [BASE + g["slug"] + "/" for g in GUIDES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8").write(sm)
print("wrote sitemap.xml with", len(urls), "urls")
