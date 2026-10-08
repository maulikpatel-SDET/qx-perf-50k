"""Service module 5347: business logic, no crypto."""


def calculate_total_5347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5347():
    return 'module 5347 handles orders and invoices'
