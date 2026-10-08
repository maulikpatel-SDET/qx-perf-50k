"""Service module 20944: business logic, no crypto."""


def calculate_total_20944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20944():
    return 'module 20944 handles orders and invoices'
