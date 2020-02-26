# AUR Audit

Anyone can push a package to the Arch User Repository. So, it's a good idea to audit AUR package contents before installing.

Many AUR package managers such as `yaourt` and `yay` give you an option to edit the PKGBUILDs before continuing to installation. If you use this feature like me, you hardly ever edit them, and simply need to quickly skim the code to make sure there's nothing suss.

Ever wish there was a tool to let you quickly skim ALL code (not just the package build scripts) in the AUR build directory for that package?

Enter `aur-audit`.

Simply install `bat`, install `aur-audit`, and configure your AUR package manager to use `aur-audit` instead of whatever it was using before (`vim`, `nano`, etc).

Easy!

Available as a [package from the AUR repo](https://aur.archlinux.org/packages/aur-audit-git/).
