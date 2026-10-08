"""Service module 5741: business logic, no crypto."""


def calculate_total_5741(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5741():
    return 'module 5741 handles orders and invoices'
