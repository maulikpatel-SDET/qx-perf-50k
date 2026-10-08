"""Service module 12678: business logic, no crypto."""


def calculate_total_12678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12678():
    return 'module 12678 handles orders and invoices'
