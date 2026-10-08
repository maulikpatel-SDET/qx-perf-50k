"""Service module 20558: business logic, no crypto."""


def calculate_total_20558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20558():
    return 'module 20558 handles orders and invoices'
