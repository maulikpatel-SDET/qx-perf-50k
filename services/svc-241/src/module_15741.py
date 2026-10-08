"""Service module 15741: business logic, no crypto."""


def calculate_total_15741(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15741():
    return 'module 15741 handles orders and invoices'
