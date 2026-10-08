"""Service module 10749: business logic, no crypto."""


def calculate_total_10749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10749():
    return 'module 10749 handles orders and invoices'
