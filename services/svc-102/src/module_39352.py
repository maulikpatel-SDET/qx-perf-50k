"""Service module 39352: business logic, no crypto."""


def calculate_total_39352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39352():
    return 'module 39352 handles orders and invoices'
