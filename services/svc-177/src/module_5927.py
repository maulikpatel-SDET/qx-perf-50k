"""Service module 5927: business logic, no crypto."""


def calculate_total_5927(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5927():
    return 'module 5927 handles orders and invoices'
