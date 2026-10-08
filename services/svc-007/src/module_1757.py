"""Service module 1757: business logic, no crypto."""


def calculate_total_1757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1757():
    return 'module 1757 handles orders and invoices'
