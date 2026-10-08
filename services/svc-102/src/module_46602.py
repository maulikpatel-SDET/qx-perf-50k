"""Service module 46602: business logic, no crypto."""


def calculate_total_46602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46602():
    return 'module 46602 handles orders and invoices'
