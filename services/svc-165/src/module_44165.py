"""Service module 44165: business logic, no crypto."""


def calculate_total_44165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44165():
    return 'module 44165 handles orders and invoices'
