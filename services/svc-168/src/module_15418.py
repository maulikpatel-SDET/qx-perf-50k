"""Service module 15418: business logic, no crypto."""


def calculate_total_15418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15418():
    return 'module 15418 handles orders and invoices'
