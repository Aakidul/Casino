#!/bin/bash

# Function to check if Python 3 is installed
check_python3() {
    if command -v python3 &>/dev/null; then
        echo "Python 3 is installed."
        return 0
    else
        echo "Python 3 is not installed."
        return 1
    fi
}

# Function to check if a Python package is installed
check_package() {
    local package=$1
    python3 -c "import $package" &>/dev/null
}

# Function to prompt user for installation
prompt_install() {
    read -p "Do you want to install the missing packages? (y/yes/n/no): " choice
    case "$choice" in
        y|yes)
            install_packages
            ;;
        n|no)
            echo "Exiting script."
            exit 1
            ;;
        *)
            echo "Invalid choice. Exiting script."
            exit 1
            ;;
    esac
}

# Function to install missing packages
install_packages() {
    echo "Installing required packages..."
    pip install -q random os time json
    echo "Installation complete."
}

# Main script
check_python3
if [ $? -eq 0 ]; then
    for pkg in random os time json; do
        if ! check_package $pkg; then
            echo "$pkg is not installed."
            prompt_install
            break
        else
            echo "$pkg is installed."
        fi
    done
else
    echo "Please install Python 3 to proceed."
    exit 1
fi
