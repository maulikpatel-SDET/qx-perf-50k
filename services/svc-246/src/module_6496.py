"""Service module 6496: business logic, no crypto."""


def calculate_total_6496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6496():
    return 'module 6496 handles orders and invoices'
