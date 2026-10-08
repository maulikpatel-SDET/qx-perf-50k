"""Service module 42910: business logic, no crypto."""


def calculate_total_42910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42910():
    return 'module 42910 handles orders and invoices'
