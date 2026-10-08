"""Service module 21291: business logic, no crypto."""


def calculate_total_21291(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21291():
    return 'module 21291 handles orders and invoices'
