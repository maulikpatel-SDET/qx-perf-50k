"""Service module 4558: business logic, no crypto."""


def calculate_total_4558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4558():
    return 'module 4558 handles orders and invoices'
