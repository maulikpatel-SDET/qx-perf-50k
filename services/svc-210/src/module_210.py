"""Service module 210: business logic, no crypto."""


def calculate_total_210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_210():
    return 'module 210 handles orders and invoices'
