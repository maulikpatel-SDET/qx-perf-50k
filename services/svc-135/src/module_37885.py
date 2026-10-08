"""Service module 37885: business logic, no crypto."""


def calculate_total_37885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37885():
    return 'module 37885 handles orders and invoices'
