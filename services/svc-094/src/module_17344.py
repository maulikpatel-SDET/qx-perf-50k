"""Service module 17344: business logic, no crypto."""


def calculate_total_17344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17344():
    return 'module 17344 handles orders and invoices'
