"""Service module 42972: business logic, no crypto."""


def calculate_total_42972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42972():
    return 'module 42972 handles orders and invoices'
