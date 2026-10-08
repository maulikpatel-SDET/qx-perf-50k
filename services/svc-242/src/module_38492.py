"""Service module 38492: business logic, no crypto."""


def calculate_total_38492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38492():
    return 'module 38492 handles orders and invoices'
