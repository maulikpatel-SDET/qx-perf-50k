"""Service module 49345: business logic, no crypto."""


def calculate_total_49345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49345():
    return 'module 49345 handles orders and invoices'
