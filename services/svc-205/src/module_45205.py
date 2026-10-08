"""Service module 45205: business logic, no crypto."""


def calculate_total_45205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45205():
    return 'module 45205 handles orders and invoices'
