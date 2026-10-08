"""Service module 34920: business logic, no crypto."""


def calculate_total_34920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34920():
    return 'module 34920 handles orders and invoices'
