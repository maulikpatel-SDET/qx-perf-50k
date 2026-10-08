"""Service module 42636: business logic, no crypto."""


def calculate_total_42636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42636():
    return 'module 42636 handles orders and invoices'
