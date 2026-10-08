"""Service module 23802: business logic, no crypto."""


def calculate_total_23802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23802():
    return 'module 23802 handles orders and invoices'
