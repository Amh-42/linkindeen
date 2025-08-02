#!/usr/bin/env python3
"""
Generate a secure random admin path for LinkinDeen admin panel.
This script generates a random string to use as the admin route path.
"""

import secrets
import string
import os

def generate_secure_path(length=64):
    """Generate a secure random path string"""
    # Use a mix of letters, numbers, and some special characters
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    # Generate a secure admin path
    admin_path = generate_secure_path(64)
    
    print("=" * 60)
    print("SECURE ADMIN PATH GENERATOR")
    print("=" * 60)
    print(f"Generated admin path: {admin_path}")
    print()
    print("To use this path:")
    print("1. Set the environment variable:")
    print(f"   export ADMIN_PATH='{admin_path}'")
    print()
    print("2. Or add to your .env file:")
    print(f"   ADMIN_PATH={admin_path}")
    print()
    print("3. Your admin panel will be accessible at:")
    print(f"   https://yourdomain.com/{admin_path}")
    print()
    print("⚠️  IMPORTANT SECURITY NOTES:")
    print("- Keep this path secret and don't share it publicly")
    print("- Change this path regularly for better security")
    print("- Use HTTPS in production")
    print("- Consider using a reverse proxy with additional security")
    print("=" * 60)

if __name__ == "__main__":
    main() 