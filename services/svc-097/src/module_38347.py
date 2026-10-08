"""Service module 38347: business logic, no crypto."""


def calculate_total_38347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38347():
    return 'module 38347 handles orders and invoices'
