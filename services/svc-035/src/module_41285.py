"""Service module 41285: business logic, no crypto."""


def calculate_total_41285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41285():
    return 'module 41285 handles orders and invoices'
