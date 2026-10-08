"""Service module 28508: business logic, no crypto."""


def calculate_total_28508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28508():
    return 'module 28508 handles orders and invoices'
