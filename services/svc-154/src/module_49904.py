"""Service module 49904: business logic, no crypto."""


def calculate_total_49904(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49904():
    return 'module 49904 handles orders and invoices'
