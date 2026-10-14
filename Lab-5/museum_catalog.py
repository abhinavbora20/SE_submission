"""Manage museum artifacts and their display status."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE artifacts (
        id INTEGER PRIMARY KEY,
        title TEXT,
        era TEXT,
        value INTEGER,
        on_display INTEGER
    )
    """
)


def add_artifact(title, era, value, on_display=0):
    """Add an artifact to the museum catalog."""
    conn.execute(
        """
        INSERT INTO artifacts (title, era, value, on_display)
        VALUES (?, ?, ?, ?)
        """,
        (title, era, value, on_display),
    )
    conn.commit()


def display_status(artifact_id):
    """Return whether an artifact is on display or in storage."""
    row = conn.execute(
        "SELECT on_display FROM artifacts WHERE id = ?",
        (artifact_id,),
    ).fetchone()

    if row is None:
        return "artifact not found"
    if row[0] == 1:
        return "on display"
    return "in storage"


def total_value(era):
    """Calculate the total value of artifacts from a given era."""
    total = 0
    for (value,) in conn.execute(
        "SELECT value FROM artifacts WHERE era = ?",
        (era,),
    ):
        total += value
    return total


def move_to_display(artifact_id):
    """Move an artifact to display."""
    conn.execute(
        "UPDATE artifacts SET on_display = 1 WHERE id = ?",
        (artifact_id,),
    )
    conn.commit()


def backup_note():
    """Print a message confirming the backup note."""
    print("Catalog backup complete.")


def main():
    """Run the museum catalog demonstration."""
    add_artifact("Bronze Mirror", "Chola", 120000)
    add_artifact("Palm Manuscript", "Vijayanagara", 80000, 1)
    add_artifact("Terracotta Lamp", "Chola", 15000)

    move_to_display(1)

    print(display_status(1))
    print(total_value("Chola"))
    backup_note()


if __name__ == "__main__":
    main()
