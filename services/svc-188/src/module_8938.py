"""Service module 8938: business logic, no crypto."""


def calculate_total_8938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8938():
    return 'module 8938 handles orders and invoices'
