"""Service module 6614: business logic, no crypto."""


def calculate_total_6614(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6614():
    return 'module 6614 handles orders and invoices'
