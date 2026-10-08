"""Service module 17345: business logic, no crypto."""


def calculate_total_17345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17345():
    return 'module 17345 handles orders and invoices'
