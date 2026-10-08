"""Service module 10076: business logic, no crypto."""


def calculate_total_10076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10076():
    return 'module 10076 handles orders and invoices'
