"""Service module 3635: business logic, no crypto."""


def calculate_total_3635(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3635():
    return 'module 3635 handles orders and invoices'
