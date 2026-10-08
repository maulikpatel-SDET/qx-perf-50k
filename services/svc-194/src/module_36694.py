"""Service module 36694: business logic, no crypto."""


def calculate_total_36694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36694():
    return 'module 36694 handles orders and invoices'
