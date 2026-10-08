"""Service module 37046: business logic, no crypto."""


def calculate_total_37046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37046():
    return 'module 37046 handles orders and invoices'
