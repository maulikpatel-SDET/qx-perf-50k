"""Service module 45741: business logic, no crypto."""


def calculate_total_45741(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45741():
    return 'module 45741 handles orders and invoices'
