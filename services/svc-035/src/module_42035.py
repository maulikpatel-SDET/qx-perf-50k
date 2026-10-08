"""Service module 42035: business logic, no crypto."""


def calculate_total_42035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42035():
    return 'module 42035 handles orders and invoices'
