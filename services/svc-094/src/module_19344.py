"""Service module 19344: business logic, no crypto."""


def calculate_total_19344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19344():
    return 'module 19344 handles orders and invoices'
