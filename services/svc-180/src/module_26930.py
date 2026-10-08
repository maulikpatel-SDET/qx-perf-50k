"""Service module 26930: business logic, no crypto."""


def calculate_total_26930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26930():
    return 'module 26930 handles orders and invoices'
