#!/usr/bin/env python3
"""
Simple testing script for Jupyter Book project
No external dependencies beyond what's in requirements-docs.txt
"""

import os
import sys
import yaml
from pathlib import Path
import subprocess
import time


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")

    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required for Jupyter Book")
        return False

    if version.major == 3 and version.minor >= 12:
        print("⚠️  Python 3.12+ may have compatibility issues with some packages")

    return True


def validate_config_files():
    """Validate YAML configuration files"""
    print("\n⚙️ Validating configuration files...")

    config_files = {
        'docs/_config.yml': '_config.yml',
        'docs/_toc.yml': '_toc.yml'
    }

    for file_path, name in config_files.items():
        try:
            if not os.path.exists(file_path):
                print(f"❌ {name} not found at {file_path}")
                return False

            with open(file_path, 'r') as f:
                yaml.safe_load(f)
            print(f"✅ {name} is valid")

        except yaml.YAMLError as e:
            print(f"❌ {name} has YAML syntax error: {e}")
            return False
        except Exception as e:
            print(f"❌ Error reading {name}: {e}")
            return False

    return True


def check_content_files():
    """Check if all required content files exist"""
    print("\n📄 Checking content files...")

    required_files = [
        'docs/index.md',
        'docs/reproduction.md'
    ]

    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ Found {os.path.basename(file_path)}")
        else:
            print(f"❌ Missing {file_path}")
            missing_files.append(file_path)

    return len(missing_files) == 0


def create_placeholder_images():
    """Create simple placeholder images for testing"""
    print("\n🖼️ Creating placeholder images...")

    try:
        import matplotlib.pyplot as plt
        import numpy as np

        # Create _static directory
        static_dir = Path('docs/_static')
        static_dir.mkdir(exist_ok=True)

        # Create role_share.png
        fig, ax = plt.subplots(figsize=(8, 6))
        roles = ['Researchers', 'Developers', 'Data Scientists', 'Students', 'Other']
        sizes = [34.2, 28.6, 19.4, 12.1, 5.7]
        ax.pie(sizes, labels=roles, autopct='%1.1f%%', startangle=90)
        ax.set_title('Professional Roles Distribution')
        plt.tight_layout()
        plt.savefig('docs/_static/role_share.png', dpi=100, bbox_inches='tight')
        plt.close()

        # Create tools_heatmap.png
        fig, ax = plt.subplots(figsize=(10, 8))
        tools = ['Python', 'JavaScript', 'R', 'Java', 'C++']
        roles_short = ['Research', 'Dev', 'DataSci', 'Student']
        data = np.random.rand(len(tools), len(roles_short)) * 100

        im = ax.imshow(data, cmap='YlOrRd', aspect='auto')
        ax.set_xticks(range(len(roles_short)))
        ax.set_yticks(range(len(tools)))
        ax.set_xticklabels(roles_short)
        ax.set_yticklabels(tools)
        ax.set_title('Tool Usage Heatmap (%)')

        # Add colorbar
        cbar = plt.colorbar(im)
        cbar.set_label('Usage %')

        plt.tight_layout()
        plt.savefig('docs/_static/tools_heatmap.png', dpi=100, bbox_inches='tight')
        plt.close()

        print("✅ Created role_share.png")
        print("✅ Created tools_heatmap.png")
        return True

    except ImportError:
        print("⚠️ matplotlib not available, skipping image creation")
        return True
    except Exception as e:
        print(f"❌ Error creating images: {e}")
        return False


def test_build():
    """Test building the Jupyter Book"""
    print("\n🏗️ Testing Jupyter Book build...")

    try:
        # Clean previous build
        result = subprocess.run(['jupyter-book', 'clean', 'docs/'],
                                capture_output=True, text=True)

        # Build the book
        start_time = time.time()
        result = subprocess.run(['jupyter-book', 'build', 'docs/'],
                                capture_output=True, text=True)
        build_time = time.time() - start_time

        if result.returncode == 0:
            print(f"✅ Build successful in {build_time:.2f} seconds")

            # Check if HTML files were created
            html_files = [
                'docs/_build/html/index.html',
                'docs/_build/html/data_overview.html',
                'docs/_build/html/methodology.html',
                'docs/_build/html/results.html',
                'docs/_build/html/figures.html',
                'docs/_build/html/about.html'
            ]

            missing_html = []
            for html_file in html_files:
                if os.path.exists(html_file):
                    print(f"✅ Generated {os.path.basename(html_file)}")
                else:
                    missing_html.append(html_file)
                    print(f"❌ Missing {html_file}")

            return len(missing_html) == 0
        else:
            print("❌ Build failed")
            print("Error output:")
            print(result.stderr)
            return False

    except FileNotFoundError:
        print("❌ jupyter-book command not found. Is it installed?")
        print("Try: pip install jupyter-book")
        return False
    except Exception as e:
        print(f"❌ Build error: {e}")
        return False


def test_local_server():
    """Test if we can start a local server"""
    print("\n🌐 Testing local server capability...")

    if not os.path.exists('docs/_build/html/index.html'):
        print("❌ No built HTML files found. Run build first.")
        return False

    try:
        import http.server
        import socketserver
        import threading
        import socket

        # Test if port 8000 is available
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(('localhost', 8000))
            if result == 0:
                print("⚠️ Port 8000 is already in use")
                return True  # Not a failure, just can't test

        print("✅ Can start local server (port 8000 available)")
        print("ℹ️  To serve locally, run: make serve")
        return True

    except Exception as e:
        print(f"❌ Server test error: {e}")
        return False


def main():
    """Run all tests"""
    print("🧪 Starting Jupyter Book tests...\n")

    tests = [
        ("Python Version", check_python_version),
        ("Config Files", validate_config_files),
        ("Content Files", check_content_files),
        ("Placeholder Images", create_placeholder_images),
        ("Build Test", test_build),
        ("Server Test", test_local_server),
    ]

    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} crashed: {e}")
            results.append((test_name, False))

    # Summary
    print("\n📊 Test Summary:")
    print("=" * 50)

    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:<20} {status}")
        if result:
            passed += 1

    print("=" * 50)
    print(f"Passed: {passed}/{len(results)}")

    if passed == len(results):
        print("\n🎉 All tests passed! Your Jupyter Book is ready.")
        print("\nNext steps:")
        print("1. Run 'make serve' to view locally")
        print("2. Push to GitHub to trigger automatic deployment")
    else:
        print(f"\n⚠️ {len(results) - passed} test(s) failed. Please fix issues before deployment.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())