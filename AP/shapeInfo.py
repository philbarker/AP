from dataclasses import dataclass, field, asdict


@dataclass
class ShapeInfo:
    """Data with information about a shape."""
    id: str = ""
    label: dict = field(default_factory=dict)
    comment: dict = field(default_factory=dict)
    targets: list = field(default_factory=dict)
    closed: bool = False
    ignoreProps: list = field(default_factory=list)
    mandatory: bool = False
    severity: str = ""
    note: dict = field(default_factory=dict)

    def set_id(self, id):
        """Set the value of shapeID to be the id."""

        if type(id) == str:
            self.id = id
        else:
            msg = "Shape identifier must be a string."
            raise TypeError(msg)

    def add_label(self, lang, label):
        """Add {lang: label} to label dict."""

        if (type(lang) == str) and (type(label) == str):
            self.label[lang] = label
        else:
            msg = "Language identifier and label must be strings."
            raise TypeError(msg)

    def add_comment(self, lang, label):
        """Add {lang: label} to comments dict."""

        if (type(lang) == str) and (type(label) == str):
            self.comment[lang] = label
        else:
            msg = "Language identifier and comment must be strings."
            raise TypeError(msg)

    def append_target(self, target, target_type):
        """Append {target_type: target} to targets dict."""
        #FIXME: need list of targets for each type.
        known_types = ["class", "instance", "objectsof", "subjectsof"]
        if (type(target) == str) and (type(target_type) == str):
            if target_type.lower() in known_types:
                self.targets[target_type.lower()] = target
            else:
                self.targets[target_type] = target
                msg = "Warning, ", target_type, " is unknown."
                print(msg)
        else:
            msg = "Target and type must be strings."
            raise TypeError(msg)

    def set_closed(self, isClosed):
        """Set boolean value of closed to value of isClosed"""
        if type(isClosed) == bool:
            self.closed = isClosed
        else :
            msg = "Value must be a boolean, True or False."
            raise TypeError(msg)

    def append_ignoreProps(self, prop):
        if type(prop) == str:
            self.ignoreProps.append(prop)
        else:
            msg = "Property id must be a string."
            raise TypeError(msg)

    def set_mandatory(self, isMandatory):
        """Set boolean value of closed to value of isClosed"""
        if type(isMandatory) == bool:
            self.mandatory = isMandatory
        else :
            msg = "Value must be a boolean, True or False."
            raise TypeError(msg)

    def set_severity(self, severity):
        """Append {target_type: target} to targets dict."""
        #FIXME: need list of targets for each type.
        known_vals = ["warning", "info", "violation", ""]
        if (type(severity) == str):
            if severity.lower() in known_vals:
                self.severity = severity.lower()
            else:
                self.severity = severity.lower()
                msg = "Warning, severity", severity, " is unknown."
                print(msg)
        else:
            msg = "Severity must be a string."
            raise TypeError(msg)

    def add_note(self, lang, note):
        """Add {lang: label} to note dict."""

        if (type(lang) == str) and (type(note) == str):
            self.note[lang] = note
        else:
            msg = "Language identifier and note must be strings."
            raise TypeError(msg)
