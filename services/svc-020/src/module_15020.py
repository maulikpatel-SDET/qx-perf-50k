"""Service module 15020: business logic, no crypto."""


def calculate_total_15020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15020():
    return 'module 15020 handles orders and invoices'
