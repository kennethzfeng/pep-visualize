"""Application Models"""


class PEP(object):
    LINE_READ_COUNT = 20

    def __init__(self, pep_text):
        self.pep_text = pep_text

    def parse_metadata(self):
        lines = self.pep_text.splitlines()

        self.metadata_dict = {}
        caches = []
        for line in lines[:20]:
            if len(line) > 1 and line[-1] == ',':
                caches.append(line)
                continue
            else:
                caches.append(line)
                combined = ''.join(caches)
                caches = []
                parts = combined.split(':')
                if len(parts) == 2:
                    self.metadata_dict[parts[0]] = parts[1].strip()

        self._parse_title()
        self._parse_pep()
        self._parse_authors()
        self._parse_type()
        self._parse_status()


        self.pep_content = '\n\n\n'.join(self.pep_text.split('\n\n\n')[1:])

    def _parse_title(self):
        """Parse for Title"""
        if 'Title' in self.metadata_dict:
            self.title = self.metadata_dict['Title']

    def _parse_pep(self):
        if 'PEP' in self.metadata_dict:
            self.number = self.metadata_dict['PEP']

    def _parse_authors(self):
        if 'Author' in self.metadata_dict:
            author_string = self.metadata_dict['Author']
            self.authors = [x.strip() for x in author_string.split(',')]

    def _parse_type(self):
        if 'Type' in self.metadata_dict:
            self.type = self.metadata_dict['Type']

    def _parse_status(self):
        if 'Status' in self.metadata_dict:
            self.status = self.metadata_dict['Status']

    def to_dict(self):
        return {
            'title': self.title,
            'number': self.number,
            'authors': self.authors,
            'type': self.type,
            'status': self.status
        }
