"""Service module 9334: business logic, no crypto."""


def calculate_total_9334(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9334():
    return 'module 9334 handles orders and invoices'
