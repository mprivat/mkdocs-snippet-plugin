from mkdocs.plugins import BasePlugin

from jinja2 import Template
from git import Repo
import uuid
import shutil
import re
import os
import mkdocs
import sys


class SnippetPlugin(BasePlugin):

    if sys.version_info[0] == 3:
        string_types = str
    else:
        string_types = basestring

    config_scheme = (('base_path',
                      mkdocs.config.config_options.Type(
                          string_types, default=None)), )

    page = None

    def copy_markdown_images(self, tmpRoot, markdown):
        # root = os.path.dirname(os.path.dirname(self.page.url))
        root = self.page.url

        paths = []

        p = re.compile("!\[.*\]\((.*)\)")
        it = p.finditer(markdown)
        for match in it:
            path = match.group(1)
            paths.append(path)

            destinationPath = os.path.realpath(self.config['base_path'] + "/" +
                                               root + "/gen_/" + path)

            if not os.path.isfile(destinationPath):
                print("Copying image: " + path + " to " + destinationPath)

                os.makedirs(os.path.dirname(destinationPath), exist_ok=True)
                shutil.copyfile(tmpRoot + "/" + path, destinationPath)

        for path in paths:
            markdown = markdown.replace(path, "gen_/" + path)

        return markdown

    def markdown_snippet(self, git_url, file_path, section_name):
        p = re.compile("^#+ ")
        m = p.search(section_name)
        if m:
            section_level = m.span()[1] - 1

            id = uuid.uuid4().hex
            root = "/tmp/" + id
            Repo.clone_from(git_url, root)

            content = ""
            with open(root + '/' + file_path, 'r') as myfile:
                content = myfile.read()

            p = re.compile("^" + section_name + "$", re.MULTILINE)
            start = p.search(content)
            start_index = start.span()[1]

            p = re.compile("^#{1," + str(section_level) + "} ", re.MULTILINE)

            result = ""
            end = p.search(content[start_index:])
            if end:
                end_index = end.span()[0]
                result = content[start_index:end_index + start_index]
            else:
                result = content[start_index:]

            # If there are any images, find them, copy them
            result = self.copy_markdown_images(root, result)

            shutil.rmtree(root)
            return result
        else:
            return "Markdown section doesn't exist in source"

    def snippet(self, git_url, file_path, section_name):
        if file_path.endswith('.md'):
            return self.markdown_snippet(git_url, file_path, section_name)
        else:
            return "File format not supported"

    def on_page_markdown(self, markdown, page, config, **kwargs):
        self.page = page
        md_template = Template(markdown)
        return md_template.render(snippet=self.snippet)
