"""Service module 12493: business logic, no crypto."""


def calculate_total_12493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12493():
    return 'module 12493 handles orders and invoices'
