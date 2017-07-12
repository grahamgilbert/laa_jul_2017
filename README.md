# London Apple Admins

This is a demo setup to demonstrate a Flask app that serves as middleware to provide Hiera data to a Puppet Server from an inventory tool.

# Usage

## Prerequisites

You will need:

* A macOS Vagrant box
* Create a directory called `r10k_cache` in the root directory
* Copy the example `r10k.yaml` and `Vagrantfile` files and edit to suit your environment.
* Create a `ssh` directory with an SSH private key that has access to your `puppet_control` repository
