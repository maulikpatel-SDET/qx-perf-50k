"""Service module 1205: business logic, no crypto."""


def calculate_total_1205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1205():
    return 'module 1205 handles orders and invoices'
