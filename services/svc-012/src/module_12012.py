"""Service module 12012: business logic, no crypto."""


def calculate_total_12012(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12012():
    return 'module 12012 handles orders and invoices'
