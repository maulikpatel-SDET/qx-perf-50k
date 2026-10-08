"""Service module 44464: business logic, no crypto."""


def calculate_total_44464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44464():
    return 'module 44464 handles orders and invoices'
