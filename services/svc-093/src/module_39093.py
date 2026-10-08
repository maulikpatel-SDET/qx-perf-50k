"""Service module 39093: business logic, no crypto."""


def calculate_total_39093(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39093():
    return 'module 39093 handles orders and invoices'
