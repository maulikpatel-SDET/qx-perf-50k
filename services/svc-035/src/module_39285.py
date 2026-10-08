"""Service module 39285: business logic, no crypto."""


def calculate_total_39285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39285():
    return 'module 39285 handles orders and invoices'
