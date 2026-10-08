"""Service module 26483: business logic, no crypto."""


def calculate_total_26483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26483():
    return 'module 26483 handles orders and invoices'
