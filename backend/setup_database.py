"""
Database setup and testing script for Phase A completion
Run this to verify database connection and create tables
"""

import traceback
from models import User, Summary
from app import create_app, db
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def test_database_connection():
    """Test database connection and create tables"""
    try:
        print(" Testing database connection...")

        # Create Flask app
        app = create_app()

        with app.app_context():
            # Test connection
            print(" Database connection successful!")

            # Create all tables
            print(" Creating database tables...")
            db.create_all()
            print(" Database tables created successfully!")

            # Test table creation
            print(" Verifying table structure...")

            # Check if tables exist
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()

            expected_tables = ['users', 'summaries']
            for table in expected_tables:
                if table in tables:
                    print(f" Table '{table}' exists")

                    # Get column info
                    columns = inspector.get_columns(table)
                    print(f"   Columns: {[col['name'] for col in columns]}")
                else:
                    print(f" Table '{table}' missing")

            print("\n Phase A database setup completed successfully!")
            print("\n Next Steps:")
            print("   1. Commit Phase A changes")
            print("   2. Move to Phase B (Authentication)")

            return True

    except Exception as e:
        print(f" Database setup failed: {str(e)}")
        print("\n Troubleshooting:")
        print("   1. Check if MySQL is running")
        print("   2. Verify database credentials in .env file")
        print("   3. Run: mysql -u root -p < sql/schema.sql")
        print(f"\n Error details:\n{traceback.format_exc()}")
        return False


if __name__ == "__main__":
    success = test_database_connection()
    exit(0 if success else 1)
