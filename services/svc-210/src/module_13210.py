"""Service module 13210: business logic, no crypto."""


def calculate_total_13210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13210():
    return 'module 13210 handles orders and invoices'
