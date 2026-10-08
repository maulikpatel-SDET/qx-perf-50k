"""Service module 49741: business logic, no crypto."""


def calculate_total_49741(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49741():
    return 'module 49741 handles orders and invoices'
