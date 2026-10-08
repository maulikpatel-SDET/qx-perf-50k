"""Service module 10344: business logic, no crypto."""


def calculate_total_10344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10344():
    return 'module 10344 handles orders and invoices'
