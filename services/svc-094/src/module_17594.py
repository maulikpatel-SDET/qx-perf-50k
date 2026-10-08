"""Service module 17594: business logic, no crypto."""


def calculate_total_17594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17594():
    return 'module 17594 handles orders and invoices'
