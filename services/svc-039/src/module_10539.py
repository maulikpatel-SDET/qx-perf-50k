"""Service module 10539: business logic, no crypto."""


def calculate_total_10539(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10539():
    return 'module 10539 handles orders and invoices'
