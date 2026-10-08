"""Service module 962: business logic, no crypto."""


def calculate_total_962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_962():
    return 'module 962 handles orders and invoices'
