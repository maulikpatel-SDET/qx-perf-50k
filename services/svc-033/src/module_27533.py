"""Service module 27533: business logic, no crypto."""


def calculate_total_27533(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27533():
    return 'module 27533 handles orders and invoices'
