"""Service module 8285: business logic, no crypto."""


def calculate_total_8285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8285():
    return 'module 8285 handles orders and invoices'
