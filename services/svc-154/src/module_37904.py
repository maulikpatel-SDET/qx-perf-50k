"""Service module 37904: business logic, no crypto."""


def calculate_total_37904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37904():
    return 'module 37904 handles orders and invoices'
