"""Service module 6285: business logic, no crypto."""


def calculate_total_6285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6285():
    return 'module 6285 handles orders and invoices'
