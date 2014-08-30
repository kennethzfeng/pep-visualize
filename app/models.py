"""Application Models"""

import os


class PEP(object):
    LINE_READ_COUNT = 20
    def __init__(self, pep_text):
        self.pep_text = pep_text

    @classmethod
    def load_pep(cls, pep_number, directory):
        if not os.path.isdir(directory):
            raise ValueError('Unexpected directory value: %s' % directory)
        path = os.path.join(directory, 'pep-%04d.txt' % pep_number)
        with open(path, 'rb') as f:
            data = f.read()
        return PEP(data)

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

        if 'Title' in self.metadata_dict:
            self.title = self.metadata_dict['Title']

        if 'PEP' in self.metadata_dict:
            self.number = self.metadata_dict['PEP']

        if 'Author' in self.metadata_dict:
            author_string = self.metadata_dict['Author']
            self.authors = [x.strip() for x in author_string.split(',')]

        if 'Type' in self.metadata_dict:
            self.type = self.metadata_dict['Type']

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
