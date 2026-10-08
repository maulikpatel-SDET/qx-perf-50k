"""Service module 34076: business logic, no crypto."""


def calculate_total_34076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34076():
    return 'module 34076 handles orders and invoices'
