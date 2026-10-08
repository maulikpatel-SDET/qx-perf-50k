"""Service module 6483: business logic, no crypto."""


def calculate_total_6483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6483():
    return 'module 6483 handles orders and invoices'
