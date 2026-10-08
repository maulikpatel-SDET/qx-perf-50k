"""Service module 43792: business logic, no crypto."""


def calculate_total_43792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43792():
    return 'module 43792 handles orders and invoices'
