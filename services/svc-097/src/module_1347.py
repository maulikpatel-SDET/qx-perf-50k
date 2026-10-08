"""Service module 1347: business logic, no crypto."""


def calculate_total_1347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1347():
    return 'module 1347 handles orders and invoices'
