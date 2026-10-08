"""Service module 33344: business logic, no crypto."""


def calculate_total_33344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33344():
    return 'module 33344 handles orders and invoices'
