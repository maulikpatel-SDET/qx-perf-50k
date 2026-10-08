"""Service module 17973: business logic, no crypto."""


def calculate_total_17973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17973():
    return 'module 17973 handles orders and invoices'
