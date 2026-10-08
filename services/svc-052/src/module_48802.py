"""Service module 48802: business logic, no crypto."""


def calculate_total_48802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48802():
    return 'module 48802 handles orders and invoices'
