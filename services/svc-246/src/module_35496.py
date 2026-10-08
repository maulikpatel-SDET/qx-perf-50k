"""Service module 35496: business logic, no crypto."""


def calculate_total_35496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35496():
    return 'module 35496 handles orders and invoices'
