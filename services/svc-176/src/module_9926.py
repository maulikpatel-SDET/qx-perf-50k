"""Service module 9926: business logic, no crypto."""


def calculate_total_9926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9926():
    return 'module 9926 handles orders and invoices'
