"""Service module 38390: business logic, no crypto."""


def calculate_total_38390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38390():
    return 'module 38390 handles orders and invoices'
