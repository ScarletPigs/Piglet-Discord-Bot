class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        
    def __repr__(self):
        return f'<Event {self.name} - at {self.date}>'

    def to_dict(self):
        return {
            'name': self.name,
            'date': self.date,
            'location': self.location
        }

    @classmethod
    def from_dict(cls, event_dict):
        return cls(
            name=event_dict['name'],
            date=event_dict['date'],
            location=event_dict['location']
        )
