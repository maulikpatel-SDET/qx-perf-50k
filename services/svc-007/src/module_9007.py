"""Service module 9007: business logic, no crypto."""


def calculate_total_9007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9007():
    return 'module 9007 handles orders and invoices'
