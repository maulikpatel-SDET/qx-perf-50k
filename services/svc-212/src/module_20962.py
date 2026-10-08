"""Service module 20962: business logic, no crypto."""


def calculate_total_20962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20962():
    return 'module 20962 handles orders and invoices'
