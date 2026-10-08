"""Service module 49973: business logic, no crypto."""


def calculate_total_49973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49973():
    return 'module 49973 handles orders and invoices'
