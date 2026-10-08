"""Service module 35076: business logic, no crypto."""


def calculate_total_35076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35076():
    return 'module 35076 handles orders and invoices'
