"""Service module 16100: business logic, no crypto."""


def calculate_total_16100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16100():
    return 'module 16100 handles orders and invoices'
