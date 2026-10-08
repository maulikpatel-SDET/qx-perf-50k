"""Service module 10011: business logic, no crypto."""


def calculate_total_10011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10011():
    return 'module 10011 handles orders and invoices'
