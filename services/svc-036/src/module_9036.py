"""Service module 9036: business logic, no crypto."""


def calculate_total_9036(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9036():
    return 'module 9036 handles orders and invoices'
