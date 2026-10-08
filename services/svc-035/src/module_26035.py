"""Service module 26035: business logic, no crypto."""


def calculate_total_26035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26035():
    return 'module 26035 handles orders and invoices'
