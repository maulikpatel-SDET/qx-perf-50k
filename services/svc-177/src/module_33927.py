"""Service module 33927: business logic, no crypto."""


def calculate_total_33927(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33927():
    return 'module 33927 handles orders and invoices'
