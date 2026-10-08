"""Service module 18957: business logic, no crypto."""


def calculate_total_18957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18957():
    return 'module 18957 handles orders and invoices'
