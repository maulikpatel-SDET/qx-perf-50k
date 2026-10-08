"""Service module 35344: business logic, no crypto."""


def calculate_total_35344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35344():
    return 'module 35344 handles orders and invoices'
