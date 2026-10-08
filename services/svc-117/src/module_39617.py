"""Service module 39617: business logic, no crypto."""


def calculate_total_39617(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39617():
    return 'module 39617 handles orders and invoices'
