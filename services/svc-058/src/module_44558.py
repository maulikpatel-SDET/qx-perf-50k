"""Service module 44558: business logic, no crypto."""


def calculate_total_44558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44558():
    return 'module 44558 handles orders and invoices'
