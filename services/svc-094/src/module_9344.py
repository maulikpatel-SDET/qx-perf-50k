"""Service module 9344: business logic, no crypto."""


def calculate_total_9344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9344():
    return 'module 9344 handles orders and invoices'
