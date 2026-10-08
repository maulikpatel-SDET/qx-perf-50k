"""Service module 46309: business logic, no crypto."""


def calculate_total_46309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46309():
    return 'module 46309 handles orders and invoices'
