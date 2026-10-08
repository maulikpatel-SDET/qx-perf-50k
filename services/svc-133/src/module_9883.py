"""Service module 9883: business logic, no crypto."""


def calculate_total_9883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9883():
    return 'module 9883 handles orders and invoices'
