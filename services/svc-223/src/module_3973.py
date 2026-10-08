"""Service module 3973: business logic, no crypto."""


def calculate_total_3973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3973():
    return 'module 3973 handles orders and invoices'
