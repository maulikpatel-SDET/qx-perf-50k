"""Service module 1558: business logic, no crypto."""


def calculate_total_1558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1558():
    return 'module 1558 handles orders and invoices'
