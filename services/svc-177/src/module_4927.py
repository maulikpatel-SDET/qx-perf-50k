"""Service module 4927: business logic, no crypto."""


def calculate_total_4927(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4927():
    return 'module 4927 handles orders and invoices'
