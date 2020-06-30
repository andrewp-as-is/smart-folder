<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/smart-folder.svg?maxAge=3600)](https://pypi.org/project/smart-folder/)
[![](https://img.shields.io/npm/v/smart-folder.svg?maxAge=3600)](https://www.npmjs.com/package/smart-folder)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/smart-folder/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/smart-folder/actions)

### Installation
```bash
$ [sudo] pip install smart-folder
```

```bash
$ [sudo] npm i -g smart-folder
```

#### How it works
targets|`folder`
-|-
`path/to/<repo1>`|`<folder>/<repo1 symlink>`
`path/to/<repo2>`|`<folder>/<repo2 symlink>`

#### Examples
`find`
```bash
$ find ~/git -type d -name "*.py" -mindepth 1 -maxdepth 1 | xargs smart-folder "py"
```

macOS `mdfind`
```bash
$ mdfind "kMDItemUserTags == py" -0 | xargs -0 smart-folder "py"
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>