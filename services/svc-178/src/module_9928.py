"""Service module 9928: business logic, no crypto."""


def calculate_total_9928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9928():
    return 'module 9928 handles orders and invoices'
