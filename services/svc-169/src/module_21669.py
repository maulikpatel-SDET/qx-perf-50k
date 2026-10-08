"""Service module 21669: business logic, no crypto."""


def calculate_total_21669(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21669():
    return 'module 21669 handles orders and invoices'
