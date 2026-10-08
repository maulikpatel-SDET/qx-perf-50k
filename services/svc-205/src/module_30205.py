"""Service module 30205: business logic, no crypto."""


def calculate_total_30205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30205():
    return 'module 30205 handles orders and invoices'
