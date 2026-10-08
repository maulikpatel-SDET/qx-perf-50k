"""Service module 39885: business logic, no crypto."""


def calculate_total_39885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39885():
    return 'module 39885 handles orders and invoices'
