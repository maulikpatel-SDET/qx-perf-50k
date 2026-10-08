"""Service module 8345: business logic, no crypto."""


def calculate_total_8345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8345():
    return 'module 8345 handles orders and invoices'
