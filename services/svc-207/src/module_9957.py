"""Service module 9957: business logic, no crypto."""


def calculate_total_9957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9957():
    return 'module 9957 handles orders and invoices'
