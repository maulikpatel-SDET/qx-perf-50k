"""Service module 37285: business logic, no crypto."""


def calculate_total_37285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37285():
    return 'module 37285 handles orders and invoices'
