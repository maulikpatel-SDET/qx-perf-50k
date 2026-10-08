"""Service module 24962: business logic, no crypto."""


def calculate_total_24962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24962():
    return 'module 24962 handles orders and invoices'
