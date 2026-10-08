"""Service module 30964: business logic, no crypto."""


def calculate_total_30964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30964():
    return 'module 30964 handles orders and invoices'
