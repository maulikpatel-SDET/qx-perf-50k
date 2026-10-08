"""Service module 27496: business logic, no crypto."""


def calculate_total_27496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27496():
    return 'module 27496 handles orders and invoices'
