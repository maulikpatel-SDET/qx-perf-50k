"""Service module 17558: business logic, no crypto."""


def calculate_total_17558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17558():
    return 'module 17558 handles orders and invoices'
