"""Service module 16011: business logic, no crypto."""


def calculate_total_16011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16011():
    return 'module 16011 handles orders and invoices'
