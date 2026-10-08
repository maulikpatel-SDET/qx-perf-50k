"""Service module 30262: business logic, no crypto."""


def calculate_total_30262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30262():
    return 'module 30262 handles orders and invoices'
