"""Service module 46930: business logic, no crypto."""


def calculate_total_46930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46930():
    return 'module 46930 handles orders and invoices'
