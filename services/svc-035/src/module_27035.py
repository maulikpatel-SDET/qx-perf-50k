"""Service module 27035: business logic, no crypto."""


def calculate_total_27035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27035():
    return 'module 27035 handles orders and invoices'
