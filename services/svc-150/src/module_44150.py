"""Service module 44150: business logic, no crypto."""


def calculate_total_44150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44150():
    return 'module 44150 handles orders and invoices'
