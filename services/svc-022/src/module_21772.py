"""Service module 21772: business logic, no crypto."""


def calculate_total_21772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21772():
    return 'module 21772 handles orders and invoices'
