"""Service module 2930: business logic, no crypto."""


def calculate_total_2930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2930():
    return 'module 2930 handles orders and invoices'
