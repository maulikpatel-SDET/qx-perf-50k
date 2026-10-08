"""Service module 48370: business logic, no crypto."""


def calculate_total_48370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48370():
    return 'module 48370 handles orders and invoices'
