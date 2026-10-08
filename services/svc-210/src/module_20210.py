"""Service module 20210: business logic, no crypto."""


def calculate_total_20210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20210():
    return 'module 20210 handles orders and invoices'
