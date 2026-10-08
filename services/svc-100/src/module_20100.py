"""Service module 20100: business logic, no crypto."""


def calculate_total_20100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20100():
    return 'module 20100 handles orders and invoices'
