#!/usr/bin/env python3
"""
Setup script to create database with SEO fields
"""

from app import app, db, init_db

def setup_database():
    """Create database with all tables including SEO fields"""
    
    print("🔧 Setting up database with SEO fields...")
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Create admin user if it doesn't exist
        from models import User
        
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@thelinkindeen.com',
                is_admin=True,
                is_approved=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin user created: username=admin, password=admin123")
        else:
            print("ℹ️  Admin user already exists")
        
        print("✅ Database setup completed!")
        print("🎯 You can now:")
        print("   1. Start the Flask app: python app.py")
        print("   2. Access admin panel with the secure path")
        print("   3. Create posts/pages with SEO features")

if __name__ == "__main__":
    setup_database() 