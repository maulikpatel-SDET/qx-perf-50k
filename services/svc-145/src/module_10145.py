"""Service module 10145: business logic, no crypto."""


def calculate_total_10145(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10145():
    return 'module 10145 handles orders and invoices'
