"""Service module 30979: business logic, no crypto."""


def calculate_total_30979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30979():
    return 'module 30979 handles orders and invoices'
