"""Service module 28678: business logic, no crypto."""


def calculate_total_28678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28678():
    return 'module 28678 handles orders and invoices'
