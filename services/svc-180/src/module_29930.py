"""Service module 29930: business logic, no crypto."""


def calculate_total_29930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29930():
    return 'module 29930 handles orders and invoices'
