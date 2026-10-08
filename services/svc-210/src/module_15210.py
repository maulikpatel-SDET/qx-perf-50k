"""Service module 15210: business logic, no crypto."""


def calculate_total_15210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15210():
    return 'module 15210 handles orders and invoices'
