#!/usr/bin/python3
"""
Generates personalized invitation files from a template and attendee data.
"""
import os


def _log(message):
    """Simple logger for required error/info messages."""
    print(message)


def generate_invitations(template, attendees):
    """
    Generate invitation files output_X.txt from a template and a list of attendee dicts.

    Args:
        template (str): Template text containing placeholders {name}, {event_title},
                        {event_date}, {event_location}.
        attendees (list[dict]): List of attendee dictionaries.

    Behavior:
        - If template is empty: log and return (no files).
        - If attendees is empty: log and return (no files).
        - If types are invalid: log and return (no files).
        - Missing/None values replaced with "N/A".
        - Files named output_1.txt, output_2.txt, ... created.
        - If a target file already exists, it is not overwritten.
    """
    # Type checks
    if not isinstance(template, str):
        _log(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        _log("Invalid input type: attendees must be a list of dictionaries.")
        return

    # Empty checks
    if template == "":
        _log("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        _log("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        filled = template

        for key in placeholders:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            filled = filled.replace("{" + key + "}", str(value))

        filename = f"output_{idx}.txt"

        # Avoid overwriting existing files (per hint)
        if os.path.exists(filename):
            _log(f"{filename} already exists, skipping.")
            continue

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(filled)
        except OSError as e:
            _log(f"Error writing {filename}: {e}")
