"""Service module 43772: business logic, no crypto."""


def calculate_total_43772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43772():
    return 'module 43772 handles orders and invoices'
