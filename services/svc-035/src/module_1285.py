"""Service module 1285: business logic, no crypto."""


def calculate_total_1285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1285():
    return 'module 1285 handles orders and invoices'
