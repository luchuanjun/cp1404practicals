class Band:
    """Class to represent a musical band."""

    def __init__(self, name, members=None):
        """Initialise band with name and optional list of members."""
        self.name = name
        self.members = members if members is not None else []

    def add_member(self, member_name):
        """Add a member to the band."""
        if member_name not in self.members:
            self.members.append(member_name)

    def remove_member(self, member_name):
        """Remove a member from the band if present."""
        if member_name in self.members:
            self.members.remove(member_name)

    def __str__(self):
        """Return string representation of the band."""
        members_str = ", ".join(self.members) if self.members else "No members"
        return f"Band: {self.name}, Members: {members_str}"


if __name__ == "__main__":
    band = Band("The Rockers", ["Alice", "Bob"])
    band.add_member("Charlie")
    band.remove_member("Bob")
    print(band)
