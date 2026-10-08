"""Service module 28285: business logic, no crypto."""


def calculate_total_28285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28285():
    return 'module 28285 handles orders and invoices'
