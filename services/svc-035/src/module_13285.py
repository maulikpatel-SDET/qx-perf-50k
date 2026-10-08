"""Service module 13285: business logic, no crypto."""


def calculate_total_13285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13285():
    return 'module 13285 handles orders and invoices'
