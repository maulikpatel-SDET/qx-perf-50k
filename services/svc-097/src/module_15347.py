"""Service module 15347: business logic, no crypto."""


def calculate_total_15347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15347():
    return 'module 15347 handles orders and invoices'
