"""Service module 2347: business logic, no crypto."""


def calculate_total_2347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2347():
    return 'module 2347 handles orders and invoices'
