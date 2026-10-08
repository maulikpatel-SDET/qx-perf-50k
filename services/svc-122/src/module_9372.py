"""Service module 9372: business logic, no crypto."""


def calculate_total_9372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9372():
    return 'module 9372 handles orders and invoices'
