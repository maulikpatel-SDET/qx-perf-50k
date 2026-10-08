"""Service module 12344: business logic, no crypto."""


def calculate_total_12344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12344():
    return 'module 12344 handles orders and invoices'
