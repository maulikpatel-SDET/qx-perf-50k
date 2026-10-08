"""Service module 19309: business logic, no crypto."""


def calculate_total_19309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19309():
    return 'module 19309 handles orders and invoices'
