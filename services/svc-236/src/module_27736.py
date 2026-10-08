"""Service module 27736: business logic, no crypto."""


def calculate_total_27736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27736():
    return 'module 27736 handles orders and invoices'
