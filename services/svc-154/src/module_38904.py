"""Service module 38904: business logic, no crypto."""


def calculate_total_38904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38904():
    return 'module 38904 handles orders and invoices'
