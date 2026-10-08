"""Service module 44971: business logic, no crypto."""


def calculate_total_44971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44971():
    return 'module 44971 handles orders and invoices'
