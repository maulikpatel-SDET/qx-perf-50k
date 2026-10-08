"""Service module 17100: business logic, no crypto."""


def calculate_total_17100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17100():
    return 'module 17100 handles orders and invoices'
