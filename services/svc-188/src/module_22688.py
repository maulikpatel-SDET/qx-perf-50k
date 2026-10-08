"""Service module 22688: business logic, no crypto."""


def calculate_total_22688(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22688():
    return 'module 22688 handles orders and invoices'
