"""Service module 26539: business logic, no crypto."""


def calculate_total_26539(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26539():
    return 'module 26539 handles orders and invoices'
