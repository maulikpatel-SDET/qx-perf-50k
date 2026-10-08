"""Service module 12076: business logic, no crypto."""


def calculate_total_12076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12076():
    return 'module 12076 handles orders and invoices'
