"""Service module 44434: business logic, no crypto."""


def calculate_total_44434(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44434():
    return 'module 44434 handles orders and invoices'
