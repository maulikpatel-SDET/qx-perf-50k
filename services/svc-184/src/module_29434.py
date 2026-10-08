"""Service module 29434: business logic, no crypto."""


def calculate_total_29434(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29434():
    return 'module 29434 handles orders and invoices'
