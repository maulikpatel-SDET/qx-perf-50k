"""Service module 6930: business logic, no crypto."""


def calculate_total_6930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6930():
    return 'module 6930 handles orders and invoices'
