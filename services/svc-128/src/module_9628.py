"""Service module 9628: business logic, no crypto."""


def calculate_total_9628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9628():
    return 'module 9628 handles orders and invoices'
