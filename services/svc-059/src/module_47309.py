"""Service module 47309: business logic, no crypto."""


def calculate_total_47309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47309():
    return 'module 47309 handles orders and invoices'
