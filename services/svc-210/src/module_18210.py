"""Service module 18210: business logic, no crypto."""


def calculate_total_18210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18210():
    return 'module 18210 handles orders and invoices'
