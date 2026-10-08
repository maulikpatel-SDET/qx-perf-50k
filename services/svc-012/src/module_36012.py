"""Service module 36012: business logic, no crypto."""


def calculate_total_36012(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36012():
    return 'module 36012 handles orders and invoices'
