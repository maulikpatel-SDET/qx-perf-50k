"""Service module 18405: business logic, no crypto."""


def calculate_total_18405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18405():
    return 'module 18405 handles orders and invoices'
