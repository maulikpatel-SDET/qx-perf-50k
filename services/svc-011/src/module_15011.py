"""Service module 15011: business logic, no crypto."""


def calculate_total_15011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15011():
    return 'module 15011 handles orders and invoices'
