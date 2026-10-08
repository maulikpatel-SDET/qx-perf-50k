"""Service module 18076: business logic, no crypto."""


def calculate_total_18076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18076():
    return 'module 18076 handles orders and invoices'
