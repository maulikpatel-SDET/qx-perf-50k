"""Service module 19046: business logic, no crypto."""


def calculate_total_19046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19046():
    return 'module 19046 handles orders and invoices'
