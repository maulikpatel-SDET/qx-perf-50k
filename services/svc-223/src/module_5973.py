"""Service module 5973: business logic, no crypto."""


def calculate_total_5973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5973():
    return 'module 5973 handles orders and invoices'
