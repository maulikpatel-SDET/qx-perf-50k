"""Service module 26211: business logic, no crypto."""


def calculate_total_26211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26211():
    return 'module 26211 handles orders and invoices'
