from dataclasses import dataclass, field, asdict
from .propertyStatement import PropertyStatement
from csv import DictReader
import pprint


@dataclass
class AP:
    """Data to define an Application Profile."""

    propertyStatements: list = field(default_factory=list)
    namespaces: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    shapeInfo: dict = field(default_factory=dict)

    def add_namespace(self, ns, uri):
        """Adds (over-writes) the ns: URI, key value pair to the namespaces dict."""
        if (type(ns) == str) and (type(uri) == str):
            self.namespaces[ns] = uri
        else:
            msg = "Both ns and URI must be strings."
            raise TypeError(msg)
        return

    def add_metadata(self, prop, value):
        """Adds (over-writes) the ns: URI, key value pair to the namespaces dict."""
        if (type(prop) == str) and (type(value) == str):
            self.metadata[prop] = value
        else:
            msg = "Both ns and URI must be strings."
            raise TypeError(msg)
        return

    def add_shapeInfo(self, sh, value):
        """Adds (over-writes) the shape info to the shape dict."""
        if (type(sh) == str) and (type(value) == dict):
            self.shapeInfo[sh] = value
        elif type(value) != dict:
            msg = "Shape info must be a dictionary."
            raise TypeError(msg)
        return

    def add_propertyStatement(self, ps):
        """Adds PropertyStatement object to the list of property statements."""
        if ps in self.propertyStatements:
            pass
        elif type(ps) == PropertyStatement:
            self.propertyStatements.append(ps)
        else:
            msg = "Statement must be of PropertyStatement type."
            raise TypeError(msg)

    def load_namespaces(self, fname):
        """Load namespaces from a (csv) file."""
        # could add options for loading from other formats
        with open(fname, "r") as csv_file:
            csvReader = DictReader(csv_file)
            for row in csvReader:
                if row["prefix"] and row["URI"]:
                    self.add_namespace(row["prefix"], row["URI"])
                else:  # pass rows with missing data
                    pass

    def dump(self):
        """Print all the AP data."""
        pp = pprint.PrettyPrinter(indent=2)
        print("\n\n=== Metadata ===")
        pp.pprint(self.metadata)
        print("\n\n=== Namespaces ===")
        pp.pprint(self.namespaces)
        print("\n\n=== Shapes ===")
        pp.pprint(self.shapeInfo)
        print("\n\n=== propertyStatements ===")
        pp.pprint(self.propertyStatements)
        return


from dataclasses import dataclass, field, asdict
from .propertyStatement import PropertyStatement
from csv import DictReader
import pprint


@dataclass
class AP:
    """Data to define an Application Profile."""

    propertyStatements: list = field(default_factory=list)
    namespaces: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    shapeInfo: dict = field(default_factory=dict)

    def add_namespace(self, ns, uri):
        """Adds (over-writes) the ns: URI, key value pair to the namespaces dict."""
        if (type(ns) == str) and (type(uri) == str):
            self.namespaces[ns] = uri
        else:
            msg = "Both ns and URI must be strings."
            raise TypeError(msg)
        return

    def add_metadata(self, prop, value):
        """Adds (over-writes) the ns: URI, key value pair to the namespaces dict."""
        if (type(prop) == str) and (type(value) == str):
            self.metadata[prop] = value
        else:
            msg = "Both ns and URI must be strings."
            raise TypeError(msg)
        return

    def add_shapeInfo(self, sh, value):
        """Adds (over-writes) the shape info to the shape dict."""
        if (type(sh) == str) and (type(value) == dict):
            self.shapeInfo[sh] = value
        elif type(value) != dict:
            msg = "Shape info must be a dictionary."
            raise TypeError(msg)
        return

    def add_propertyStatement(self, ps):
        """Adds PropertyStatement object to the list of property statements."""
        if ps in self.propertyStatements:
            pass
        elif type(ps) == PropertyStatement:
            self.propertyStatements.append(ps)
        else:
            msg = "Statement must be of PropertyStatement type."
            raise TypeError(msg)

    def load_namespaces(self, fname):
        """Load namespaces from a (csv) file."""
        # could add options for loading from other formats
        with open(fname, "r") as csv_file:
            csvReader = DictReader(csv_file)
            for row in csvReader:
                if row["prefix"] and row["URI"]:
                    self.add_namespace(row["prefix"], row["URI"])
                else:  # pass rows with missing data
                    pass

    def dump(self):
        """Print all the AP data."""
        pp = pprint.PrettyPrinter(indent=2)
        print("\n\n=== Metadata ===")
        pp.pprint(self.metadata)
        print("\n\n=== Namespaces ===")
        pp.pprint(self.namespaces)
        print("\n\n=== Shapes ===")
        pp.pprint(self.shapeInfo)
        print("\n\n=== propertyStatements ===")
        pp.pprint(self.propertyStatements)
        return
