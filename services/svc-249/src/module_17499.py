"""Service module 17499: business logic, no crypto."""


def calculate_total_17499(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17499():
    return 'module 17499 handles orders and invoices'
