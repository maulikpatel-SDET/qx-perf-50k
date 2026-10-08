"""Service module 49076: business logic, no crypto."""


def calculate_total_49076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49076():
    return 'module 49076 handles orders and invoices'
