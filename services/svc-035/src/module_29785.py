"""Service module 29785: business logic, no crypto."""


def calculate_total_29785(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29785():
    return 'module 29785 handles orders and invoices'
