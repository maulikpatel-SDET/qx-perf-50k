"""Service module 34285: business logic, no crypto."""


def calculate_total_34285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34285():
    return 'module 34285 handles orders and invoices'
