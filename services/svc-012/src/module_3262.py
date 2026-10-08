"""Service module 3262: business logic, no crypto."""


def calculate_total_3262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3262():
    return 'module 3262 handles orders and invoices'
