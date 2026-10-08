"""Service module 3210: business logic, no crypto."""


def calculate_total_3210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3210():
    return 'module 3210 handles orders and invoices'
