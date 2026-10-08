"""Service module 42344: business logic, no crypto."""


def calculate_total_42344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42344():
    return 'module 42344 handles orders and invoices'
