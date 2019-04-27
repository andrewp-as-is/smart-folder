<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/smart-folder.svg?maxAge=3600)](https://pypi.org/project/smart-folder/)
[![](https://img.shields.io/npm/v/smart-folder.svg?maxAge=3600)](https://www.npmjs.com/package/smart-folder)
[![Travis](https://api.travis-ci.org/looking-for-a-job/smart-folder.svg?branch=master)](https://travis-ci.org/looking-for-a-job/smart-folder/)

#### Installation
```bash
$ [sudo] npm i -g smart-folder
```
```bash
$ [sudo] pip install smart-folder
```

#### Benefits
+   organize a large number of repositories using `smart-folder`

#### How it works
targets|`folder`
-|-
`path/to/<repo1>`|`<folder>/<repo1 symlink>`
`path/to/<repo2>`|`<folder>/<repo2 symlink>`

#### Scripts usage
```bash
usage: smart-folder folder target ...
```

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
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>