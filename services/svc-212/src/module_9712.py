"""Service module 9712: business logic, no crypto."""


def calculate_total_9712(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9712():
    return 'module 9712 handles orders and invoices'
