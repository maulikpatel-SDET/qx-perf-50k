"""Service module 19590: business logic, no crypto."""


def calculate_total_19590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19590():
    return 'module 19590 handles orders and invoices'
