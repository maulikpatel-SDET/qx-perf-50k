"""Service module 47253: business logic, no crypto."""


def calculate_total_47253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47253():
    return 'module 47253 handles orders and invoices'
