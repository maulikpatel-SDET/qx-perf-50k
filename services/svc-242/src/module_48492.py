"""Service module 48492: business logic, no crypto."""


def calculate_total_48492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48492():
    return 'module 48492 handles orders and invoices'
