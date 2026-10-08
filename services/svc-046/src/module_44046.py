"""Service module 44046: business logic, no crypto."""


def calculate_total_44046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44046():
    return 'module 44046 handles orders and invoices'
