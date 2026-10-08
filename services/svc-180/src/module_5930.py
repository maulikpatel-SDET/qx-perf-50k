"""Service module 5930: business logic, no crypto."""


def calculate_total_5930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5930():
    return 'module 5930 handles orders and invoices'
