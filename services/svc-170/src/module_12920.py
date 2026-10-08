"""Service module 12920: business logic, no crypto."""


def calculate_total_12920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12920():
    return 'module 12920 handles orders and invoices'
