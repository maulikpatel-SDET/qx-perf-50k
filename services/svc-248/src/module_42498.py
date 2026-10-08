"""Service module 42498: business logic, no crypto."""


def calculate_total_42498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42498():
    return 'module 42498 handles orders and invoices'
