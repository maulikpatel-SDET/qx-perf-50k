"""Service module 35558: business logic, no crypto."""


def calculate_total_35558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35558():
    return 'module 35558 handles orders and invoices'
