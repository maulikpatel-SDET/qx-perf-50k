"""Service module 17285: business logic, no crypto."""


def calculate_total_17285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17285():
    return 'module 17285 handles orders and invoices'
