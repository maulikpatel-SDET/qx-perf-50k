"""Service module 9973: business logic, no crypto."""


def calculate_total_9973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9973():
    return 'module 9973 handles orders and invoices'
