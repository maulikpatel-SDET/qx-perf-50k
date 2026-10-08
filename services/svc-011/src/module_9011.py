"""Service module 9011: business logic, no crypto."""


def calculate_total_9011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9011():
    return 'module 9011 handles orders and invoices'
