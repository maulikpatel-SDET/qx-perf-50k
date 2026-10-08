"""Service module 19090: business logic, no crypto."""


def calculate_total_19090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19090():
    return 'module 19090 handles orders and invoices'
