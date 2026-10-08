"""Service module 20165: business logic, no crypto."""


def calculate_total_20165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20165():
    return 'module 20165 handles orders and invoices'
