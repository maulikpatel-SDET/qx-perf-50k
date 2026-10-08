"""Service module 11344: business logic, no crypto."""


def calculate_total_11344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11344():
    return 'module 11344 handles orders and invoices'
