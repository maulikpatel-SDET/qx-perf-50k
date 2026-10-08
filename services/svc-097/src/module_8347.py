"""Service module 8347: business logic, no crypto."""


def calculate_total_8347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8347():
    return 'module 8347 handles orders and invoices'
