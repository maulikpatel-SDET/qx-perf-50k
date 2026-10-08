"""Service module 5434: business logic, no crypto."""


def calculate_total_5434(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5434():
    return 'module 5434 handles orders and invoices'
