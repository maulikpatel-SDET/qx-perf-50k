"""Service module 12558: business logic, no crypto."""


def calculate_total_12558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12558():
    return 'module 12558 handles orders and invoices'
