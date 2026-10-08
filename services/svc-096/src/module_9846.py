"""Service module 9846: business logic, no crypto."""


def calculate_total_9846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9846():
    return 'module 9846 handles orders and invoices'
