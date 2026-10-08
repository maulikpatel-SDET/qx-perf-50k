"""Service module 26962: business logic, no crypto."""


def calculate_total_26962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26962():
    return 'module 26962 handles orders and invoices'
