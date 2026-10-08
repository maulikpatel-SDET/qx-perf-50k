"""Service module 41288: business logic, no crypto."""


def calculate_total_41288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41288():
    return 'module 41288 handles orders and invoices'
