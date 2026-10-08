"""Service module 30941: business logic, no crypto."""


def calculate_total_30941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30941():
    return 'module 30941 handles orders and invoices'
