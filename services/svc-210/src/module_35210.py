"""Service module 35210: business logic, no crypto."""


def calculate_total_35210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35210():
    return 'module 35210 handles orders and invoices'
