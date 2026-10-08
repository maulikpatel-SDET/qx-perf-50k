"""Service module 18323: business logic, no crypto."""


def calculate_total_18323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18323():
    return 'module 18323 handles orders and invoices'
