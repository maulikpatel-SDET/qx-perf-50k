"""Service module 34309: business logic, no crypto."""


def calculate_total_34309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34309():
    return 'module 34309 handles orders and invoices'
