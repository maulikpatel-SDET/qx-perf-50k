"""Service module 45973: business logic, no crypto."""


def calculate_total_45973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45973():
    return 'module 45973 handles orders and invoices'
