"""Service module 21904: business logic, no crypto."""


def calculate_total_21904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21904():
    return 'module 21904 handles orders and invoices'
