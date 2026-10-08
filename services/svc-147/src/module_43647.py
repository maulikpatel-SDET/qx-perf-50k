"""Service module 43647: business logic, no crypto."""


def calculate_total_43647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43647():
    return 'module 43647 handles orders and invoices'
