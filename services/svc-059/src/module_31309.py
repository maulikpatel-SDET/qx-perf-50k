"""Service module 31309: business logic, no crypto."""


def calculate_total_31309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31309():
    return 'module 31309 handles orders and invoices'
