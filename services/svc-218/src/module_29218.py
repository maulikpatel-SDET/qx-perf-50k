"""Service module 29218: business logic, no crypto."""


def calculate_total_29218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29218():
    return 'module 29218 handles orders and invoices'
