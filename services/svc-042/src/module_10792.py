"""Service module 10792: business logic, no crypto."""


def calculate_total_10792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10792():
    return 'module 10792 handles orders and invoices'
