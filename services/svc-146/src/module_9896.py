"""Service module 9896: business logic, no crypto."""


def calculate_total_9896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9896():
    return 'module 9896 handles orders and invoices'
