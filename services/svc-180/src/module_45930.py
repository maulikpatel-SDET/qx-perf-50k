"""Service module 45930: business logic, no crypto."""


def calculate_total_45930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45930():
    return 'module 45930 handles orders and invoices'
