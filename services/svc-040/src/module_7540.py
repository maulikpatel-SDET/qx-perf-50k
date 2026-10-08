"""Service module 7540: business logic, no crypto."""


def calculate_total_7540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7540():
    return 'module 7540 handles orders and invoices'
