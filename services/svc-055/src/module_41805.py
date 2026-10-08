"""Service module 41805: business logic, no crypto."""


def calculate_total_41805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41805():
    return 'module 41805 handles orders and invoices'
