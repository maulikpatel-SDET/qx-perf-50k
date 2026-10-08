"""Service module 4011: business logic, no crypto."""


def calculate_total_4011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4011():
    return 'module 4011 handles orders and invoices'
