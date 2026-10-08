"""Service module 2076: business logic, no crypto."""


def calculate_total_2076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2076():
    return 'module 2076 handles orders and invoices'
