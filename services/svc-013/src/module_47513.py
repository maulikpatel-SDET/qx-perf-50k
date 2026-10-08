"""Service module 47513: business logic, no crypto."""


def calculate_total_47513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47513():
    return 'module 47513 handles orders and invoices'
