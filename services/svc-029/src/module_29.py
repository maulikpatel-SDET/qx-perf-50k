"""Service module 29: business logic, no crypto."""


def calculate_total_29(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29():
    return 'module 29 handles orders and invoices'
