"""Service module 5111: business logic, no crypto."""


def calculate_total_5111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5111():
    return 'module 5111 handles orders and invoices'
