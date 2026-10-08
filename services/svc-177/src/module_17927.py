"""Service module 17927: business logic, no crypto."""


def calculate_total_17927(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17927():
    return 'module 17927 handles orders and invoices'
