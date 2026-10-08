"""Service module 9154: business logic, no crypto."""


def calculate_total_9154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9154():
    return 'module 9154 handles orders and invoices'
