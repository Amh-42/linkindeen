#!/usr/bin/env python3
"""
Database migration script to add SEO fields to existing posts and pages.
Run this script after updating the models.py file to add the new SEO fields.
"""

import sqlite3
import os
from datetime import datetime

def migrate_database():
    """Add SEO fields to existing database"""
    
    # Database file path
    db_path = 'instance/LinkinDeen.db'
    
    if not os.path.exists(db_path):
        print(f"Database file {db_path} not found!")
        return
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("🔧 Starting SEO fields migration...")
    
    try:
        # Check if SEO fields already exist
        cursor.execute("PRAGMA table_info(post)")
        post_columns = [column[1] for column in cursor.fetchall()]
        
        cursor.execute("PRAGMA table_info(page)")
        page_columns = [column[1] for column in cursor.fetchall()]
        
        # Add SEO fields to Post table if they don't exist
        if 'focus_keyword' not in post_columns:
            print("➕ Adding SEO fields to Post table...")
            cursor.execute("ALTER TABLE post ADD COLUMN focus_keyword VARCHAR(100)")
            cursor.execute("ALTER TABLE post ADD COLUMN meta_description TEXT")
            cursor.execute("ALTER TABLE post ADD COLUMN meta_keywords VARCHAR(255)")
            cursor.execute("ALTER TABLE post ADD COLUMN secondary_keywords TEXT")
            cursor.execute("ALTER TABLE post ADD COLUMN canonical_url VARCHAR(255)")
            print("✅ SEO fields added to Post table")
        else:
            print("ℹ️  SEO fields already exist in Post table")
        
        # Add SEO fields to Page table if they don't exist
        if 'focus_keyword' not in page_columns:
            print("➕ Adding SEO fields to Page table...")
            cursor.execute("ALTER TABLE page ADD COLUMN focus_keyword VARCHAR(100)")
            cursor.execute("ALTER TABLE page ADD COLUMN meta_description TEXT")
            cursor.execute("ALTER TABLE page ADD COLUMN meta_keywords VARCHAR(255)")
            cursor.execute("ALTER TABLE page ADD COLUMN secondary_keywords TEXT")
            cursor.execute("ALTER TABLE page ADD COLUMN canonical_url VARCHAR(255)")
            print("✅ SEO fields added to Page table")
        else:
            print("ℹ️  SEO fields already exist in Page table")
        
        # Commit changes
        conn.commit()
        
        # Show current data
        cursor.execute("SELECT COUNT(*) FROM post")
        post_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM page")
        page_count = cursor.fetchone()[0]
        
        print(f"\n📊 Migration Summary:")
        print(f"   • Posts in database: {post_count}")
        print(f"   • Pages in database: {page_count}")
        print(f"   • SEO fields added successfully")
        
        print(f"\n🎯 Next Steps:")
        print(f"   1. Restart your Flask application")
        print(f"   2. Access the admin panel to edit posts/pages")
        print(f"   3. Add SEO data to your existing content")
        print(f"   4. Use the new SEO analysis features")
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        conn.rollback()
    finally:
        conn.close()

def show_current_data():
    """Show current posts and pages data"""
    
    db_path = 'instance/LinkinDeen.db'
    if not os.path.exists(db_path):
        print(f"Database file {db_path} not found!")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("\n📋 Current Database Content:")
    
    # Show posts
    cursor.execute("SELECT id, title, status FROM post ORDER BY created_at DESC LIMIT 5")
    posts = cursor.fetchall()
    
    if posts:
        print("\n📝 Recent Posts:")
        for post in posts:
            print(f"   • ID {post[0]}: {post[1]} ({post[2]})")
    else:
        print("\n📝 No posts found")
    
    # Show pages
    cursor.execute("SELECT id, title, status FROM page ORDER BY created_at DESC LIMIT 5")
    pages = cursor.fetchall()
    
    if pages:
        print("\n📄 Recent Pages:")
        for page in pages:
            print(f"   • ID {page[0]}: {page[1]} ({page[2]})")
    else:
        print("\n📄 No pages found")
    
    conn.close()

if __name__ == "__main__":
    print("=" * 60)
    print("SEO FIELDS MIGRATION SCRIPT")
    print("=" * 60)
    
    migrate_database()
    show_current_data()
    
    print("\n" + "=" * 60)
    print("Migration completed!")
    print("=" * 60) 