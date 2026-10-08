"""Service module 42285: business logic, no crypto."""


def calculate_total_42285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42285():
    return 'module 42285 handles orders and invoices'
