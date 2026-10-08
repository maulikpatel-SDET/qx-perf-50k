"""Service module 48695: business logic, no crypto."""


def calculate_total_48695(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48695():
    return 'module 48695 handles orders and invoices'
