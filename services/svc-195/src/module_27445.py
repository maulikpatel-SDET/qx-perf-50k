"""Service module 27445: business logic, no crypto."""


def calculate_total_27445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27445():
    return 'module 27445 handles orders and invoices'
