"""Service module 47871: business logic, no crypto."""


def calculate_total_47871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47871():
    return 'module 47871 handles orders and invoices'
