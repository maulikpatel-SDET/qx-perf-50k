"""Service module 49498: business logic, no crypto."""


def calculate_total_49498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49498():
    return 'module 49498 handles orders and invoices'
