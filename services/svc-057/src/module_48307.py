"""Service module 48307: business logic, no crypto."""


def calculate_total_48307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48307():
    return 'module 48307 handles orders and invoices'
