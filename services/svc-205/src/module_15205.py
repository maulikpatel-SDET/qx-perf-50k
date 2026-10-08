"""Service module 15205: business logic, no crypto."""


def calculate_total_15205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15205():
    return 'module 15205 handles orders and invoices'
