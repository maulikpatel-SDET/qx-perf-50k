"""Service module 40228: business logic, no crypto."""


def calculate_total_40228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40228():
    return 'module 40228 handles orders and invoices'
