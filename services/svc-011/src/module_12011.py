"""Service module 12011: business logic, no crypto."""


def calculate_total_12011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12011():
    return 'module 12011 handles orders and invoices'
