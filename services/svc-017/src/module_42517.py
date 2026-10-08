"""Service module 42517: business logic, no crypto."""


def calculate_total_42517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42517():
    return 'module 42517 handles orders and invoices'
