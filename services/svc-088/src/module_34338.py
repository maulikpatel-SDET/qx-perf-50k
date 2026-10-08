"""Service module 34338: business logic, no crypto."""


def calculate_total_34338(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34338():
    return 'module 34338 handles orders and invoices'
