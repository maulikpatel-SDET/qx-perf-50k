"""Service module 27493: business logic, no crypto."""


def calculate_total_27493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27493():
    return 'module 27493 handles orders and invoices'
