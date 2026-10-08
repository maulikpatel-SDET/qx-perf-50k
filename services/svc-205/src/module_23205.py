"""Service module 23205: business logic, no crypto."""


def calculate_total_23205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23205():
    return 'module 23205 handles orders and invoices'
