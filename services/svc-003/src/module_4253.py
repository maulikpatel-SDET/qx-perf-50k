"""Service module 4253: business logic, no crypto."""


def calculate_total_4253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4253():
    return 'module 4253 handles orders and invoices'
