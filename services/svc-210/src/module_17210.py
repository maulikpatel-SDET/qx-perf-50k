"""Service module 17210: business logic, no crypto."""


def calculate_total_17210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17210():
    return 'module 17210 handles orders and invoices'
