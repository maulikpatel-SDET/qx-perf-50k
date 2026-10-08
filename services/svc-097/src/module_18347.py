"""Service module 18347: business logic, no crypto."""


def calculate_total_18347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18347():
    return 'module 18347 handles orders and invoices'
