"""Service module 9201: business logic, no crypto."""


def calculate_total_9201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9201():
    return 'module 9201 handles orders and invoices'
