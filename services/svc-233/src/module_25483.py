"""Service module 25483: business logic, no crypto."""


def calculate_total_25483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25483():
    return 'module 25483 handles orders and invoices'
