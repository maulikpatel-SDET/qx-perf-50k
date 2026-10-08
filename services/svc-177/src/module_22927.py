"""Service module 22927: business logic, no crypto."""


def calculate_total_22927(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22927():
    return 'module 22927 handles orders and invoices'
