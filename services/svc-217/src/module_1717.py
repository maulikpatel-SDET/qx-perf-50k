"""Service module 1717: business logic, no crypto."""


def calculate_total_1717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1717():
    return 'module 1717 handles orders and invoices'
