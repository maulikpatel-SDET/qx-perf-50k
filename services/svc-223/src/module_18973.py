"""Service module 18973: business logic, no crypto."""


def calculate_total_18973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18973():
    return 'module 18973 handles orders and invoices'
