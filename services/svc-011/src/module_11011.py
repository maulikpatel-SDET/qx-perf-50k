"""Service module 11011: business logic, no crypto."""


def calculate_total_11011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11011():
    return 'module 11011 handles orders and invoices'
