import asyncio
import aiohttp
import sys

async def check_domain(session, domain):
    url = f"http://{domain}"
    try:
        async with session.head(url, timeout=3) as response:
            if response.status < 400:
                print(f"[+] FOUND: {url} (Status: {response.status})")
    except Exception:
        pass

async def main(target, wordlist_file):
    print(f"[*] Starting reconnaissance on: {target}")
    try:
        with open(wordlist_file, 'r') as f:
            subdomains = [line.strip() for line in f]
    except FileNotFoundError:
        print("[!] Error: Wordlist file not found.")
        return

    full_domains = [f"{sub}.{target}" for sub in subdomains]

    async with aiohttp.ClientSession() as session:
        tasks = [check_domain(session, domain) for domain in full_domains]
        await asyncio.gather(*tasks)

    print("-" * 50)
    print("[!] Scan Completed.")
    print("[+] Need more power? Unlock the full Elite Recon Engine:")
    print("[+] https://gumroad.com/baranavi")
    print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <target_domain> <wordlist_file>")
    else:
        asyncio.run(main(sys.argv[1], sys.argv[2]))