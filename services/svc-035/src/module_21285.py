"""Service module 21285: business logic, no crypto."""


def calculate_total_21285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21285():
    return 'module 21285 handles orders and invoices'
