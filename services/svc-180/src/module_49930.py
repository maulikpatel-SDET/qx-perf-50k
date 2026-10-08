"""Service module 49930: business logic, no crypto."""


def calculate_total_49930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49930():
    return 'module 49930 handles orders and invoices'
