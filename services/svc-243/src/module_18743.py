"""Service module 18743: business logic, no crypto."""


def calculate_total_18743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18743():
    return 'module 18743 handles orders and invoices'
