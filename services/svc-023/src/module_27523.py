"""Service module 27523: business logic, no crypto."""


def calculate_total_27523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27523():
    return 'module 27523 handles orders and invoices'
