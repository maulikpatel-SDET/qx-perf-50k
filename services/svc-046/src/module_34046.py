"""Service module 34046: business logic, no crypto."""


def calculate_total_34046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34046():
    return 'module 34046 handles orders and invoices'
