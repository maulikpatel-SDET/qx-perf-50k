"""Service module 7962: business logic, no crypto."""


def calculate_total_7962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7962():
    return 'module 7962 handles orders and invoices'
