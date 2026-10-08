"""Service module 4398: business logic, no crypto."""


def calculate_total_4398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4398():
    return 'module 4398 handles orders and invoices'
