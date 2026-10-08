"""Service module 9772: business logic, no crypto."""


def calculate_total_9772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9772():
    return 'module 9772 handles orders and invoices'
