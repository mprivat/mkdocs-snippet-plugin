# mkdocs-snippet-plugin

An mkdocs plugin that injects snippets from a file in a git repository.

## Installation

> **Note:** This package requires MkDocs version 0.17 or higher.

Install the package with pip:

```bash
pip install mkdocs-snippet-plugin
```

Enable the plugin in your `mkdocs.yml`:

```yaml
plugins:
    - snippet:
          base_path: docs
```

The `base_path` entry should point to the root of your documentation site, usually defaulted to `docs`.

## How to use it

If you have a markdown file in a remote Git repostory, and you want to extract a sections from it, add the following to your documentation markdown in mkdocs:

```
{{ snippet('git@github.com:mprivat/mkdocs-snippet-plugin.git', 'README.md', '## Installation') }}
```

It will download the file you specify from the Git URL, extract the section you ask for (including its subsections) and inject that into your mkdocs file at render time.

If the remote file has references to images, those will also be downloaded and placed in a `_gen` folder in the mkdocs hierarchy. You will probably want to include `**/gen_` in your `.gitignore` file so you don't put those into your git repository unless you want them there.
