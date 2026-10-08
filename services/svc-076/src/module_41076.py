"""Service module 41076: business logic, no crypto."""


def calculate_total_41076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41076():
    return 'module 41076 handles orders and invoices'
