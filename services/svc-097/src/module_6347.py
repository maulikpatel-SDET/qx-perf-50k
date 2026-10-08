"""Service module 6347: business logic, no crypto."""


def calculate_total_6347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6347():
    return 'module 6347 handles orders and invoices'
