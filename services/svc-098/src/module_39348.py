"""Service module 39348: business logic, no crypto."""


def calculate_total_39348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39348():
    return 'module 39348 handles orders and invoices'
