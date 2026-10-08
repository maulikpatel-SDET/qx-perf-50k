"""Service module 28558: business logic, no crypto."""


def calculate_total_28558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28558():
    return 'module 28558 handles orders and invoices'
