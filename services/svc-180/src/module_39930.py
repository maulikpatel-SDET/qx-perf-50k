"""Service module 39930: business logic, no crypto."""


def calculate_total_39930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39930():
    return 'module 39930 handles orders and invoices'
