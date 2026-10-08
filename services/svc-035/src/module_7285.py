"""Service module 7285: business logic, no crypto."""


def calculate_total_7285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7285():
    return 'module 7285 handles orders and invoices'
