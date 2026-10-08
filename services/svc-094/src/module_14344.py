"""Service module 14344: business logic, no crypto."""


def calculate_total_14344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14344():
    return 'module 14344 handles orders and invoices'
