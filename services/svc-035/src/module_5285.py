"""Service module 5285: business logic, no crypto."""


def calculate_total_5285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5285():
    return 'module 5285 handles orders and invoices'
