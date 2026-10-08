"""Service module 9146: business logic, no crypto."""


def calculate_total_9146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9146():
    return 'module 9146 handles orders and invoices'
