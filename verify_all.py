"""
Verification script to check all project components
"""
import os
import sys
import subprocess

def check_file_exists(filepath):
    """Check if a file exists"""
    exists = os.path.exists(filepath)
    status = "✓" if exists else "✗"
    print(f"{status} {filepath}")
    return exists

def check_python_syntax(filepath):
    """Check Python file for syntax errors"""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'py_compile', filepath],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✓ {filepath} - No syntax errors")
            return True
        else:
            print(f"✗ {filepath} - Syntax errors found")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"✗ {filepath} - Error checking: {str(e)}")
        return False

def main():
    print("=" * 70)
    print("AEROLEADS ASSIGNMENT - PROJECT VERIFICATION")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Project structure
    projects = {
        'LinkedIn Scraper': {
            'dir': 'linkedin_scraper',
            'files': ['scraper.py', 'requirements.txt', 'README.md', '.env.example']
        },
        'Autodialer App': {
            'dir': 'autodialer_app',
            'files': ['app.py', 'requirements.txt', 'README.md', '.env.example',
                     'templates/index.html']
        },
        'Blog Generator': {
            'dir': 'blog_generator',
            'files': ['app.py', 'requirements.txt', 'README.md', '.env.example',
                     'templates/blog_index.html', 'templates/blog_post.html',
                     'templates/blog_admin.html']
        }
    }
    
    all_checks_passed = True
    
    for project_name, config in projects.items():
        print(f"\n{project_name}")
        print("-" * 70)
        
        project_dir = os.path.join(base_dir, config['dir'])
        
        # Check files exist
        for filename in config['files']:
            filepath = os.path.join(project_dir, filename)
            if not check_file_exists(filepath):
                all_checks_passed = False
        
        # Check Python files for syntax
        for filename in config['files']:
            if filename.endswith('.py'):
                filepath = os.path.join(project_dir, filename)
                if os.path.exists(filepath):
                    if not check_python_syntax(filepath):
                        all_checks_passed = False
    
    # Check documentation
    print(f"\nDocumentation")
    print("-" * 70)
    docs = ['README.md', 'SETUP_GUIDE.md', 'DEPLOYMENT_GUIDE.md', 'PROJECT_SUMMARY.md']
    for doc in docs:
        filepath = os.path.join(base_dir, doc)
        if not check_file_exists(filepath):
            all_checks_passed = False
    
    print("\n" + "=" * 70)
    if all_checks_passed:
        print("✓ ALL VERIFICATION CHECKS PASSED")
        print("All projects are ready for deployment!")
    else:
        print("✗ SOME CHECKS FAILED")
        print("Please review the errors above")
    print("=" * 70)
    
    return 0 if all_checks_passed else 1

if __name__ == '__main__':
    sys.exit(main())
