"""Service module 7309: business logic, no crypto."""


def calculate_total_7309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7309():
    return 'module 7309 handles orders and invoices'
