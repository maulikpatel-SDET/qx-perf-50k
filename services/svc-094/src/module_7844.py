"""Service module 7844: business logic, no crypto."""


def calculate_total_7844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7844():
    return 'module 7844 handles orders and invoices'
