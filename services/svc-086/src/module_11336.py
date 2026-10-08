"""Service module 11336: business logic, no crypto."""


def calculate_total_11336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11336():
    return 'module 11336 handles orders and invoices'
