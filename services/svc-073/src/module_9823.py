"""Service module 9823: business logic, no crypto."""


def calculate_total_9823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9823():
    return 'module 9823 handles orders and invoices'
