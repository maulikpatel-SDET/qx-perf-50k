"""Service module 22496: business logic, no crypto."""


def calculate_total_22496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22496():
    return 'module 22496 handles orders and invoices'
