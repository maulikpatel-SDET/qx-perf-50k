"""Service module 26347: business logic, no crypto."""


def calculate_total_26347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26347():
    return 'module 26347 handles orders and invoices'
