"""Service module 26262: business logic, no crypto."""


def calculate_total_26262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26262():
    return 'module 26262 handles orders and invoices'
