"""Service module 34802: business logic, no crypto."""


def calculate_total_34802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34802():
    return 'module 34802 handles orders and invoices'
