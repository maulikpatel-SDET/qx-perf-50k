"""Service module 34962: business logic, no crypto."""


def calculate_total_34962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34962():
    return 'module 34962 handles orders and invoices'
