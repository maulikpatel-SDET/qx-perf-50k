"""Service module 49540: business logic, no crypto."""


def calculate_total_49540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49540():
    return 'module 49540 handles orders and invoices'
