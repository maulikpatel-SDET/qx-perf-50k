"""Service module 47191: business logic, no crypto."""


def calculate_total_47191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47191():
    return 'module 47191 handles orders and invoices'
