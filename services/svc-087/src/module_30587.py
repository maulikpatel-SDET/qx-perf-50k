"""Service module 30587: business logic, no crypto."""


def calculate_total_30587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30587():
    return 'module 30587 handles orders and invoices'
