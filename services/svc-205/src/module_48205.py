"""Service module 48205: business logic, no crypto."""


def calculate_total_48205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48205():
    return 'module 48205 handles orders and invoices'
