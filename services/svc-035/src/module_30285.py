"""Service module 30285: business logic, no crypto."""


def calculate_total_30285(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30285():
    return 'module 30285 handles orders and invoices'
