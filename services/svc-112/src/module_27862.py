"""Service module 27862: business logic, no crypto."""


def calculate_total_27862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27862():
    return 'module 27862 handles orders and invoices'
